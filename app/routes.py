from flask import render_template
from app import app


@app.route('/')
@app.route('/tasks')
def index():
  tasks = None
  with open('tasks.txt', 'r+') as f:
    tasks = f.readlines()
  return render_template('tasks.html', title='Tasks', tasks=tasks)
