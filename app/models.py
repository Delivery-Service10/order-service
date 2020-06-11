from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

db = SQLAlchemy()


def init_app(app):
    db.app = app
    db.init_app(app)
    return db


def create_tables(app):
    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    if not database_exists(engine.url):
        create_database(engine.url)
        db.metadata.create_all(engine)
        db.session.commit()
    return engine


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True, nullable=False)
    customer_id = db.Column(db.String(50), nullable=False)
    store_id = db.Column(db.String(50), nullable=False)
    driver_id = db.Column(db.String(50), nullable=True)
    date = db.Column(db.DateTime, nullable=False)
    amount = db.Column(db.Numeric(10, 2), nullable=True)
    payment_method = db.Column(db.String(20), nullable=False)
    payment_confirmation_id = db.Column(db.String(50), nullable=False)
    order_items = db.relationship('OrderItem', backref='order_obj')


class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), nullable=False)
    product_id = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))





