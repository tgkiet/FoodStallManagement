import pandas as pd

# Buoc 1: Clean SALES
print("\n DANG CLEAN SALES DATA...")
df_sales = pd.read_csv('raw_sales.csv')

# Lam sach cot "Ngày" (strip space)
df_sales['Ngày'] = df_sales['Ngày'].str.strip()

# Viet hoa chuan cho cot "Sản phẩm chính"
df_sales['Sản phẩm chính'] = df_sales['Sản phẩm chính'].str.strip().str.title()

# Đảm bảo số nguyên cho Số lượng, Giá đơn vị, Tổng giá
for col in ['Số lượng', 'Giá đơn vị', 'Tổng giá']:
    df_sales[col] = pd.to_numeric(df_sales[col], errors='coerce')

# Log lỗi nếu có giá trị null sau khi covert
if df_sales.isnull().any().any():
    print("CẢNH BÁO: Dữ liệu SALES có giá trị null sau khi làm sạch. Vui lòng kiểm tra lại.")
    print(df_sales[df_sales.isnull().any(axis=1)])

# Xuất dữ liệu đã làm sạch
df_sales.to_csv('sales_clean.csv', index=False)
print("\n✅ Dữ liệu SALES đã được làm sạch và lưu vào 'sales_clean.csv'.")


# Buoc 2: Clean PURCHASES COSTS

print("\n DANG CLEAN PURCHASES COSTS DATA...")
df_purchase = pd.read_csv('raw_purchase_costs.csv')

# Lam sach cot "Ngày" (strip space)
df_purchase['Ngày'] = df_purchase['Ngày'].str.strip()

# lam sach Danh muc
df_purchase['Danh mục'] = df_purchase['Danh mục'].str.strip().str.title()

# đảm bảo Số tiền là số nguyên
df_purchase['Số tiền'] = pd.to_numeric(df_purchase['Số tiền'], errors='coerce')

# Log lỗi nếu có giá trị null sau khi covert
if df_purchase.isnull().any().any():
    print("CẢNH BÁO: Dữ liệu PURCHASES COSTS có giá trị null sau khi làm sạch. Vui lòng kiểm tra lại.")
    print(df_purchase[df_purchase.isnull().any(axis=1)])
    
# Xuất file dữ liệu đã làm sạch
df_purchase.to_csv('purchases_costs_clean.csv', index=False)
print("\n✅ Dữ liệu PURCHASES COSTS đã được làm sạch và lưu vào 'purchases_costs_clean.csv'.")

