from flask import render_template, redirect, url_for
from app import app


@app.route('/')
@app.route('/index')
@app.route('/tasks')
def tasks():
  tasks = None
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
  return render_template('tasks.html', title='Tasks', timeframes=timeframes)
