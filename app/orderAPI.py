from flask import Blueprint, request, jsonify
from models import db, Order, OrderItem
from json import dumps
import uuid
import datetime
import simplejson as json
# import helper_functions

order_api = Blueprint('order_api', __name__)


@order_api.route("/order/", methods=['POST', 'PUT'])
def add_order_item():
    data = request.get_json()
    products = data['products']
    total_price = 0
    new_order_public_id = str(uuid.uuid4())
    new_order = Order(
        public_id=new_order_public_id,
        customer_id=data['customer_id'],
        store_id=data['store_id'],
        date=datetime.datetime.utcnow(),
        payment_method=data['payment_method'],
        payment_confirmation_id=data['payment_confirmation_id']
    )
    print(new_order)
    db.session.add(new_order)
    db.session.commit()

    for product in products:
        new_product = OrderItem(
            public_id=str(uuid.uuid4()),
            product_id=product['product_id'],
            quantity=product['quantity'],
            price=product['price'],
            order_obj=new_order
        )
        total_price = total_price + (product['quantity']*product['price'])
        db.session.add(new_product)
        db.session.commit()

        new_order = Order.query.filter_by(public_id=new_order_public_id).first()
        new_order.amount = total_price
        db.session.commit()

    return jsonify({'message': 'order created'})
