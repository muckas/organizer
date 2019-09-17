from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
  tasks = None
  with open('tasks.txt', 'r+') as f:
    tasks = f.readlines()
  return render_template('index.html', title='Tasks', tasks=tasks)
