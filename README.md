# tasks
Web interface task management app

## Installation

### Requirements

On some systems its just "python" instead of "python3"
```
python3
python3-venv
python3-pip
```

### Virtual environment

Createing virtual environment
```
python3 -m venv venv
```
Starting virtual environment
```
source venv/bin/activate
```
Installing python packages in virtual invironment
```
pip install -r requirements.txt
```

## Testing

### Development server
Export flask app variable and run
```
export FLASK_APP=tasks.py
flask run
```
Runs the server on localhost:5000

### Production server
```
gunicorn -b :5000 tasks:app
```
Runs WSGI server accessible from outside on port 5000

## Deployment

### On linux

Running a server from the command line is not advisable, so I am using "supervisor".

Make a config file in /etc/supervisor/conf.d/
```
[program:tasks]
command=/path/to/workdir/venv/bin/gunicorn -b localhost:5000 -w 4 tasks:app
directory=/path/to/workdir/
user=youruser
autostart=true
autorestart=true
stopasgroup=true
killasgroup=true
```
Change path and user, save it and reload supervisor
```
sudo supervisorctl reload
```
Now, after setting up ProxyPass to gunicorn server it's all done

## Deploying updates
For updating just pull the new version and restart the app
```
git pull
sudo supervisorctl restart tasks
```
