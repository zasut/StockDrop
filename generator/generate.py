import csv
import os

data_dir = "data/"
location_path = os.path.join(data_dir, "locations.csv")
products_path = os.path.join(data_dir, "products.csv")

os.makedirs(data_dir, exist_ok=True)


# location structure: location_id, name, type
locations = [
    ("WH-01", "Central Warehouse", "warehouse"),
    ("ST-01", "Downtown", "store")
]

with open(location_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["location_id", "name", "type"])
    writer.writerows(locations)

# product structure: sku(generates on line 24), name, category, unit_price, unit_cost
raw = [
    ("black sneaker", "shoes", 25.00, 10.00),
    ("portable charger", "electronics", 7.99, 3.50),
    ("limited edition aqua sneaker", "hot_drop", 69.99, 30.00),
    ("yellow baby chicken room decoration", "decor", 13.99, 7.99),
    ("black business shirt", "clothing",  34.99, 15.99)
]

products = []
for i, (name, category, price, cost) in enumerate(raw, start=1):
    sku = f"{category[:3].upper()}-{i:04d}"
    products.append((sku, name, category, f"{price:.2f}", f"{cost:.2f}"))

with open(products_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["sku", "name", "category", "unit_price", "unit_cost"])
    writer.writerows(products)