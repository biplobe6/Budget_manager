# Requirements
* Python 3 is required.

# How to install on linux
## Creating virtual environment (recommended)
You can skip this if you don't want
```
python3 -m venv env
source env/bin/activate
pip install -r env/requirements.txt
```

## Database Migration
```
python src/manage.py makemigrations
python src/manage.py migrate
```

# How to install on windows
Windows installer added, just double click on install.bat

# How to run
Activate virtual environment if you are using it.
```
source env/bin/activate
```
Starting server
```
python src/manage.py runserver
```

