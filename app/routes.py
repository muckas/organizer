import os
from flask import render_template, redirect, url_for, request
from app import app
from app.forms import EditForm
from config import Config


@app.route('/')
@app.route('/index')
@app.route('/tasks/')
@app.route('/tasks/<task>')
def tasks(task=None):
  path = Config.TASKS_PATH
  files = os.listdir(path)
  tasks = None
  if task:
    with open(os.path.join(path, task), 'r') as f:
      tasks = f.readlines()
    timeframes = []
    timeframe = tasks[0]
    for line in tasks[1:]:
      if line == '\n':
        timeframes.append(timeframe)
        timeframe = ''
      else:
        timeframe += line
    timeframes.append(timeframe)
    return render_template('tasks.html', title='Tasks', timeframes=timeframes, files=files, task=task)
  return render_template('tasks.html', title='Tasks', files=files)

@app.route('/edit/<task>', methods=['GET', 'POST'])
def edit_tasks(task):
  path = Config.TASKS_PATH
  form = EditForm()
  if form.validate_on_submit():
    data = form.content.data
    with open(os.path.join(path, task), 'w') as f:
      f.write(data)
    return redirect(url_for('tasks', task=task))
  elif request.method == 'GET':
    with open(os.path.join(path, task), 'r') as f:
      data = f.read()
    form.content.data = data
  return render_template('edit.html', form = form)
