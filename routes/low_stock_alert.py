from flask import Blueprint, jsonify
from datetime import datetime, timedelta
from sqlalchemy import func
from models import db, Inventory, Product, Warehouse, Supplier, InventoryChange, ProductSupplier

low_stock_alert_route = Blueprint('low_stock_alert', __name__)

@low_stock_alert_route.route('/api/companies/<int:company_id>/alerts/low-stock', methods=['GET'])
def low_stock_alerts(company_id):
    alerts = []
    today = datetime.utcnow()
    recent_days = 30
    since = today - timedelta(days=recent_days)

    inventories = db.session.query(
        Inventory, Product, Warehouse, Supplier
    ).join(Product, Product.id == Inventory.product_id
    ).join(Warehouse, Warehouse.id == Inventory.warehouse_id
    ).join(ProductSupplier, ProductSupplier.product_id == Product.id
    ).join(Supplier, Supplier.id == ProductSupplier.supplier_id
    ).filter(
        Warehouse.company_id == company_id,
        Inventory.quantity < Product.low_stock_threshold
    ).all()

    for inv, prod, wh, supp in inventories:
        sales = db.session.query(func.sum(InventoryChange.change_quantity)).filter(
            InventoryChange.inventory_id == inv.id,
            InventoryChange.change_type == 'sale',
            InventoryChange.timestamp >= since
        ).scalar() or 0

        avg_daily_sales = sales / recent_days if sales > 0 else 0
        days_until_stockout = int(inv.quantity / avg_daily_sales) if avg_daily_sales > 0 else -1

        alerts.append({
            "product_id": prod.id,
            "product_name": prod.name,
            "sku": prod.sku,
            "warehouse_id": wh.id,
            "warehouse_name": wh.name,
            "current_stock": inv.quantity,
            "threshold": prod.low_stock_threshold,
            "days_until_stockout": days_until_stockout,
            "supplier": {
                "id": supp.id,
                "name": supp.name,
                "contact_email": supp.contact_email
            }
        })

    return jsonify({
        "alerts": alerts,
        "total_alerts": len(alerts)
    })
