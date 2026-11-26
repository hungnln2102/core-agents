# Core Agents

Bộ cấu hình gồm một Hiến pháp chung và bảy Hiến pháp vai trò. Năng lực chuyên môn nằm trong cấu hình agent. Repo ứng dụng cung cấp stack, cấu trúc, lệnh kiểm thử và quy tắc nghiệp vụ qua `AGENTS.md`.

## Cấu trúc

- [Hiến pháp chung](rules/AGENTS.md) quy định quyền hạn, phê duyệt và kiểm chứng.
- [Hiến pháp vai trò](rules/roles/) quy định trách nhiệm, điều kiện áp dụng năng lực và điểm bàn giao.
- [Hướng dẫn giao dịch](rules/references/acid-transactions.md) là nguồn dùng chung cho Backend và Finance.
- [Đặc tả và hướng dẫn chuyển đổi](docs/agent-constitutions-spec.md) đối chiếu các skill cũ với năng lực tương ứng.
- [Cấu hình Codex](agents/) được sinh từ Hiến pháp. Sửa nguồn Markdown rồi sinh lại bằng [scripts/agents.py](scripts/agents.py).

## Cài đặt cho Codex

Clone repo vào thư mục anh chọn, rồi chạy từ thư mục gốc của repo với Python 3.11 trở lên.

```sh
python scripts/agents.py check
python scripts/agents.py install
```

Installer dùng thư mục `agents` trong `CODEX_HOME` hoặc trong thư mục cấu hình Codex mặc định. Có thể chỉ định đích bằng `--directory`. Installer giữ các agent khác và báo nếu gặp file cùng tên chưa được quản lý bởi bộ cài này. Nếu từng dùng junction tới checkout, hãy chuyển sang thư mục agents thông thường, hoặc cập nhật checkout đang được junction trỏ tới. Với file cũ cùng tên, lưu bản sao và xóa hoặc chuyển file cũ ra ngoài thư mục agents trước khi cài. Mở phiên mới để danh mục nhận cấu hình đã cài.

Cài TOML để đăng ký agent. Manifest marketplace giữ định danh plugin cho người đang dùng bản cũ. Có thể tắt plugin cũ trong Codex để bỏ catalog skill còn lưu trong cache.

## Dùng trên runtime khác

Manifest gốc giữ định danh plugin. Để chuyển cấu hình sang runtime khác, dùng Hiến pháp chung, Hiến pháp của vai trò và `AGENTS.md` của repo làm đầu vào cho cơ chế chỉ dẫn tương ứng. Với Backend và Finance, nạp thêm tài liệu giao dịch. Thư mục `rules/roles/` là nguồn tài liệu. Mức hỗ trợ tự nạp phụ thuộc runtime và cần kiểm chứng trước khi dùng.

## Thay đổi và phát hành

```sh
python scripts/agents.py build
python -m unittest discover -s tests
git diff --check
```

Một năng lực mới phải có vai trò chủ trì, điều kiện áp dụng và một nguồn hướng dẫn. Thay đổi Hiến pháp hoặc cấu hình agent đi qua nhánh và pull request. Sau khi hợp nhất phiên bản đã duyệt, chạy lại installer rồi mở phiên mới. Có thể quay lại phiên bản đã kiểm chứng bằng cách cài lại từ checkout của phiên bản đó.
