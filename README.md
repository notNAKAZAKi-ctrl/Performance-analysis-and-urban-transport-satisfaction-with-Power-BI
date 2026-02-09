# 🚍 Urban Transit Analysis: Chicago vs. Philadelphia (2019-2025)

## 📌 Project Overview
**The Challenge:** Public transit systems worldwide faced an unprecedented collapse in ridership due to the 2020 pandemic. This project analyzes **5+ years of data** from Chicago (CTA) and Philadelphia (SEPTA) to quantify the recovery, identify mode-shift trends, and provide operational recommendations.

**The Solution:** I built a dynamic **Power BI Dashboard** using a **Star Schema** architecture to integrate Daily data (Chicago) with Monthly data (SEPTA), enabling side-by-side comparison despite different granularities.

## 🔑 Key Insights & Findings
1.  **The "Bus Resilience" Phenomenon:** Bus ridership has recovered significantly faster than Rail in both cities. In Chicago, bus volume is currently at **[X]%** of pre-pandemic levels, suggesting a reliance on essential local travel over downtown commuting.
2.  **The "Hybrid Work" Impact:** Weekday ridership (M-F) remains suppressed compared to weekends, confirming that hybrid work models have permanently altered commuter patterns.
3.  **Chicago's Backbone:** The **#79 (79th)** and **Red Line** routes remain the highest volume corridors, carrying over [X]% of the city's total traffic.

## 🛠️ Technical Stack
* **Tool:** Power BI Desktop
* **Data Modeling:** Star Schema
* **ETL:** Power Query (M Language) for cleaning, unpivoting, and standardizing date formats.
* **Analysis:** DAX (Data Analysis Expressions) for Time Intelligence and YoY Growth calculations.

## 📊 Dashboard Structure
### Page 1: Executive Overview
* **Comparison:** Side-by-side KPI cards for Total Ridership and YoY Growth.
* **Trend Analysis:** Dual-axis line charts standardizing daily vs. monthly granularities.
* **Mode Split:** Automated breakdown of Bus vs. Rail performance.

<img width="1282" height="722" alt="Screenshot 2026-02-09 103651" src="https://github.com/user-attachments/assets/77485445-a1c3-4ae5-b1b7-725e83ecba60" />


### Page 2: Chicago Deep Dive
* **Operational Metrics:** Day-type analysis (Weekday vs. Weekend).
* **Route Performance:** "Top 10 Routes" leaderboard using Top N filtering.
* **Seasonality:** Heatmap/Trend lines identifying peak travel months.

<img width="1286" height="717" alt="Screenshot 2026-02-09 103713" src="https://github.com/user-attachments/assets/c2e46eb2-4c02-4680-bdcf-bbf52ed4a5af" />


## 🚀 How to Run This Project
1.  Clone this repository.
2.  Open `Transit_Analysis.pbix` in **Power BI Desktop**.
3.  The dataset is embedded; no external database connection is required.

## 📅 Project Management
This project was managed using **Jira** to simulate a real-world Agile workflow. I utilized a Kanban board to track data engineering tasks, measure progress, and manage the backlog of user stories.

* **Methodology:** Agile / Kanban
* **Tracking:** Jira Software
* **Key Epics:** Data Cleaning (ETL), Data Modeling (Galaxy Schema), Dashboard Design.

[**🔗 View the Jira Project Board**] (https://mohamefamine2006.atlassian.net/?continue=https%3A%2F%2Fmohamefamine2006.atlassian.net%2Fwelcome%2Fsoftware%3FprojectId%3D10000&atlOrigin=eyJpIjoiZDYzMmI0MjNlNjZhNDM2NzkwNzFlMzQyMTIyZDdhMWYiLCJwIjoiamlyYS1zb2Z0d2FyZSJ9)

![Jira Board Preview]<img width="1647" height="822" alt="image" src="https://github.com/user-attachments/assets/912b253c-ca1f-42cb-b212-45b5a32ca36f" />





