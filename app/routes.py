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
  files = os.listdir(Config.TASKS_PATH)
  tasks = None
  if task:
    with open('tasks.txt', 'r') as f:
      tasks = f.readlines()
    timeframes = []
    timeframe = tasks[0]
    for task in tasks[1:]:
      if task == '\n':
        timeframes.append(timeframe)
        timeframe = ''
      else:
        timeframe += task
    timeframes.append(timeframe)
    return render_template('tasks.html', title='Tasks', timeframes=timeframes, files=files)
  return render_template('tasks.html', title='Tasks', files=files)

@app.route('/edit', methods=['GET', 'POST'])
def edit_tasks():
  form = EditForm()
  if form.validate_on_submit():
    data = form.content.data
    with open('tasks.txt', 'w') as f:
      f.write(data)
    return redirect(url_for('tasks'))
  elif request.method == 'GET':
    with open('tasks.txt', 'r') as f:
      data = f.read()
    form.content.data = data
  return render_template('edit.html', form = form)
