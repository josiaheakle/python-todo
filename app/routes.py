from flask import render_template, url_for, flash, redirect
from flask_login import current_user, login_user, logout_user

from app import app, forms, models, db

def check_user_logged_in():
    if (current_user.is_authenticated):
        return redirect(url_for('index'))

@app.route("/")
@app.route("/index")
def index():
    items = [
        {"name" : "Item 1"},
        {"name" : "Item 2"},
    ]
    return render_template("pages/index.html",  title="HELLO", items=items)


@app.route("/login", methods=["GET","POST"])
def login():
    check_user_logged_in()
    form = forms.LoginForm()
    if (form.validate_on_submit()):
        user = models.User.query.filter_by(username=form.username.data).first()
        if (user is None or not user.check_password(form.password.data)):
            flash('Invalid username or password.')
            return redirect(url_for('login'))
        login_user(user, remember=form.rememberMe.data)
        return redirect(url_for("index"))
    return render_template("pages/login.html", form=form)

@app.route("/register", methods=["GET", "POST"])
def register():
    check_user_logged_in()
    form = forms.RegisterForm()
    if (form.validate_on_submit()):
        isUsernameTaken = models.User.query.filter_by(username=form.username.data).first()
        isEmailTaken = models.User.query.filter_by(email=form.email.data).first()
        if (not(isUsernameTaken or isEmailTaken)):
            user = models.User(username=form.username.data, email=form.email.data, firstName=form.firstName.data, lastName=form.lastName.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            login_user(user, remember=form.rememberMe.data)
            redirect("index")
        else:
            if (isEmailTaken):
                form.email.errors.append("Email already in use!")
            if (isUsernameTaken):
                form.username.errors.append("Username already in use!")
    return render_template("pages/register.html", form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))