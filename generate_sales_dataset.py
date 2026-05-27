import pandas as pd
import random
from faker import Faker

fake = Faker()

regions = ["East", "West", "South", "Central"]
segments = ["Consumer", "Corporate", "Home Office"]

categories = {
    "Furniture": ["Chair", "Table", "Bookcase"],
    "Office Supplies": ["Paper", "Binders", "Pens"],
    "Technology": ["Laptop", "Printer", "Phone"]
}

payment_modes = ["Cash", "Card", "UPI"]

data = []

for i in range(500):

    category = random.choice(list(categories.keys()))
    sub_category = random.choice(categories[category])

    sales = round(random.uniform(100, 5000), 2)
    profit = round(random.uniform(-500, 1500), 2)

    row = {
        "Order ID": f"ORD{i+1}",
        "Order Date": fake.date_between(start_date='-2y', end_date='today'),
        "Customer Name": fake.name(),
        "Segment": random.choice(segments),
        "Region": random.choice(regions),
        "State": fake.state(),
        "City": fake.city(),
        "Category": category,
        "Sub-Category": sub_category,
        "Product Name": sub_category + " Model",
        "Sales": sales,
        "Profit": profit,
        "Quantity": random.randint(1, 10),
        "Payment Mode": random.choice(payment_modes)
    }

    data.append(row)

df = pd.DataFrame(data)

df.to_csv("sales_dataset.csv", index=False)

print("Sales dataset generated successfully!")
