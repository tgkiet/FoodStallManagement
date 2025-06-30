import pandas as pd

# Buoc 1: Doc file CSV da xuat o buoc extract_google_sheets.py
df_sales = pd.read_csv('raw_sales.csv')
print("\n Dữ liệu sales ban đầu: ")
print(df_sales)

# Bước 2: Tạo list để chứa kết quả topping đã parse
parsed_rows = []

# Bước 3: Duyệt từng dòng sales
for _, row in df_sales.iterrows():
    ngay = row['Ngày']
    san_pham = row['Sản phẩm chính']
    topping_text = str(row['Topping thêm'])
    
    # Nếu topping trống thì bỏ qua
    if topping_text.strip() == '':
        continue
    
    # ✅ Ví dụ: "Chả giò:10x5000; Trứng:5x5000"
    toppings = topping_text.split(';')
    for t in toppings:
        t = t.strip()  # Loại bỏ khoảng trắng
        if not t:
            continue
        try: 
            # Parse phan text
            name_qty_price = t.split(':')
            topping_name = name_qty_price[0].strip()
            
            qty_price = name_qty_price[1].split('x')
            qty = int(qty_price[0].strip())
            price = int(qty_price[1].strip())
            
            # Append kết quả vào list
            parsed_rows.append({
                'Ngày': ngay,
                'Sản phẩm chính': san_pham,
                'Topping': topping_name,
                'Số lượng': qty,
                'Giá đơn vị topping': price
            })
        except Exception as e:
            print(f"Lỗi khi parse topping '{t}' ở ngày {ngay}: {e}")
            
# Bước 4: Tạo DataFrame mới
df_topping_clean = pd.DataFrame(parsed_rows)

print("\n Dữ liệu topping đã parse: ")
print(df_topping_clean)

# Bước 5: Lưu DataFrame đã parse vào file CSV
df_topping_clean.to_csv('topping_clean.csv', index=False)
print("\n✅ Dữ liệu topping đã parse và lưu vào topping_clean.csv thành công!")