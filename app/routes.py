from flask import render_template, url_for
from app import app, forms
from flask import flash, redirect

@app.route("/")
@app.route("/index")
def index():
    items = [
        {"name" : "Item 1"},
        {"name" : "Item 2"},
    ]
    return render_template("index.html",  title="HELLO", items=items)


@app.route("/login", methods=["GET","POST"])
def login():
    form = forms.LoginForm()
    if (form.validate_on_submit()):
        flash("Login requested for {}, rememeberMe = {}".format(form.username.data, form.rememberMe.data))
        return redirect(url_for("index"))
    return render_template("login.html", form=form)