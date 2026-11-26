"""Test the Codex adapters and installation in temporary directories."""
import importlib.util
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import tomllib
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("core_agents", ROOT / "scripts/agents.py")
assert SPEC and SPEC.loader
agents = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(agents)


class AgentTests(unittest.TestCase):
    def test_seven_valid_constitutions(self):
        configs = agents.render()
        agents.check(configs)
        self.assertEqual(len(configs), 7)
        common = agents.read(ROOT / "rules/AGENTS.md").strip()
        acid = agents.read(ROOT / "rules/references/acid-transactions.md").strip()
        for role in agents.ROLES:
            with self.subTest(role=role):
                config = tomllib.loads(configs[f"{role}-agent.toml"])
                instructions = config["developer_instructions"]
                self.assertTrue(instructions.startswith(common + "\n\n"))
                body = agents.read(ROOT / "rules/roles" / f"{role}.md").strip()
                self.assertIn(body, instructions)
                self.assertEqual(role in agents.TRANSACTION_ROLES, acid in instructions)

    def test_install_idempotent_and_preserves_other_agents(self):
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary)
            custom = target / "custom.toml"
            custom.write_bytes(b"custom")
            configs = agents.render()
            self.assertEqual(agents.install(configs, target), 7)
            self.assertEqual(agents.install(configs, target), 0)
            (target / "backend-specialist-agent.toml").write_text(agents.MANAGED, encoding="utf-8")
            self.assertEqual(agents.install(configs, target), 1)
            self.assertEqual(custom.read_bytes(), b"custom")

    def test_install_preserves_conflicting_file_and_writes_nothing(self):
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary)
            conflicting = target / "backend-specialist-agent.toml"
            conflicting.write_bytes(b"custom")
            with self.assertRaisesRegex(ValueError, "Existing unmanaged"):
                agents.install(agents.render(), target)
            self.assertEqual(list(target.iterdir()), [conflicting])
            self.assertEqual(conflicting.read_bytes(), b"custom")

    def test_relocated_checkout(self):
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            checkout = base / "checkout with spaces"
            shutil.copytree(ROOT, checkout, ignore=shutil.ignore_patterns(".git", "__pycache__"))
            target = base / "external agents"
            for args in (["build"], ["install", "--directory", str(target)]):
                result = subprocess.run(
                    [sys.executable, str(checkout / "scripts/agents.py"), *args],
                    cwd=base, capture_output=True, text=True,
                )
                self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(len(list(target.glob("*.toml"))), 7)
