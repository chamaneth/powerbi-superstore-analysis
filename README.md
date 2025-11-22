# Global Superstore Dashboard

## Overview
This project is a **Power BI dashboard** built using the **Global Superstore dataset**. It demonstrates data cleaning, transformation, and visualization for **retail sales analysis**. The dashboard highlights **key metrics, trends, and top performers**, making it an **intern-ready portfolio project**.

---

## Dataset
- **Source:** [Kaggle — Global Superstore Dataset](https://www.kaggle.com/datasets/apoorvaappz/global-super-store-dataset)  
- **Format:** CSV (`Global_Superstore2.csv`)  

## Data Cleaning & Transformation
Performed in **Python (pandas)**:
- Removed duplicates  
- Fixed data types (dates, numeric columns)  
- Created `TotalSales = Quantity × Sales`  
- Saved cleaned dataset as `cleaned_superstore.csv`  

In **Power BI**:
- Added calculated columns:
  - `OrderYear`, `OrderMonth`, `OrderQuarter`, `MonthYear`  
  - `TotalSales` (if missing)  
- Created **DAX measures**:
  - `TotalSalesMeasure`, `TotalProfitMeasure`, `TotalQuantity`, `AvgDiscount`, `ProfitMargin`  

---

## Dashboard Features
| Visual | Description |
|--------|-------------|
| Sales Trend | Line chart showing sales over time |
| Profit by Category | Bar chart of total profit per category |
| Top 10 Customers | Column chart of top 10 customers by sales |
| Sales by Region | Map visualization of regional sales |
| Discount vs Sales | Scatter plot showing discount vs total sales |
| KPI Cards | Total Sales, Total Profit, Total Quantity, Average Discount |

---

## Interactivity
- **Slicers:** Year, Category, Region  
- **Filters:** Top N customers/products  
- **Drill-through:** Explore details per region or customer  

---


## Technologies Used
- **Python (pandas)** — Data cleaning & transformation  
- **Power BI** — Dashboard creation & visualization  
- **DAX** — Measures & advanced calculations  

---

## Project Outcome
- Fully interactive, **intern-ready dashboard**  
- Insights on **sales trends, top customers, category performance, and profit margins**  
- Useful for **retail decision-making and performance tracking**

---

## Screenshots
<img width="1359" height="683" alt="Screenshot 2025-11-22 232815" src="https://github.com/user-attachments/assets/212153e3-bec3-4222-bb1d-f752fc1c590c" />
<img width="1359" height="718" alt="Screenshot 2025-11-22 232644" src="https://github.com/user-attachments/assets/1baa6a91-1488-45dd-9a84-7638d233d7c6" />



## Hashtags / Tags
#PowerBI #DataAnalysis #RetailDashboard #Python #DAX #DataCleaning #Visualization 
