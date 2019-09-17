# tasks
Web interface task management app

## Installation

### Requirements

python 3.7
python-pip

### Virtual environment

Createing venv
'''
python -m venv venv
'''
Starting venv
'''
pip install -r requirements.txt
'''

## Testing

### Development server
'''
python app.py
'''
Runs the server on localhost:5000

### Production server
'''
gunicorn -b localhost:5000 app:app
'''
Runs WSGI server accessible from outside by yourdomain.com:5000

## Deployment


