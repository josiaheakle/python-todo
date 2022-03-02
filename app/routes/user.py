from flask import render_template, url_for, flash, redirect, request
from flask_login import current_user, login_user, logout_user
from werkzeug.urls import url_parse

from app import app, forms, models, db

def _check_user_logged_in():
    if (current_user.is_authenticated):
        return redirect(url_for('index'))


@app.route("/login", methods=["GET","POST"])
def login():
    _check_user_logged_in()
    form = forms.LoginForm()
    if (form.validate_on_submit()):
        user = models.User.query.filter_by(username=form.username.data).first()
        if (user is None or not user.check_password(form.password.data)):
            flash('Invalid username or password.')
            return redirect(url_for('login'))
        login_user(user, remember=form.rememberMe.data)
        if (request.args.get('next')):
            next_page = request.args.get('next').split('/')[0]
        else:
            next_page = 'index'
        if (not next_page or url_parse(next_page).netloc != ''):
            next_page = 'index'
        return redirect(url_for(next_page))

    return render_template("pages/login.html", form=form)

@app.route("/register", methods=["GET", "POST"])
def register():
    _check_user_logged_in()
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
            if (request.args.get('next')):
                next_page = request.args.get('next').split('/')[0]
            else:
                next_page = 'index'
            if (not next_page or url_parse(next_page).netloc != ''):
                next_page = 'index'
            return redirect(url_for(next_page))
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