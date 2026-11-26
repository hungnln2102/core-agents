# Kiểm tra giao dịch ACID

Áp dụng khi các bước ghi phải thành công cùng nhau hoặc có thể bị gọi lặp, cạnh tranh hay lỗi giữa chừng. Bắt đầu từ bất biến nghiệp vụ, dữ liệu, thao tác ghi, trigger, sự kiện và tác động ngoài cơ sở dữ liệu.

- **Atomicity**. Đặt các bước ghi phụ thuộc vào một giao dịch, truyền cùng ngữ cảnh giao dịch qua các lời gọi và kiểm tra rollback khi một bước bắt buộc thất bại. Kiểm tra trigger và tác vụ phụ. Với hệ thống độc lập, xác định cách bù trừ hoặc phục hồi theo hợp đồng.
- **Consistency**. Kiểm tra ràng buộc và bất biến sau commit, ví dụ biên lai khớp trạng thái thanh toán, số dư khớp sổ cái, tổng hợp khớp nguồn. Xác định lớp chịu trách nhiệm tính toán để tránh trigger và ứng dụng cùng cộng một khoản. Với thay đổi schema, kiểm chứng dữ liệu cũ và backfill.
- **Isolation**. Tìm cửa sổ đọc rồi ghi, lost update, ghi trùng và thứ tự khóa xung đột. Chọn cơ chế thích hợp như khóa dòng, cập nhật có điều kiện, kiểm tra phiên bản, ràng buộc duy nhất hoặc tuần tự hóa. Nếu dùng khóa idempotency, bảo đảm lưu khóa cùng kết quả ở nơi kiểm soát được tính duy nhất.
- **Durability**. Chỉ báo thành công sau commit với hợp đồng chờ kết quả. Khi cần sự kiện bền vững đi kèm thay đổi dữ liệu, ghi outbox trong cùng giao dịch, phát sau commit và xử lý giao nhận lặp an toàn. Kiểm tra lỗi phát, retry và khả năng đối soát.
- **Bằng chứng**. Kiểm tra thành công, lỗi giữa chừng, gọi lặp, hai tác vụ cùng tài nguyên và lỗi phân phối sự kiện nếu liên quan. Báo cáo mỗi mục ACID là đạt, có rủi ro hoặc chưa kiểm chứng, kèm vị trí và biện pháp sửa.
