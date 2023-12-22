# XoSoKeno Analyzer

## Mô tả

Đây là một đoạn mã Python được thiết kế để phân tích kết quả xổ số kiểu Keno từ trang web [minhchinh.com](https://www.minhchinh.com/xo-so-dien-toan-keno.html#containerKQKeno). Đoạn mã sử dụng thư viện `requests` để gửi yêu cầu HTTP và `BeautifulSoup` để phân tích nội dung HTML.

## Các Màu Sắc ANSI

Mã ANSI được định nghĩa để thêm màu sắc vào in ra màn hình. Các màu bao gồm đỏ, xanh lá, vàng, xanh dương, hồng, và xanh da trời.

## Các Hàm Hỗ Trợ

1. **`convert_name(name)`**
   - Chuyển đổi tên class thành tên hiển thị tương ứng.

2. **`is_number(string)`**
   - Kiểm tra xem một chuỗi có phải là số hay không.

## Các Bước Thực Hiện

1. Gửi yêu cầu POST đến trang web để lấy nội dung HTML.
2. Phân tích HTML để lấy danh sách các trang.
3. Lặp qua mỗi trang và trích xuất thông tin kết quả xổ số.
4. In ra màn hình kết quả với màu sắc tương ứng:
   - Chẵn: Màu xanh lá
   - Lẻ: Màu vàng
   - Hòa: Màu đỏ

## Kết Quả

Kết quả sẽ được hiển thị với màu sắc tương ứng, kèm theo số trang và thông tin chi tiết về mỗi kết quả xổ số.

## Lưu Ý

1. Cần cài đặt thư viện `requests` và `BeautifulSoup` trước khi chạy mã:
   ```bash
   pip install requests beautifulsoup4
   ```

2. Mã này được xây dựng để phân tích trang web cụ thể và có thể cần được điều chỉnh nếu trang web thay đổi cấu trúc HTML của mình.

3. Có thể chỉnh sửa mã để lưu trữ dữ liệu kết quả hoặc thực hiện các xử lý phức tạp hơn tùy thuộc vào yêu cầu cụ thể của bạn.
