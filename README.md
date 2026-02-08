# 🚍 Urban Transit Analysis: Chicago vs. Philadelphia (2019-2025)

## 📌 Project Overview
**The Challenge:** Public transit systems worldwide faced an unprecedented collapse in ridership due to the 2020 pandemic. This project analyzes **5+ years of data** from Chicago (CTA) and Philadelphia (SEPTA) to quantify the recovery, identify mode-shift trends, and provide operational recommendations.

**The Solution:** I built a dynamic **Power BI Dashboard** using a **Galaxy Schema** architecture to integrate Daily data (Chicago) with Monthly data (SEPTA), enabling side-by-side comparison despite different granularities.

## 🔑 Key Insights & Findings
1.  **The "Bus Resilience" Phenomenon:** Bus ridership has recovered significantly faster than Rail in both cities. In Chicago, bus volume is currently at **[X]%** of pre-pandemic levels, suggesting a reliance on essential local travel over downtown commuting.
2.  **The "Hybrid Work" Impact:** Weekday ridership (M-F) remains suppressed compared to weekends, confirming that hybrid work models have permanently altered commuter patterns.
3.  **Chicago's Backbone:** The **#79 (79th)** and **Red Line** routes remain the highest volume corridors, carrying over [X]% of the city's total traffic.

## 🛠️ Technical Stack
* **Tool:** Power BI Desktop
* **Data Modeling:** Galaxy Schema (Star Schema variation with multiple Fact tables).
* **ETL:** Power Query (M Language) for cleaning, unpivoting, and standardizing date formats.
* **Analysis:** DAX (Data Analysis Expressions) for Time Intelligence and YoY Growth calculations.

## 📊 Dashboard Structure
### Page 1: Executive Overview
* **Comparison:** Side-by-side KPI cards for Total Ridership and YoY Growth.
* **Trend Analysis:** Dual-axis line charts standardizing daily vs. monthly granularities.
* **Mode Split:** Automated breakdown of Bus vs. Rail performance.

<img width="1311" height="727" alt="Screenshot 2026-02-08 181745" src="https://github.com/user-attachments/assets/c1ee70e4-1d9a-490b-945c-86a246d2bb4f" />


### Page 2: Chicago Deep Dive
* **Operational Metrics:** Day-type analysis (Weekday vs. Weekend).
* **Route Performance:** "Top 10 Routes" leaderboard using Top N filtering.
* **Seasonality:** Heatmap/Trend lines identifying peak travel months.

<img width="1307" height="730" alt="Screenshot 2026-02-08 181823" src="https://github.com/user-attachments/assets/7c8432eb-494d-4ed2-95b1-d256981a7723" />


## 🚀 How to Run This Project
1.  Clone this repository.
2.  Open `Transit_Analysis.pbix` in **Power BI Desktop**.
3.  The dataset is embedded; no external database connection is required.

