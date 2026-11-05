# Core AI Agents & Constitution (SSOT)

> **Single Source of Truth** cho toàn bộ hệ thống Agent, Subagent và Hiến pháp làm việc (Antigravity & Codex Extension).

---

## 🏛️ Danh Sách Subagents & Kỹ Năng
1. 👑 **Orchestrator Agent**: Tổng chỉ huy kỹ thuật & Spec-Kit Gatekeeper.
2. 📝 **Lead Planner**: Thư ký quy hoạch, soạn thảo Spec-Kit & điều phối ký ức.
3. ⚙️ **Backend Specialist**: Node.js, Knex, PostgreSQL & Automation.
4. 🎨 **Frontend Lead**: React TSX, Tailwind CSS, Vanilla CSS, UI/UX.
5. 🧪 **QA Automation**: Unit test, Integration test, Playwright.
6. 🛡️ **Security Auditor**: Rà soát tái sử dụng mã nguồn & bảo mật.
7. 💰 **Finance Specialist**: Quản trị tài chính, đối soát SePay/USDT, P&L.
8. 📋 **Spec-Kit**: Quy trình Spec-Driven Development (SDD) chuẩn Gherkin.
9. ⚖️ **ACID DB Review**: Chuẩn kiểm toán giao dịch cơ sở dữ liệu.
10. 🗄️ **DB Schema SSOT**: Chuẩn truy vấn PostgreSQL qua `dbSchema.js`.

---

## 🚀 Hướng Dẫn Tích Hợp Dự Án Mới (Git Submodule)

### 1. Nhúng Submodule vào dự án mới
Tại thư mục gốc của dự án (ví dụ `otp_portal`):
```bash
git submodule add https://github.com/hungnln2102/core-agents.git .agents
```

### 2. Tạo file `AGENTS.md` tại thư mục gốc dự án
Tạo file `AGENTS.md` ở root dự án để trỏ tới Hiến pháp:
```markdown
@[HIẾN PHÁP AI AGENT TỐI CAO](.agents/AGENTS.md)
```

### 3. Đồng bộ khi clone dự án về máy mới (Máy ở nhà / Công ty)
Khi clone dự án về máy khác:
```bash
git clone --recurse-submodules <URL_DU_AN>
```
Hoặc nếu đã clone từ trước:
```bash
git submodule update --init --recursive
```

### 4. Cập nhật khi có thay đổi luật mới
Khi repo `core-agents` có phiên bản mới, cập nhật ở dự án con bằng lệnh:
```bash
git submodule update --remote --merge
```
