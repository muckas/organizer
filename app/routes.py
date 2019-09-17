from app import app


@app.route('/')
@app.route('/index')
def index():
  tasks = None
  with open('tasks.txt', 'r+') as f:
    tasks = f.readlines()
  tasklist = ''
  for line in tasks:
    tasklist += (f'<pre class="tab">{line}</pre>')
  return f'''
  <html>
    <head>
      <title>Tasks</title>
    </head>
    <body>
      {tasklist}
    </body>
  <html>
  '''
