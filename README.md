# django-2-refresh

## Overview

This is a quick project to set up polls per Django docs.  See more here - 

https://docs.djangoproject.com/en/2.2/intro/tutorial01/

## Getting Started

Use pip-env: 

`pip install pipenv`

(if not installed)

Then run: 

`pipenv shell`

to create a virtual environment.

Then 

`pipenv install django`.

Then `django-admin startproject pollingapp`

then `cd pollingapp` and then `python manage.py runserver` to run the server.

To use default migrations to set up tables, run `python manage.py migrate`

Using SQLite to expedite.

Then, run `python manage.py startapp polls` 