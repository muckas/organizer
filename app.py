from flask import Flask
app = Flask(__name__)

@app.route('/')
def main():
  tasks = None
  with open('tasks.txt', 'r+') as f:
    tasks = f.readlines()
  print(tasks)
  result = ''
  for line in tasks:
    result += (f'<pre class="tab">{line}</pre>')
  return result

if __name__ == '__main__':
  app.run()
