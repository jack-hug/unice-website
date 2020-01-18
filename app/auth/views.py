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

@auth.route('/index')
@login_required
def index():
    return render_template('auth/index.html')