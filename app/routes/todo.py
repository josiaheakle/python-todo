from flask import redirect, render_template, request
from flask_login import current_user, login_required
from app import app, db
from app import models
from app.forms import TodoForm
from app.models import Todo

@app.route('/new-task', methods=['GET', 'POST'])
@login_required
def new_task():
    form = TodoForm()
    if (form.validate_on_submit()):
        task = Todo(title=form.title.data, description=form.description.data, dueDate=form.dueDate.data, userId=current_user.id)
        db.session.add(task)
        db.session.commit()
        return redirect('index')
    return render_template("pages/new-task.html", form=form)

@app.route('/complete-task', methods=["POST"])
def complete_task():
    taskId = request.json['checkboxId']
    task = models.Todo.query.filter_by(id=taskId).first()
    task.toggle()
    db.session.commit()

    return redirect('index')
    