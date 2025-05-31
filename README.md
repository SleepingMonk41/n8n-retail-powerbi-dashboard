# n8n +  Power BI Automated Retail Sales Data Dashboard

This project demonstrates an end-to-end **automated retail analytics dashboard** using only free and self-hostable tools. This project fetches product and cart data from a public demo API, transforms it using Python in n8n, and visualizes it in Power BI. The dashboard auto-refreshes at scheduled intervals using AutoHotKey and Windows Task Scheduler.

---

## 🔧 Tools Used

- **n8n (via Docker)** – for data fetching, transformation, and automation
- **Python** – for JSON flattening and CSV generation
- **Power BI Desktop** – for data visualization
- **AutoHotKey + Windows Task Scheduler** – for automated dashboard refresh

---

## 📊 Project Workflow

1. **Data Extraction**  
   Fetches product, cart, and user data from `dummyjson.com` using n8n HTTP request nodes.

2. **Transformation**  
   Python code node flattens nested JSON, handles missing values, and converts it into CSV format using in-memory buffers.

3. **File Output**  
   CSV files are saved locally using Docker-mounted volumes.

4. **Power BI Reporting**  
   The CSVs are imported into Power BI and transformed using Power Query. Dashboard visuals include:
   - Top products
   - Revenue metrics
   - Cart insights
   - Category performance

5. **Automation**  
   - AutoHotKey script refreshes the `.pbix` file
   - Scheduled with Windows Task Scheduler
   - Fully hands-free data update pipeline

---

## 💡 Highlights

- **End-to-end solution using publicly accessible and modifiable tools**
- Dynamic schema generation in Python
- No temporary file handling—everything is in-memory
- Auto-refresh setup with AHK scripting
- Easy to extend or adapt for other data sources

---

## 📁 Folder Structure

📁 scripts/           # Python code used in n8n Code nodes
📁 n8n_workflows/     # JSON export of your n8n workflow
📁 sample_data/       # Output CSVs (products.csv, carts.csv, users.csv)
📁 automation/        # AutoHotKey script
📁 powerbi/           # Power BI .pbix dashboard file and screenshots of dashboard

---

## 📌 Author

Made  by Varghese Jose  
📧 Contact:[LinkedIn](https://www.linkedin.com/in/varghese-jose41)

---

> Feel free to reuse, or build upon this project for your own analytics pipelines!
