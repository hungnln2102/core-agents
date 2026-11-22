# Core Agents & Constitution (SSOT Plugin)

> **Single Source of Truth (SSOT)** cho toàn bộ hệ thống Hiến pháp, 7 Subagents và 5 Kỹ năng dùng chung — đóng gói thành **1 Plugin duy nhất** cài đặt ở cấp toàn cục (Global) cho cả **Antigravity** và **Codex**.

## 📁 Cấu trúc Plugin SSOT

```text
core-agents/
├── plugin.json                        # Manifest cho Antigravity
├── .codex-plugin/plugin.json          # Manifest cho Codex
├── .agents/plugins/marketplace.json   # Local marketplace cho Codex
├── rules/AGENTS.md                    # Hiến pháp SSOT duy nhất (Antigravity tự nạp)
├── skills/                            # 12 skills (7 subagent roles + 5 core skills)
└── agents/                            # 7 định nghĩa subagent (.toml cho Codex)
```

## 🚀 Cài đặt 1 lần trên máy mới (Windows — Công ty / Nhà)

### 1. Clone repo về thư mục cố định
```powershell
git clone https://github.com/hungnln2102/core-agents.git E:\Project\core-agents
```

### 2. Gắn vào Antigravity (Directory Junction — không cần quyền Admin)
```powershell
New-Item -ItemType Junction -Path "$env:USERPROFILE\.gemini\config\plugins\core-agents" -Target "E:\Project\core-agents"
```

### 3. Gắn vào Codex (Global Subagents + Local Marketplace)
```powershell
New-Item -ItemType Junction -Path "$env:USERPROFILE\.codex\agents" -Target "E:\Project\core-agents\agents"
```
Trong `$env:USERPROFILE\.codex\config.toml`, bật:
```toml
[plugins."core-agents@core-agents-local"]
enabled = true

[marketplaces.core-agents-local]
source_type = "local"
source = '\\?\E:\Project\core-agents'
```

## 🔄 Cập nhật Hiến pháp / Skills cho toàn bộ dự án
Chỉ cần sửa 1 chỗ duy nhất tại `E:\Project\core-agents\rules\AGENTS.md` (hoặc chạy `git pull` trên máy còn lại) — **tất cả dự án** trên Antigravity và Codex sẽ tự động nhận bản mới mà không cần submodule `.agents` trong từng repo.
