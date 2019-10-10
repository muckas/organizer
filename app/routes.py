import os
from flask import render_template, redirect, url_for, request
from app import app
from app.forms import EditForm, AddForm, DelForm
from config import Config


@app.route('/')
@app.route('/index')
@app.route('/<folder>/')
@app.route('/<folder>/<name>')
def show(folder='tasks', name=None):
  path = Config.CONTENT_PATH
  folders = Config.CONTENT_FOLDERS
  files = os.listdir(os.path.join(path, folder))
  if name:
    with open(os.path.join(path, folder, name), 'r') as f:
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
      content = str()
      for line in lines:
        content += line

    return render_template('show.html',
        title=folder.title(), content=content, files=files, folders=folders, folder=folder, name=name)
  return render_template('show.html', title=folder.title(), folders=folders, folder=folder, files=files)

@app.route('/edit/<folder>/<name>', methods=['GET', 'POST'])
def edit(folder, name):
  path = Config.CONTENT_PATH
  folders = Config.CONTENT_FOLDERS
  form = EditForm()
  if form.validate_on_submit():
    data = form.content.data
    with open(os.path.join(path, folder, name), 'w') as f:
      f.write(data)
    return redirect(url_for('show', folder=folder, name=name))
  elif request.method == 'GET':
    with open(os.path.join(path, folder, name), 'r') as f:
      data = f.read()
    form.content.data = data
  return render_template('form.html', title=f'Edit {name}', folders=folders, form=form)

@app.route('/add/<folder>', methods=['GET', 'POST'])
def add(folder):
  path = Config.CONTENT_PATH
  folders = Config.CONTENT_FOLDERS
  form = AddForm()
  if form.validate_on_submit():
    name = form.name.data
    content = form.content.data
    with open(os.path.join(path, folder, name), 'x') as f:
      f.write(content)
    return redirect(url_for('show', folder=folder, name=name))
  elif request.method == 'GET':
    return render_template('form.html', title='Add list', folders=folders, form=form)

@app.route('/remove/<folder>/<name>', methods=['GET', 'POST'])
def remove(folder, name):
  path = Config.CONTENT_PATH
  folders = Config.CONTENT_FOLDERS
  form = DelForm()
  if form.validate_on_submit():
    result = form.result.data
    if result == 'yes':
      os.remove(os.path.join(path, folder, name))
      return redirect(url_for('show', folder=folder))
    return redirect(url_for('show', folder=folder, name=name))
  elif request.method == 'GET':
    return render_template('form.html', title=f'Delete {name}', folders=folders,  form=form)
