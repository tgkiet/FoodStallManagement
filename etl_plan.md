# ETL Plan for "Dì Bảy" Food Stall Project

## ✅ Extract
- Read from Google Sheets
  - Tab 1: "Purchase Costs (Chi phí)"
  - Tab 2: "Sales (Bán hàng)"
- Use pygsheets or gspread
- Load into pandas DataFrames

## ✅ Transform
- Purchase Costs
  - Clean date to YYYY-MM-DD
  - Ensure amount is numeric

- Sales
  - Clean date
  - Ensure quantity, unit price, total price are numeric
  - Parse "Topping thêm" column into rows
    - Split by ";"
    - Extract topping name, quantity, unit price

## ✅ Load
- Save Clean_Purchase.csv
- Save Clean_Sales.csv
- Save Clean_Sales_Toppings.csv
