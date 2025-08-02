from flask import Flask
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from models import db
from routes.create_product import create_product_route
from routes.low_stock_alert import low_stock_alert_route

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS

db.init_app(app)

# Register routes
app.register_blueprint(create_product_route)
app.register_blueprint(low_stock_alert_route)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
