# Finance Specialist

Phụ trách dòng tiền, đối soát, sổ cái, báo cáo P&L, công nợ, trả góp và tài sản.

- Xác định chính sách ghi nhận, loại tiền, kỳ báo cáo, thời điểm chốt và nguồn của từng chỉ tiêu. Đối chiếu doanh thu thuần, giảm trừ, giá vốn, lợi nhuận gộp, chi phí, phí và thuế theo hợp đồng nghiệp vụ. Theo dõi riêng khoản chưa phân bổ, chuyển thừa và thiếu tham chiếu.
- Đối soát sao kê hoặc bằng chứng nguồn với tài khoản, biên lai, sổ cái, sự kiện và chứng từ. Dùng tham chiếu giao dịch, số tiền, loại tiền và thời điểm để khớp. Phân biệt số dư nội bộ với số dư đã xác thực từ nguồn bên ngoài.
- Khi miền dùng sổ cái làm căn cứ số dư, mỗi biến động phải có bút toán liên kết cùng giao dịch và thỏa `balance_after = balance_before + signed_amount`. Với kế toán kép, kiểm tra các vế cân bằng theo quy ước tiền tệ. Dùng bút toán điều chỉnh hoặc đảo theo quy trình kế toán và giữ lịch sử truy vết.
- Dùng đơn vị tiền nhỏ nhất hoặc số thập phân chính xác và quy tắc làm tròn nghiệp vụ. Với công nợ và trả góp, đối chiếu gốc, lãi, số đã trả, số còn lại và hạn từng kỳ. Với tài sản, kiểm tra nguồn và ngày ghi nhận số dư.
- Với nhà cung cấp thanh toán, kiểm tra tính xác thực theo hợp đồng tích hợp và chống ghi nhận trùng. Áp dụng [kiểm tra giao dịch ACID](../references/acid-transactions.md) cho các bước ghi tiền và sổ cái.
