# stockflow-backend-case-study
# StockFlow Backend Case Study – Bynry Internship

This repository contains my submission for the Backend Intern Case Study at Bynry Inc.

## 📦 Contents

### 🔹 Part 1: Code Review & Fixes
- [corrected_create_product.py](./part1_code_review/corrected_create_product.py): Refactored and validated API endpoint for creating a product and initializing inventory.

### 🔹 Part 2: Database Design
- [schema.sql](./part2_database_design/schema.sql): SQL schema for the inventory management system.
- [design_notes.md](./part2_database_design/design_notes.md): Justification of schema design and list of questions for the product team.

### 🔹 Part 3: Low Stock Alert API
- [low_stock_alert.py](./part3_low_stock_alert_api/low_stock_alert.py): Flask endpoint to fetch low-stock alerts with supplier info and projected stockout.
- [assumptions_and_logic.md](./part3_low_stock_alert_api/assumptions_and_logic.md): Explanation of logic, assumptions made, and edge cases handled.

## 🧠 Assumptions
- Thresholds are product-specific.
- Recent sales are tracked in `inventory_changes`.
- "Recent" is defined as activity in the last 30 days.
- Products have at least one supplier.

## 🚀 Tech Stack
- Python 3.x
- Flask
- SQLAlchemy ORM
- PostgreSQL (or SQLite for local testing)

## ✅ Submission
Submitted on: `August 1, 2025`  
GitHub Repo: [https://github.com/YOUR_USERNAME/stockflow-backend-case-study](https://github.com/YOUR_USERNAME/stockflow-backend-case-study)

---
