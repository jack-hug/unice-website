from . import db,login_manager
from flask import current_app
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


# 定义模型
class Information(db.Model):
    __tablename__ = 'information'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), unique=True)
    banner = db.Column(db.Text())
    inf_img = db.Column(db.Text())
    content = db.Column(db.String(64))
    add_time = db.Column(db.DateTime(),default = datetime.utcnow)

    def __repr__(self):
        return '<Role %r>' % self.title

# 产品大分类
class Product_category(db.Model):
    __tablename__ = 'product_category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    is_enable = db.Column(db.Integer)
    add_time = db.Column(db.DateTime(),default = datetime.utcnow)
    product_class = db.relationship('Product_class',backref = 'pro_category')
    
    def __repr__(self):
        return '<Role %r>' % self.name

# 产品小分类
class Product_class(db.Model):
    __tablename__ = 'product_class'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    is_enable = db.Column(db.Integer)
    add_time = db.Column(db.DateTime(),default = datetime.utcnow)
    product = db.relationship('Product',backref = 'pro_class')
    product_category = db.Column(db.Integer,db.ForeignKey('product_category.id'))

    def __repr__(self):
        return '<Role %r>' % self.name

class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    url = db.Column(db.String(64))  # 原图url
    url_s = db.Column(db.String(64))  # 展示图url
    code = db.Column(db.Text())
    product_class_id = db.Column(db.Integer,db.ForeignKey('product_class.id'))
    product_img = db.Column(db.Text())
    is_enable = db.Column(db.Integer)
    add_time = db.Column(db.DateTime(),default = datetime.utcnow)


    def __repr__(self):
        return '<Role %r>' % self.name

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    # flask-security记录登录信息
    last_login_at = db.Column(db.DateTime) #记录上次登录时间
    current_login_at = db.Column(db.DateTime) #记录本次登录时间
    last_login_ip = db.Column(db.String(100)) #记录上次登录IP
    current_login_ip = db.Column(db.String(100)) #记录本次登录IP
    login_count = db.Column(db.Integer) #记录登录次数

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Role %r>' % self.username

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
