import os
from flask import render_template, redirect, url_for, request
from app import app
from app.forms import EditForm, AddForm, DelForm
from config import Config


@app.route('/')
@app.route('/index')
@app.route('/tasks/')
@app.route('/tasks/<name>')
def tasks(name=None):
  path = Config.TASKS_PATH
  files = os.listdir(path)
  tasks = None
  if name:
    with open(os.path.join(path, name), 'r') as f:
      tasks = f.readlines()
    timeframes = []
    if len(tasks) > 0:
      timeframe = tasks[0]
      for line in tasks[1:]:
        if line == '\n':
          timeframes.append(timeframe)
          timeframe = ''
        else:
          timeframe += line
      timeframes.append(timeframe)
    return render_template('tasks.html', title='Tasks', timeframes=timeframes, files=files, name=name)
  return render_template('tasks.html', title='Tasks', files=files)

@app.route('/edit/<folder>/<name>', methods=['GET', 'POST'])
def edit(folder, name):
  if folder == 'tasks':
    path = Config.TASKS_PATH
  elif folder == 'notes':
    path = Config.NOTES_PATH
  form = EditForm()
  if form.validate_on_submit():
    data = form.content.data
    with open(os.path.join(path, name), 'w') as f:
      f.write(data)
    return redirect(url_for(folder, name=name))
  elif request.method == 'GET':
    with open(os.path.join(path, name), 'r') as f:
      data = f.read()
    form.content.data = data
  return render_template('form.html', title=f'Edit {name}', form=form)

@app.route('/add/<folder>', methods=['GET', 'POST'])
def add(folder):
  if folder == 'tasks':
    path = Config.TASKS_PATH
  elif folder == 'notes':
    path = Config.NOTES_PATH
  form = AddForm()
  if form.validate_on_submit():
    name = form.name.data
    content = form.content.data
    with open(os.path.join(path, name), 'x') as f:
      f.write(content)
    return redirect(url_for(folder, name=name))
  elif request.method == 'GET':
    return render_template('form.html', title='Add list', form=form)

@app.route('/remove/<folder>/<name>', methods=['GET', 'POST'])
def remove(folder, name):
  if folder == 'tasks':
    path = Config.TASKS_PATH
  elif folder == 'notes':
    path = Config.NOTES_PATH
  form = DelForm()
  if form.validate_on_submit():
    result = form.result.data
    if result == 'yes':
      os.remove(os.path.join(path, name))
      return redirect(url_for(folder))
    return redirect(url_for(folder, name=name))
  elif request.method == 'GET':
    return render_template('form.html', title=f'Delete {name}?', form=form)

@app.route('/notes/')
@app.route('/notes/<name>')
def notes(name=None):
  path = Config.NOTES_PATH
  files = os.listdir(path)
  if name:
    with open(os.path.join(path, name), 'r') as f:
      lines = f.readlines()
    content = ''
    for line in lines:
      content += line
    return render_template('notes.html', title='Notes', content=content, files=files, name=name)
  return render_template('notes.html', title='Notes', files=files)






















