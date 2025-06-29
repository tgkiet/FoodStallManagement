# FoodStallManagement

## Các file cần setup config

Để kết nối với Google Sheets API, phải cần một tệp `.json` chứa thông tin xác thực. Dưới đây là hướng dẫn chi tiết cách tạo và cấu hình:

## Hướng dẫn kết nối Google Sheets API

### A. Đăng ký Google Cloud Project

1.  Truy cập [Google Cloud Console](https://console.cloud.google.com/).
2.  **Chọn hoặc tạo một Project mới:**
    * Nhấn "Select project" (Chọn dự án) → "NEW PROJECT" (Dự án mới).
    * Đặt tên dự án, ví dụ: `FoodStallManagement`.
    * Nhấn "Create" (Tạo).
3.  Truy cập vào Project vừa tạo.

### B. Kích hoạt Google Sheets API

1.  Trong Dashboard, chọn **APIs & Services** (API và Dịch vụ) → **Library** (Thư viện).
2.  Tìm kiếm `Google Sheets API` và `Google Drive API`.
3.  Nhấn **Enable** (Bật) cho cả hai API.

### C. Tạo Service Account

1.  Trong Google Cloud, chọn **IAM & Admin** (IAM và Quản trị) → **Service Accounts** (Tài khoản dịch vụ).
2.  Nhấn **Create Service Account** (Tạo tài khoản dịch vụ).
    * **Name (Tên):** `di-bay-service`
    * **ID:** (Tự động điền)
    * **Description (Mô tả):** "For accessing Google Sheets"
3.  Nhấn **Create and Continue** (Tạo và tiếp tục).
4.  Ở phần "Grant role" (Cấp vai trò):
    * Chọn **Basic** > **Editor** (nếu bạn muốn có quyền đọc/ghi đầy đủ).
5.  Nhấn **Continue** (Tiếp tục) → **Done** (Hoàn tất).

### D. Tạo KEY JSON

1.  Trong danh sách Service Accounts, click vào tên Service Account vừa tạo.
2.  Chọn tab **KEYS** (Khóa).
3.  Nhấn **ADD KEY** (Thêm khóa) > **Create new key** (Tạo khóa mới).
4.  Chọn định dạng **JSON**.
5.  Nhấn **Create** (Tạo) → Tệp JSON sẽ được tải về máy của bạn. (Đây chính là tệp thông tin xác thực để mã Python của bạn kết nối).
6.  **Sao chép tệp `service_account.json` này vào thư mục dự án của bạn:** `FoodStallManagement/service_account.json`.

### E. Cấp quyền cho Service Account trên Google Sheets

1.  Mở Google Sheets mà bạn muốn truy cập (ví dụ: "Dì Bảy - Sales and Costs Raw").
2.  Nhấn nút **Share** (Chia sẻ) ở góc trên bên phải.
3.  Nhập email của Service Account của bạn vào ô chia sẻ (ví dụ: `di-bay-service@YOUR_PROJECT_ID.iam.gserviceaccount.com`).
4.  Chọn quyền **Editor** (Người chỉnh sửa).
5.  Nhấn **Send** (Gửi) hoặc **Done** (Hoàn tất).