from flask import render_template,redirect,url_for,flash,request
from . import auth
from flask_login import login_required,logout_user,login_user
from ..models import User
from .forms import LoginForm


#登录路由
@auth.route('/login',methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data.lower()).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('auth.index')
            return redirect(next)
        flash('无效的用户名或密码')
    return render_template('auth/login.html',form = form)

#登出路由
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('你已经退出登录...')
    return redirect(url_for('main.index'))

# 后台主页
@auth.route('/index')
@login_required
def index():
    return render_template('auth/index.html')

# 分类管理
@auth.route('/product_category')
@login_required
def product_category():
    return render_template('auth/product-category.html')

# 产品管理
@auth.route('/product_list')
@login_required
def product_list():
    return render_template('auth/product-list.html')

# 添加分类
@auth.route('/product_category_add')
@login_required
def product_category_add():
    return render_template('auth/product-category-add.html')