# Data Dictionary

## customers.csv

| Column | Description |
|----------|----------|
| customer_id | Unique customer identifier |
| customer_name | Customer full name |
| email | Customer email |
| city | Customer city |
| state | Customer state |
| country | Customer country |
| signup_date | Customer registration date |

---

## orders.csv

| Column | Description |
|----------|----------|
| order_id | Order identifier |
| customer_id | Customer identifier |
| order_date | Order date |
| product_name | Purchased product |
| category | Product category |
| quantity | Quantity purchased |
| unit_price | Product unit price |
| order_amount | Order value |

---

## support_tickets.csv

| Column | Description |
|----------|----------|
| ticket_id | Ticket identifier |
| customer_id | Customer identifier |
| category | Ticket category |
| priority | Ticket priority |
| status | Ticket status |

---

## web_activity.csv

| Column | Description |
|----------|----------|
| activity_id | Activity identifier |
| customer_id | Customer identifier |
| page_name | Website page |
| device_type | Device used |
| session_duration_seconds | Session duration |