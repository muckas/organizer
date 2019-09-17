# tasks
Web interface task management app

## Installation

### Requirements

```
python
python-pip
```

### Virtual environment

Createing virtual environment
```
python -m venv venv
```
Starting virtual environment
```
source venv/bin/activate
```
Installing python packeges in virtual invironment
```
pip install -r requirements.txt
```

## Testing

### Development server
```
python app.py
```
Runs the server on localhost:5000

### Production server
```
gunicorn -b localhost:5000 app:app
```
Runs WSGI server accessible from outside by yourdomain.com:5000

## Deployment


