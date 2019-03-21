from flask import render_template, flash, redirect, url_for, request
from app import app, bcrypt, db
from flask_login import login_user, login_required, current_user, logout_user
from forms import RegisterForm, LoginForm, PasswordResetRequestForm, ResetPasswordForm
from models import User




@app.route('/')
@login_required
def index():
    return render_template('index.html')



@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if current_user.is_authenticated: ## 鉴别用户是不是登入状态
        return redirect(url_for('index'))
    
    if form.validate_on_submit():
        ## 提取表单中填的数据
        username = form.username.data
        email = form.email.data
        password = bcrypt.generate_password_hash(form.password.data) ##对密码进行hash加密

        
        user = User(username=username, email=email, password=password) ##数据加入到数据库
        db.session.add(user)
        db.session.commit()
        
        flash('You were successful registeration!')
        return redirect(url_for('index'))


    return render_template('register.html', form = form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated: ## 鉴别用户是不是登入状态
        return redirect(url_for('index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        remember = form.remember.data
        
        # check password by hash 
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user, remember=remember)
            flash('login success')
            if request.args.get('next'):
                next_page = request.args.get('next')
                return redirect(next_page)
            return redirect(url_for('index'))
        flash('your password or User is wrong!!!!')
    return render_template('login.html', form = form)


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    
    logout_user()
    return redirect(url_for('login'))


@app.route('/reset', methods=['GET', 'POST'])
def reset():
    if current_user.is_authenticated: ## 鉴别用户是不是登入状态
        return redirect(url_for('index'))
    form = PasswordResetRequestForm()
    if form.validate_on_submit():
        email = form.email.data
        user =  User.query.filter_by(email=email).first()
        token = user.generate_password_token()
        send_reset_password_mail(user, token)
        flash('email has send')
    return render_template('reset.html', form = form)



@app.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    if current_user.is_authenticated: ## 鉴别用户是不是登入状态
        return redirect(url_for('index'))
    form = ResetPasswordForm()
    return render_template('reset_password.html', form = form)

    