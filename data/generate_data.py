"""Generates a realistic 2-year daily retail sales dataset across regions/categories."""
import numpy as np
import pandas as pd

rng = np.random.default_rng(7)

dates = pd.date_range("2023-01-01", "2024-12-31", freq="D")
regions = ["North", "South", "East", "West"]
categories = ["Electronics", "Apparel", "Home & Garden", "Groceries", "Toys"]

rows = []
for d in dates:
    month_factor = 1 + 0.5 * np.sin(2 * np.pi * (d.month - 1) / 12)  # seasonality
    weekend_factor = 1.3 if d.weekday() >= 5 else 1.0
    holiday_boost = 2.2 if (d.month == 12 and d.day >= 15) else 1.0
    for region in regions:
        region_base = {"North": 1.1, "South": 0.9, "East": 1.0, "West": 1.2}[region]
        for cat in categories:
            cat_base = {
                "Electronics": 850, "Apparel": 420, "Home & Garden": 380,
                "Groceries": 610, "Toys": 230,
            }[cat]
            noise = rng.normal(1.0, 0.15)
            units = max(0, rng.poisson(8 * region_base))
            revenue = round(cat_base * month_factor * weekend_factor * holiday_boost * region_base * noise, 2)
            rows.append({
                "date": d, "region": region, "category": cat,
                "units_sold": units, "revenue": max(revenue, 0),
            })

df = pd.DataFrame(rows)
df.to_csv("/home/claude/kaggle-portfolio/02-data-visualization-retail-sales/data/retail_sales.csv", index=False)
print(df.shape)
print(df.head())
