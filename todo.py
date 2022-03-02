from app import app, db
from app.models import User, Todo

@app.shell_context_processor
def init_shell_context():
    return {
        'db': db,
        'User': User,
        'Todo': Todo
    }