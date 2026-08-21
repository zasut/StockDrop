import csv
import os
import random 
from datetime import datetime

data_dir = "data/"
location_path = os.path.join(data_dir, "locations.csv")
products_path = os.path.join(data_dir, "products.csv")

os.makedirs(data_dir, exist_ok=True)


# location structure: location_id, name, type
locations = [
    ("WH-01", "Central Warehouse", "warehouse"),
    ("ST-01", "Downtown", "store"),
    ("ST-02", "Uptown", "store"),
    ("ST-03", "City Mall", "store")
]
store_locations = [loc for loc in locations if loc[2] == "store"]

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
    products.append((sku, name, category, price, cost))

formatted = []
for sku, name, category, price, cost in products:
    formatted.append((sku, name, category, f"{price:.2f}", f"{cost:.2f}"))

with open(products_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["sku", "name", "category", "unit_price", "unit_cost"])
    writer.writerows(formatted)

def make_ticket(ticket_id, rng):
    rows = []

    location = rng.choice(store_locations)
    location_id = location[0]

    channel = "in_store"
    sold_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    recorded_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    transaction_type = "sale"

    num_items = rng.randint(1, 3)

    for line_no in range(1, num_items + 1):
        product = rng.choice(products)
        quantity = rng.randint(1, 3)
        sku = product[0]
        product_name = product[1]
        unit_price = product[3]
        discount = 0.00
        line_total = unit_price * quantity
        
        rows.append([ticket_id, line_no, location_id, channel, sku, product_name, quantity, unit_price, discount, line_total, sold_at, recorded_at, transaction_type])
    return rows
