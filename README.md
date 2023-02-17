### Welcome

This is a demo signals app.

In order to use it you have to do the following.

``` bash
git clone https://github.com/r3ap3rpy/django-signals.git
virtualenv djangoinv
djangoinv\Scripts\activate.bat
pip install django
cd django-signals
python manage.py migrate
python manage.py makemigrations
python manage.py createsuperuser
python manage.py runserver
```

Make sure you populate the tables via the admin interface.