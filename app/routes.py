from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
@app.route('/tasks')
def tasks():
  tasks = None
  with open('tasks.txt', 'r+') as f:
    tasks = f.readlines()
  timeframes = []
  timeframe = tasks[0]
  for task in tasks[1:]:
    if task == '\n':
      timeframes.append(timeframe)
      timeframe = ''
    else:
      timeframe += task
  return render_template('tasks.html', title='Tasks', timeframes=timeframes)

@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    flash('Login requested for user {}, remember_me={}'.format(
      form.username.data, form.remember_me.data))
    return redirect(url_for('tasks'))
  return render_template('login.html', title='Sign In', form=form)
