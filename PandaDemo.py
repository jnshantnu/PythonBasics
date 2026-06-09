import pandas as pd

# --------------- PART 1: CHIPOTLE ORDERS (TAB-DELIMITED) ---------------

print("=== CHIPOTLE ORDERS EXERCISES ===")

chipotle_url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv"
chipo = pd.read_csv(chipotle_url, sep="\t")

print("\nFirst 5 rows:")
print(chipo.head())

# Basic info
print("\nInfo:")
print(chipo.info())

print("\nColumns:", chipo.columns.tolist())

# Clean price: remove '$' and convert to float
chipo["item_price_clean"] = chipo["item_price"].str.replace("$", "", regex=False).astype(float)

print("\nItem price (clean) summary:")
print(chipo["item_price_clean"].describe())

# 1. Select orders where quantity > 1
high_qty = chipo[chipo["quantity"] > 1]
print("\nOrders with quantity > 1:")
print(high_qty.head())
