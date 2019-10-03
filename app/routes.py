import os
from flask import render_template, redirect, url_for, request
from app import app
from app.forms import EditForm, AddForm, DelForm
from config import Config


@app.route('/')
@app.route('/index')
@app.route('/<folder>/')
@app.route('/<folder>/<name>')
def show(folder, name=None):
  if folder == 'tasks':
    path = Config.TASKS_PATH
  elif folder == 'notes':
    path = Config.NOTES_PATH
  files = os.listdir(path)
  if name:
    with open(os.path.join(path, name), 'r') as f:
      lines = f.readlines()

    if folder == 'tasks':
      content = []
      if len(lines) > 0:
        timeframe = lines[0]
        for line in lines[1:]:
          if line == '\n':
            content.append(timeframe)
            timeframe = ''
          else:
            timeframe += line
      content.append(timeframe)

    elif folder == 'notes':
      content = ''
      for line in lines:
        content += line

    return render_template('show.html',
        title=folder.title, content=content, files=files, folder=folder, name=name)

  return render_template('show.html', title=folder.upper(), folder=folder, files=files)

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
    return redirect(url_for('show', folder=folder, name=name))
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
    return redirect(url_for('show', folder=folder, name=name))
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
      return redirect(url_for('show', folder=folder))
    return redirect(url_for('show', folder=folder, name=name))
  elif request.method == 'GET':
    return render_template('form.html', title=f'Delete {name}?', form=form)
