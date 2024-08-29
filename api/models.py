from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from config import db

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    cart = db.relationship('Cart', uselist=False, back_populates='user')
    orders = db.relationship('Order', back_populates='user')
    reviews = db.relationship('Review', back_populates='user')
    addresses = db.relationship('Address', back_populates='user')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_json(self):
        return {
            "id": self.id,
            "username": self.username,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat()
        }

# Admin Model
class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_json(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat()
        }

# Product Model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    discount_percentage = db.Column(db.Float)
    rating = db.Column(db.Float)
    stock = db.Column(db.Integer, nullable=False)
    brand = db.Column(db.String(50), nullable=False)
    sku = db.Column(db.String(20), unique=True, nullable=False)
    weight = db.Column(db.Float)
    width = db.Column(db.Float)
    height = db.Column(db.Float)
    depth = db.Column(db.Float)
    warranty_information = db.Column(db.String(100))
    shipping_information = db.Column(db.String(100))
    availability_status = db.Column(db.String(20))
    return_policy = db.Column(db.String(100))
    minimum_order_quantity = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    barcode = db.Column(db.String(50))
    qr_code = db.Column(db.String(200))
    thumbnail = db.Column(db.String(200))

    tags = db.relationship('Tag', secondary='product_tags', back_populates='products')
    images = db.relationship('Image', back_populates='product')
    reviews = db.relationship('Review', back_populates='product')
    cart_items = db.relationship('CartItem', back_populates='product')
    order_items = db.relationship('OrderItem', back_populates='product')

    def to_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "category": self.category,
            "price": self.price,
            "discount_percentage": self.discount_percentage,
            "rating": self.rating,
            "stock": self.stock,
            "brand": self.brand,
            "sku": self.sku,
            "weight": self.weight,
            "dimensions": {
                "width": self.width,
                "height": self.height,
                "depth": self.depth
            },
            "warranty_information": self.warranty_information,
            "shipping_information": self.shipping_information,
            "availability_status": self.availability_status,
            "return_policy": self.return_policy,
            "minimum_order_quantity": self.minimum_order_quantity,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "barcode": self.barcode,
            "qr_code": self.qr_code,
            "thumbnail": self.thumbnail,
            "tags": [tag.to_json() for tag in self.tags],
            "images": [image.to_json() for image in self.images],
            "reviews": [review.to_json() for review in self.reviews]
        }

# Tag Model
class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    products = db.relationship('Product', secondary='product_tags', back_populates='tags')

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name
        }

# Association Table for Product-Tag Many-to-Many Relationship
product_tags = db.Table('product_tags',
                        db.Column('product_id', db.Integer, db.ForeignKey('product.id'), primary_key=True),
                        db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True)
                        )

# Image Model
class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(200), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)

    product = db.relationship('Product', back_populates='images')

    def to_json(self):
        return {
            "id": self.id,
            "url": self.url,
            "product_id": self.product_id
        }

# Review Model
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    product = db.relationship('Product', back_populates='reviews')
    user = db.relationship('User', back_populates='reviews')

    def to_json(self):
        return {
            "id": self.id,
            "rating": self.rating,
            "comment": self.comment,
            "date": self.date.isoformat(),
            "product_id": self.product_id,
            "user_id": self.user_id
        }

# Cart Model
class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = db.relationship('User', back_populates='cart')
    items = db.relationship('CartItem', back_populates='cart', cascade='all, delete-orphan')

    def to_json(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "items": [item.to_json() for item in self.items]
        }

# CartItem Model
class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    cart = db.relationship('Cart', back_populates='items')
    product = db.relationship('Product', back_populates='cart_items')

    def to_json(self):
        return {
            "id": self.id,
            "cart_id": self.cart_id,
            "product_id": self.product_id,
            "quantity": self.quantity,
            "product": self.product.to_json()
        }

# Order Model
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    shipping_address_id = db.Column(db.Integer, db.ForeignKey('address.id'), nullable=True)

    user = db.relationship('User', back_populates='orders')
    items = db.relationship('OrderItem', back_populates='order', cascade="all, delete-orphan")
    shipping_address = db.relationship('Address', back_populates='orders')

    def to_json(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "status": self.status,
            "total_amount": self.total_amount,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "items": [item.to_json() for item in self.items],
            "shipping_address": self.shipping_address.to_json() if self.shipping_address else None
        }

# OrderItem Model
class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

    order = db.relationship('Order', back_populates='items')
    product = db.relationship('Product', back_populates='order_items')

    def to_json(self):
        return {
            "id": self.id,
            "order_id": self.order_id,
            "product_id": self.product_id,
            "quantity": self.quantity,
            "price": self.price,
            "product": self.product.to_json()
        }

# Address Model
class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    street = db.Column(db.String(200), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    postal_code = db.Column(db.String(20), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    is_default = db.Column(db.Boolean, default=False)

    user = db.relationship('User', back_populates='addresses')
    orders = db.relationship('Order', back_populates='shipping_address')

    def to_json(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "street": self.street,
            "city": self.city,
            "state": self.state,
            "postal_code": self.postal_code,
            "country": self.country,
            "is_default": self.is_default
        }
