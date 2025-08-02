from flask import Blueprint, request, jsonify
from models import db, Product, Inventory, Warehouse

create_product_route = Blueprint('create_product', __name__)

@create_product_route.route('/api/products', methods=['POST'])
def create_product():
    data = request.json

    # Validate input
    required_fields = ['name', 'sku', 'price', 'warehouse_id', 'initial_quantity']
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400

    # SKU uniqueness check
    if Product.query.filter_by(sku=data['sku']).first():
        return jsonify({"error": "SKU already exists"}), 409

    # Check warehouse exists
    warehouse = Warehouse.query.get(data['warehouse_id'])
    if not warehouse:
        return jsonify({"error": "Invalid warehouse ID"}), 404

    try:
        # Create product
        product = Product(
            name=data['name'],
            sku=data['sku'],
            price=float(data['price']),
            low_stock_threshold=10  # default or fetched from category
        )
        db.session.add(product)
        db.session.flush()  # get product.id

        # Create inventory
        inventory = Inventory(
            product_id=product.id,
            warehouse_id=data['warehouse_id'],
            quantity=int(data['initial_quantity'])
        )
        db.session.add(inventory)
        db.session.commit()

        return jsonify({"message": "Product created", "product_id": product.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
