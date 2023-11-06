from flask import Flask, render_template, url_for, redirect, request 
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError

app=Flask(__name__)

app.config['SECRET_KEY'] = 'thisisasecretkey'

data=[]


class RegisterForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Register')



class LoginForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Login')


@app.route('/')
def home():
    return render_template('Intermediate_flask-3_home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username=request.form.get("username")
        password=request.form.get("password")
        if (username in data) and (password in data):
            return redirect(url_for('dashboard'))
        else:
            return "You entered details are wrong."
    return render_template('Intermediate_flask-3_login.html', form=form)


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template('Intermediate_flask-3_dash.html')


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('login'))


@ app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        username=request.form.get("username")
        password=request.form.get("password")
        if username in data:
            return "Your name already exists."
        else:
            data.append(username)
            data.append(password)
            return redirect(url_for('login'))

    return render_template('Intermediate_flask-3_register.html', form=form)


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8000)