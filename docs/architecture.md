# Customer 360 Architecture

Source Systems

Customers CSV
Orders CSV
Support Tickets CSV
Web Activity CSV

↓

Microsoft Fabric OneLake

↓

Bronze Layer

bronze_customers
bronze_orders
bronze_support_tickets
bronze_web_activity

↓

Silver Layer

silver_customers
silver_orders
silver_support_tickets
silver_web_activity

↓

Gold Layer

gold_customer360

↓

Fabric Warehouse

↓

Power BI Dashboard