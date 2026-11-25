# Retail Sales Analysis — Data Visualization

A standalone capstone project applying Kaggle's **Data Visualization** course to two years
of daily multi-region, multi-category retail sales data.

## The business questions

- When do we sell the most, and is there a holiday effect?
- Which region/category combination drives the most revenue — and which underperforms?
- Does selling more units reliably mean more revenue, or does product mix matter?
- Do weekends really outsell weekdays, as the business assumes?

## What this project does

`notebooks/retail_sales_visualization.ipynb` answers each question with the chart type
best suited to it:

| Chart | Question answered |
|---|---|
| Line chart (weekly revenue) | Overall trend + holiday spike |
| Grouped bar chart | Revenue by region x category |
| Heatmap | Seasonality (month x category) |
| KDE / distribution plot | Spread of daily revenue by region |
| Scatter plot | Units sold vs. revenue relationship |
| Box plot | Weekday vs. weekend effect |

All charts are saved as PNGs in `images/` as well as rendered inline in the notebook.

## Repo structure

```
.
├── data/
│   ├── generate_data.py
│   └── retail_sales.csv
├── images/                 # exported PNG charts
├── notebooks/
│   └── retail_sales_visualization.ipynb
├── requirements.txt
└── README.md
```

## Run it yourself

```bash
pip install -r requirements.txt
python data/generate_data.py          # regenerate the dataset (optional, already included)
jupyter notebook notebooks/retail_sales_visualization.ipynb
```

## Why synthetic data?

`data/generate_data.py` builds a realistic 2-year daily sales dataset with genuine
seasonality, a weekend effect, and a December holiday spike baked in — so the patterns
the charts reveal are real signal, not noise, and the whole project runs offline.
