# Organizer
Web interface organizer app

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
export FLASK_APP=organizer.py
flask run
```
Runs the server on localhost:5000

### Production server
```
gunicorn -b :5000 organizer:app
```
Runs WSGI server accessible from outside on port 5000

## Deployment

### On linux

Make config.cfg out of config.cfg.default
```
SECRET_KEY - a key for scrf token
BASIC_AUTH_USERNAME - authentication username
BASIC_AUTH_PASSWORD - authentication password
BASIC_AUTH_FORCE - True to use authentication, False to disable it
```

Run WSGI server using supervisor

Make a config file in /etc/supervisor/conf.d/
```
[program:organizer]
command=/path/to/workdir/venv/bin/gunicorn -b localhost:5000 organizer:app
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
For updating, pull lstest release from master, install pip requirements and restart the app
```
git pull
source venv/bin/activate
pip install -r requirements.txt
sudo supervisorctl restart organizer
```
