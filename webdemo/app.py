from flask import Flask, render_template, flash
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from config import Config
from forms import RegisterForm
from models import User


app = Flask(__name__)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
app.config.from_object(Config)
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        ## 提取表单中填的数据
        username = form.username.data
        email = form.email.data
        password = bcrypt.generate_password_hash(form.password.data) ##对密码进行hash加密

        user = User(username, email, password) ##数据加入到数据库
        db.session.add(user)
        db.session.commit()
        flash('successful registeration!', category='success')




    return render_template('register.html', form = form)

if __name__ == "__main__":
    app.run( debug=True )