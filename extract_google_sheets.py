import pygsheets
import pandas as pd

# Authorize with the service account file
gc = pygsheets.authorize(service_file='foodstallmanagement-ad2e247a041b.json')

# Open the Google Sheet by its title
sheet = gc.open('Dì Bảy - Sales and Costs Raw')

# Select worksheets by title
sales_ws = sheet.worksheet_by_title('Sales (Bán hàng)')
costs_ws = sheet.worksheet_by_title('Purchase Costs (Chi phí)')

# Get data as DataFrames
df_sales = sales_ws.get_as_df()
df_costs = costs_ws.get_as_df()

# Print to check the data
print("\n Sales Data:")
print(df_sales)

print("\n Purchase Costs Data:")
print(df_costs)

# ✅ Optional: Save raw CSV
df_sales.to_csv('raw_sales.csv', index=False)
df_costs.to_csv('raw_purchase_costs.csv', index=False)

print("\n✅ CSV files exported successfully!")