Requirements:

Python 3.8

Other dependencies in Pipfile

Steps to setup locally:

Install pipenv for dependency management

pip install pipenv

Use pipenv to install other dependencies from Pipfile

pipenv install --dev

Activate the new virtual environment

pipenv shell

Install django in virtual environment

pipenv pipinstall django

Run development server on localhost

python manage.py runserver :8000
