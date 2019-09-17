from app import app


@app.route('/')
@app.route('/index')
def index():
  tasks = None
  with open('tasks.txt', 'r+') as f:
    tasks = f.readlines()
  result = ''
  for line in tasks:
    result += (f'<pre class="tab">{line}</pre>')
  return result
