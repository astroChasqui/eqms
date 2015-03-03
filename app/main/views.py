from flask import render_template
from . import main
from ..models import User

@main.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)
