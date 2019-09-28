import os
from flask import render_template, redirect, url_for, request
from app import app
from app.forms import EditForm, AddForm, DelForm
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
  return render_template('form.html', title=f'Edit {task}', form=form)

@app.route('/add_tasks', methods=['GET', 'POST'])
def add_tasks():
  path = Config.TASKS_PATH
  form = AddForm()
  if form.validate_on_submit():
    name = form.name.data
    content = form.content.data
    with open(os.path.join(path, name), 'x') as f:
      f.write(content)
    return redirect(url_for('tasks', task=name))
  elif request.method == 'GET':
    return render_template('form.html', title='Add list', form=form)

@app.route('/del/<task>', methods=['GET', 'POST'])
def del_tasks(task):
  form = DelForm()
  if form.validate_on_submit():
    result = form.result.data
    path = Config.TASKS_PATH
    if result == 'yes':
      os.remove(os.path.join(path, task))
      return redirect(url_for('tasks'))
    return redirect(url_for('tasks', task=task))
  elif request.method == 'GET':
    return render_template('form.html', title=f'Delete {task}?', form=form)























