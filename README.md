# 16th-360-customer-analytics

Customer 360 Analytics Platform using Microsoft Fabric

Overview

This project demonstrates an end-to-end Customer 360 Analytics solution built using Microsoft Fabric.

The platform ingests customer, order, support ticket, and website activity data into a Fabric Lakehouse and transforms it through a Bronze-Silver-Gold architecture.

The final Gold layer provides a unified customer profile for analytics, reporting, customer segmentation, churn prediction, and executive dashboards.

---

Architecture

Customer Data Sources

↓

OneLake

↓

Bronze Layer

↓

Silver Layer

↓

Gold Layer

↓

Fabric Warehouse

↓

Power BI Dashboard

---

Technology Stack

- Microsoft Fabric
- OneLake
- Lakehouse
- PySpark
- SQL
- Fabric Pipelines
- Power BI
- Python
- GitHub Actions
- Pytest

---

Project Structure

fabric-customer360-platform/

├── README.md

├── requirements.txt

├── data/

├── notebooks/

├── sql/

├── tests/

├── docs/

└── .github/

---

Data Sources

Customers

Customer master information.

Orders

Customer purchase transactions.

Support Tickets

Customer support interactions.

Web Activity

Website browsing activity.

---

Bronze Layer

Raw ingestion from source files.

No transformations applied.

---

Silver Layer

Data cleansing and standardization.

Features:

- Deduplication
- Null handling
- Data validation
- Type casting
- Standardized customer identifiers

---

Gold Layer

Unified Customer 360 dataset.

Includes:

- Customer Lifetime Value
- Total Orders
- Total Spend
- Support Tickets Raised
- Last Activity Date
- Customer Segment

---

Business KPIs

- Customer Lifetime Value
- Average Order Value
- Churn Risk Customers
- Most Active Customers
- Support Ticket Analysis
- Customer Segmentation
- Revenue Trends

---

Example Use Cases

- Customer Analytics
- Marketing Campaign Optimization
- Customer Retention Analysis
- Churn Detection
- Executive Reporting

---

How To Run

1. Load source CSV files into Fabric Lakehouse.
2. Execute Bronze ingestion notebook.
3. Execute Silver transformation notebook.
4. Execute Gold aggregation notebook.
5. Run SQL analytics queries.
6. Connect Power BI to Gold tables.

---

Future Enhancements

- Real-Time Streaming
- Machine Learning Customer Segmentation
- Recommendation Engine
- Fabric Data Activator Alerts
- Predictive Churn Modeling
