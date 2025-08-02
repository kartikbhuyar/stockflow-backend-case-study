# stockflow-backend-case-study
# StockFlow Backend Case Study – Bynry Internship

This repository contains my submission for the Backend Intern Case Study at Bynry Inc.

##  Contents




###  Part 1: Code Review & Fixes
- [create_product.py](./part1_code_review/corrected_create_product.py): Refactored and validated API endpoint for creating a product and initializing inventory.
- Type	Issue Description
 Technical	;- No validation for required fields (sku, price, etc.)
 Technical	;- sku uniqueness not enforced before inserting
 Technical	;- No exception handling — code crashes on bad input
 Technical	;- price may be stored as float, but not validated or converted
 Business ;- Logic	Product is tightly coupled to a single warehouse_id, but a product can exist in multiple warehouses
 Business ;- Logic	Adding product and inventory should be atomic (transaction-safe)
 Business ;- Logic	No check if the referenced warehouse_id exists
 Business ;- Logic	initial_quantity is not validated (could be negative or missing)

what we updated/fixed??
 Products were wrongly tied to one warehouse

 No validation for inputs or foreign keys

 SKU uniqueness not enforced

 Fix: Added input validation, uniqueness check, transactional safety

 Fix: Separated Product and Inventory 





###  Part 2: Database Design
- [schema.sql](./part2_database_design/schema.sql): SQL schema for the inventory management system.
- [design_notes.md](./part2_database_design/design_notes.md): Justification of schema design and list of questions for the product team.

what we fixed??

-Companies can have multiple warehouses

-Products can be stored in multiple warehouses with different quantities

-Inventory levels must be tracked historically

-Suppliers provide products to companies

-Some products are bundles that include other products



###  Part 3: Low Stock Alert API
- [low_stock_alert.py](./part3_low_stock_alert_api/low_stock_alert.py): Flask endpoint to fetch low-stock alerts with supplier info and projected stockout.
- [assumptions_and_logic.md](./part3_low_stock_alert_api/assumptions_and_logic.md): Explanation of logic, assumptions made, and edge cases handled.

what we fixed??
-Each product has a low-stock threshold (e.g., products.low_stock_threshold)

-Only alert for products that had recent sales activity (e.g., in the last 30 days)

-Products can be stored in multiple warehouses

-Response must include supplier info for reordering



##  Assumptions
- Thresholds are product-specific.
- Recent sales are tracked in `inventory_changes`.
- "Recent" is defined as activity in the last 30 days.
- Products have at least one supplier.


