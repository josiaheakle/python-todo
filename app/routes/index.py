# endpoint for dashboard
from flask import render_template
from flask_login import login_required, current_user

from app import app
from app.models import Todo

@app.route("/")
@app.route("/index")
@login_required
def index():
    tasks = Todo.query.filter_by(userId=current_user.id).all()
    return render_template("pages/index.html",  title="Python Todo", tasks=tasks)