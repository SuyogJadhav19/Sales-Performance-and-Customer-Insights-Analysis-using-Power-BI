# Sales-Performance-and-Customer-Insights-Analysis-using-Power-BI
# Sales Performance and Customer Insights Analysis using Power BI

## 📌 Project Overview
This project focuses on analyzing sales data using Business Intelligence techniques and Power BI dashboards.

The objective of this project is to analyze sales performance, customer behavior, profitability, and regional distribution using interactive visualizations and business intelligence tools.

The project uses:
- Power BI for dashboard creation
- Python for dataset generation and analysis
- Pandas for data processing
- Matplotlib for visualization

---

# 🚀 Features
- Interactive Power BI dashboards
- KPI analysis (Sales, Profit, Orders)
- Sales trend analysis
- Customer segmentation
- Regional performance analysis
- Product profitability insights
- Data filtering using slicers

---

# 🛠 Technologies Used

## Business Intelligence Tool
- Power BI

## Programming Language
- Python 3.x

## Python Libraries
- Pandas
- NumPy
- Matplotlib
- Faker

---

# 📂 Project Structure

```txt
BI_Project/
│
├── sales_analysis.py
├── dashboard_metrics.py
├── generate_sales_dataset.py
├── sales_dataset.csv
├── powerbi_measures.txt
├── requirements.txt
```

---

# 📊 Dataset Information

The dataset contains sales and customer-related business information.

## Dataset Attributes
- Order ID
- Order Date
- Customer Name
- Segment
- Region
- State
- City
- Category
- Sub-Category
- Product Name
- Sales
- Profit
- Quantity
- Payment Mode

---

# 📈 Key Business Intelligence Tasks

## Trend Analysis
Analyze sales growth over time.

## Classification
Identify profitable and non-profitable products.

## Customer Segmentation
Group customers into:
- Consumer
- Corporate
- Home Office

## Regional Analysis
Analyze performance across different regions.

---

# ⚙ Installation and Setup

## Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Project

## Step 1: Generate Dataset

```bash
python generate_sales_dataset.py
```

---

## Step 2: Run Sales Analysis

```bash
python sales_analysis.py
```

---

## Step 3: Run KPI Dashboard Metrics

```bash
python dashboard_metrics.py
```

---

# 📊 Power BI Dashboard Components

## KPI Cards
- Total Sales
- Total Profit
- Total Orders
- Profit Ratio

## Charts and Visualizations
- Sales Trend (Line Chart)
- Sales by Category (Bar Chart)
- Profit by Sub-Category (Bar Chart)
- Customer Segment Contribution (Pie Chart)
- Regional Sales Distribution (Bar Chart)
- Profit vs Sales (Scatter Plot)

---

# 📌 DAX Measures Used

```DAX
Total Sales = SUM(Sales[Sales])

Total Profit = SUM(Sales[Profit])

Total Orders = DISTINCTCOUNT(Sales[Order ID])

Profit Ratio =
DIVIDE(
    SUM(Sales[Profit]),
    SUM(Sales[Sales]),
    0
)
```

---

# 📈 Insights Generated
- Office Supplies category generates the highest sales
- Consumer segment contributes maximum revenue
- West region has the best sales performance
- Some products generate high sales but low profit
- Regional profitability varies significantly

---

# 🧪 Data Processing Steps

## Data Extraction
- Imported CSV dataset into Power BI

## Data Cleaning
- Removed unnecessary columns
- Fixed data types

## Data Transformation
- Created DAX measures
- Aggregated business metrics

## Data Visualization
- Built interactive dashboards

## Data Filtering
Added slicers for:
- Region
- Category
- Segment

---

# 🔮 Future Enhancements
- Real-time data integration
- Machine Learning analytics
- Cloud deployment
- Mobile BI dashboards
- Predictive sales forecasting

---

# 📌 Conclusion

This project demonstrates how Business Intelligence tools can transform raw sales data into meaningful business insights.

Using Power BI and Python, the project provides:
- Interactive dashboards
- Profitability analysis
- Customer insights
- Regional performance analysis

The system helps organizations make data-driven business decisions effectively.

---

# 📚 References
- https://learn.microsoft.com/power-bi
- https://www.kaggle.com
- https://pandas.pydata.org
- https://matplotlib.org
