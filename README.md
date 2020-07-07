# Energy-consumption
## Installation
Install [Python](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installing/) for your OS
Navigate to root folder and install pipenv and django
```
pip install pipenv
pipenv install Django
```
Install the dependencies for postgres (on ubuntu 18.04)
```
sudo apt-get update
sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib

```
Once installed navigate to the folder conatining manage.py and run
```
python manage.py runserver
```
The application is accessible from http://localhost:8000 and to alter the data in the data base visit http://localhost:8000/admin