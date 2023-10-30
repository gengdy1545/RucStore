from datetime import datetime
from store import db, login_manage
from flask_login import UserMixin


@login_manage.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model,UserMixin):
    __tablename__="User"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=False, nullable=False,default="私密")
    email = db.Column(db.String(120), unique=True, nullable=False)
    table_name = db.Column(db.String(20), unique=False, nullable=False)
    table_id = db.Column(db.Integer,nullable=False)


class Customer(db.Model,UserMixin):
    __tablename__ = "Customer"
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),unique=False,nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    password = db.Column(db.String(60),nullable=False)
    consignee = db.Column(db.String(20),nullable=False,default="null")
    address = db.Column(db.String(40),nullable=False,default="null")
    telephone = db.Column(db.String(20),nullable=False,default="null")
    orders = db.relationship("Order",backref="customer",lazy=True)


class Supplier(db.Model,UserMixin):
    __tablename__ = "Supplier"
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),unique=False,nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    password = db.Column(db.String(60),nullable=False)
    shipper = db.Column(db.String(40),nullable=False,default="null")
    address = db.Column(db.String(40),nullable=False,default="null")
    telephone = db.Column(db.String(20),nullable=False,default="null")
    products = db.relationship("Product",backref="supplier",lazy=True)


class Product(db.Model):
    __tablename__="Product"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40),nullable=False,default="null")
    price = db.Column(db.Float,nullable=False,default=0.00)
    count = db.Column(db.Integer, nullable=False, default=0)
    Supplier_id = db.Column(db.Integer,db.ForeignKey("Supplier.id"),nullable=False)
    order_detail = db.relationship("OrderDetail",backref="product",uselist=False,lazy=True)


class OrderDetail(db.Model):
    __tablename__="OrderDetail"
    id = db.Column(db.Integer,primary_key=True)
    count = db.Column(db.Integer, nullable=False)
    order_id = db.Column(db.Integer,db.ForeignKey("Order.id"),nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("Product.id"),nullable=False)


class Order(db.Model):
    __tablename__ = "Order"
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Integer, nullable=False, default=0)
    start_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    end_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    total_price =db.Column(db.Float,nullable=False, default=0.00)
    customer_id = db.Column("customer_id", db.Integer,db.ForeignKey("Customer.id"),nullable=False)
    orderdetails = db.relationship("OrderDetail",backref="order",lazy=True)
