# Đặc tả chuyển đổi Hiến pháp và năng lực Core Agents

## Phạm vi

Người dùng có thể gọi bảy agent theo ID hiện hành trong nhiều repo. Mỗi agent xác định năng lực cần áp dụng từ nhiệm vụ được giao, Hiến pháp vai trò và quy ước của repo sở hữu. Bộ phân phối Core Agents dùng các định nghĩa agent để cung cấp năng lực chuyên môn.

- Hiến pháp chung quy định thẩm quyền, ba mức thay đổi, Gói Đề Xuất Hợp Nhất, production, Git và nghiệm thu.
- Bảy Hiến pháp vai trò tại `rules/roles/` giữ năng lực, điều kiện áp dụng, đầu ra và bàn giao. Tài liệu tham chiếu ACID tại `rules/references/acid-transactions.md` dùng chung cho Backend và Finance.
- TOML được sinh từ Hiến pháp chung và đúng một Hiến pháp vai trò. Backend và Finance có thêm tham chiếu ACID. Bảy ID agent giữ nguyên.
- Installer Python cài bảy TOML vào thư mục `agents` của Codex. Khi cập nhật, installer giữ cấu hình ngoài bảy ID quản lý và xử lý minh bạch định nghĩa cùng tên đã tùy chỉnh.
- Hướng dẫn cài đặt ghi trạng thái hỗ trợ theo runtime có bằng chứng. Việc Antigravity tự nạp các Hiến pháp vai trò cần được xác minh riêng.

## Ánh xạ 12 kỹ năng hiện hữu

| Nguồn cũ | Nguồn sau chuyển đổi | Điều kiện áp dụng |
| --- | --- | --- |
| `orchestrator` | `roles/orchestrator.md` | Điều phối giao việc, tổng hợp đề xuất, rà soát và nghiệm thu. |
| `lead-planner` | `roles/lead-planner.md` | Xác định hành vi, phạm vi, quyết định nghiệp vụ hoặc tiêu chí nghiệm thu. |
| `backend-specialist` | `roles/backend-specialist.md` | Thay đổi API, truy vấn, tích hợp hoặc tác vụ nền. |
| `frontend-lead` | `roles/frontend-lead.md` | Thay đổi giao diện, tương tác hoặc khả năng tiếp cận. |
| `finance-specialist` | `roles/finance-specialist.md` | Giao dịch tiền, hạch toán, đối soát, công nợ hoặc báo cáo tài chính. |
| `security-auditor` | `roles/security-auditor.md` | Rà soát xác thực, phân quyền, bí mật, dữ liệu cá nhân hoặc tái sử dụng tại bề mặt thay đổi. |
| `qa-automation` | `roles/qa-automation.md` | Lập và chạy kiểm chứng phù hợp với hành vi, mức thay đổi và quy ước repo. |
| `spec-kit` | `rules/AGENTS.md`, `roles/lead-planner.md` | Thay đổi có ghi cần đề xuất. Lead Planner làm rõ các mục nghiệp vụ và tiêu chí phù hợp. |
| `db-schema-source-of-truth` | `roles/backend-specialist.md` và AGENTS.md của repo | Chạm schema hoặc truy vấn. Xác định nguồn schema từ repo trước khi thay đổi. |
| `acid-database-transaction-review` | `rules/references/acid-transactions.md` | Thay đổi cần nhất quán giao dịch, chống trùng, đồng thời hoặc đối soát. Backend xét kỹ thuật, Finance xét bất biến tài chính. |
| `task-tracking` | `rules/AGENTS.md`, `roles/lead-planner.md` | Nhiệm vụ có tracker thuộc phạm vi đã duyệt. |
| `vietnamese-diacritics` | `rules/AGENTS.md` | Soạn nội dung tiếng Việt. Kiểm tra encoding theo repo và loại file. |

Các đường dẫn `roles/` trong bảng tính từ `rules/`. Hướng dẫn phụ thuộc vào Node.js, Knex, PostgreSQL, Adobe hoặc một hệ thống thiết kế cụ thể chỉ áp dụng khi repo sở hữu dùng và xác nhận chúng.

## Trình tự thực hiện

- [x] Khảo sát định nghĩa hiện hành, catalog, cache cài đặt và các tham chiếu riêng của dự án.
- [x] Đối chiếu phạm vi đã duyệt và đặc tả ánh xạ 12 kỹ năng.
- [x] Hoàn thiện Hiến pháp chung, bảy Hiến pháp vai trò và tài liệu ACID.
- [x] Sinh bảy TOML, cập nhật installer và hướng dẫn cài đặt. Đối chiếu tên agent và dữ liệu sinh ra với tài liệu nguồn.
- [x] Xóa các bản gốc đã được thay thế và cập nhật manifest để ngừng công bố catalog cũ. Xác định các tham chiếu trong repo tiêu thụ trước khi đánh giá tương thích của từng repo.
- [x] Kiểm thử cài mới, cập nhật bản cũ, giữ lại định nghĩa của bên thứ ba và lặp lại thao tác cài. Kiểm tra văn bản, JSON, TOML, đường dẫn và chênh lệch Git trong phạm vi.
- [ ] Tạo commit, đẩy nhánh và mở pull request theo phần Git đã được duyệt.

## Tiêu chí nghiệm thu

```gherkin
Scenario: Khảo sát một repo
  Given người dùng yêu cầu rà soát hoặc đọc mã nguồn
  When agent thu thập bằng chứng trong phạm vi được giao
  Then agent trả kết quả trong hội thoại và trạng thái repo giữ nguyên

Scenario Outline: Phê duyệt một lần trước khi thay đổi
  Given tác vụ thuộc mức <muc>
  When agent trình một Gói Đề Xuất Hợp Nhất
  Then mọi thao tác ghi chờ phê duyệt rõ ràng
  And sau phê duyệt agent thực hiện các bước trong phạm vi đã trình

  Examples:
    | muc   |
    | NHỎ   |
    | CHUẨN |
    | LỚN   |

Scenario: Xác minh quyền production trong thay đổi mức LỚN
  Given một tác vụ được duyệt cho môi trường thử nghiệm
  When phát sinh đề nghị thực thi cùng thao tác trên production
  Then agent giữ các thao tác production ở trạng thái chờ phê duyệt
  And phần công việc thử nghiệm đã duyệt có thể tiếp tục nếu độc lập

Scenario: Tạo và cài bảy agent
  Given Hiến pháp chung và bảy Hiến pháp vai trò hợp lệ
  When bộ tạo sinh TOML và installer cài vào thư mục agents
  Then bảy ID cũ tồn tại và mỗi TOML chứa đúng Hiến pháp vai trò
  And Backend và Finance chứa tham chiếu ACID dùng chung
  And định nghĩa agent của bên thứ ba giữ nguyên

Scenario: Áp dụng năng lực trong hai repo khác stack
  Given cùng một Backend Specialist được giao thay đổi truy vấn ở hai repo
  When mỗi repo dùng stack và nguồn schema khác nhau
  Then agent xác định nguồn schema và điểm vào tại từng repo trước khi sửa

Scenario: Trình thay đổi Hiến pháp qua pull request
  Given chủ dự án phê duyệt thay đổi và thao tác Git để mở pull request
  When bộ kiểm chứng đã chạy và các file trong phạm vi được commit
  Then agent mở pull request từ nhánh thay đổi để người có thẩm quyền xem xét
```

## Ví dụ áp dụng

- Đọc log để tìm nguyên nhân request chậm là khảo sát. Khi đề xuất sửa truy vấn, Backend tra quy ước schema của repo và phân loại thay đổi theo phạm vi ảnh hưởng.
- Sửa chính tả trong tài liệu là mức NHỎ. Gói ngắn vẫn gồm hai phần và một tiêu chí kiểm tra văn bản.
- Thêm bộ lọc giao diện vào một màn hình là mức CHUẨN nếu tác động giới hạn. Frontend kiểm tra component sẵn có và QA xác minh trạng thái tải, rỗng và kết quả lọc phù hợp.
- Sửa cách ghi nhận khoản thanh toán là mức LỚN. Finance xác định bất biến về số dư và sổ cái, Backend kiểm tra quyền ghi và giao dịch, QA xác minh lỗi giữa chừng và giao dịch lặp.

### Ví dụ Gói Đề Xuất Hợp Nhất mức NHỎ

**Spec-Kit**

- **User Stories & Bóc tách phạm vi** — Người dùng đọc đúng tên nút trong tài liệu trợ giúp.
- **Reuse Audit & Redlines** — Dùng tên hiện có trên giao diện. Phạm vi chỉ gồm một dòng tài liệu.
- **Tiêu chí nghiệm thu**

```gherkin
Scenario: Tài liệu dùng đúng tên nút
  Given ứng dụng hiển thị nút "Lưu thay đổi"
  When người dùng đọc hướng dẫn lưu
  Then hướng dẫn dùng tên "Lưu thay đổi"
```

**Pre-Flight Check**

- **Vấn đề / Nguyên nhân gốc** — Chuỗi trong tài liệu khác nhãn đã xác minh trên giao diện.
- **Phương án đề xuất** — Sửa chuỗi trong tài liệu rồi đối chiếu lại với giao diện.
- **File dự kiến tác động** — `docs/help.md` của repo ví dụ.
- **Rủi ro & đối sách** — Tài liệu có thể mô tả nhiều phiên bản. Xác nhận đoạn cần sửa thuộc phiên bản hiện tại.
- **Kế hoạch kiểm thử** — Đọc lại câu hướng dẫn và kiểm tra diff.
- **Kiểm soát lỗi text** — Kiểm tra UTF-8 và dấu tiếng Việt trong file sửa.

Xin phê duyệt thay đổi một dòng tài liệu trước khi ghi.

## Tích hợp các dự án đang dùng phiên bản cũ

- Giữ bảy ID agent. Với lời gọi tên skill cũ, dùng vai trò hoặc chỉ dẫn tương ứng trong bảng ánh xạ. Hướng dẫn schema, component và nghiệp vụ cụ thể thuộc repo sở hữu.
- Khi rà các file AGENTS.md hiện hành của ba dự án liên quan, còn hai tham chiếu `db-schema-source-of-truth` và `acid-database-transaction-review` trong `otp_portal`. Thay tham chiếu thứ nhất bằng quy ước schema của dự án, tham chiếu thứ hai bằng năng lực giao dịch của Backend và Finance. Đợt này chỉ cập nhật repo Core Agents.
- Cấu hình được kiểm chứng tĩnh và qua bộ cài Codex. Kết quả đó chưa chứng minh Antigravity tự phát hiện vai trò.
