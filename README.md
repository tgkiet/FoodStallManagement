# FoodStallManagement

# Cần có file .json để kết nối với GG Sheets API nhé
## Cách làm
'''
A. Đăng ký Google Cloud Project
1. Vào trang: https://console.cloud.google.com/

2. Chọn hoặc tạo Project mới.
'''
Bấm Select project → NEW PROJECT
Đặt tên ví dụ: FoodStallManagement
Bấm Create
'''
3. Vào Project vừa tạo
'''
'''
B. Kích hoạt Google Sheets API
1. Trong Dashboard → Chọn APIs & Services → Library
2. Tìm Google Sheets API, Google Drive API
3. Bấm Enable
'''
'''
C. Tạo Service Account
1. Trong Google Cloud → Chọn IAM & Admin → Service Accounts
2. Bấm Create Service Account
'''
📌 Điền:

Name: di-bay-service

ID: tự động

Description: "For accessing Google Sheets"
'''
3. Bấm Create and Continue

4. Ở phần Grant role:

Chọn Basic > Editor (nếu muốn full đọc/ghi)

5. Bấm Continue → Done
'''
'''
✅ D. Tạo KEY JSON
1. Trong list Service Accounts → Click tên Service Account vừa tạo
2. Tab KEYS
3. Bấm ADD KEY > Create new key
4. Chọn JSON
5. Bấm Create → Tải file JSON về máy (Đây chính là file credential để code Python kết nối.)
6. Sau đó: COPY file service_account.json vào thư mục dự án: FoodStallManagement/service_account.json
'''
'''
E. Cấp quyền cho Service Account trên Google Sheets
✅ Mở Google Sheets bạn muốn truy cập (ví dụ Dì Bảy - Sales and Costs Raw)
✅ Bấm Share (Chia sẻ)
✅ Nhập email của Service Account (ví dụ: di-bay-service@YOUR_PROJECT_ID.iam.gserviceaccount.com)
✅ Chọn quyền Editor
✅ Bấm Send hoặc Done
'''