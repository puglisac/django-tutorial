# Django Tutorial

## Installation

From the command line:

1. Clone the repository

 ```
$ git clone https://github.com/puglisac/django-tutorial.git
```

2. Create your own virtual environment

 ```
$ python3 -m venv venv
$ source venv/bin/activate
```

 Virtual environments are where dependencies are stored, similar to node_modules in JavaScript. Every time you start your machine, you must activate the virtual environment using source venv/bin/activate.

3. Install your requirements

 ```
$ pip install -r requirements.txt
```

5. Generate a new secret key

 I like using [Djecrety](https://djecrety.ir/) to quickly generate secure secret keys.
Djecrety
Djecrety is a Django secret key generator. This is a web tool to generate SECRET_KEY  

 Create a .env file for your new SECRET_KEY
 
 ```
 $ touch mysite/mysite/.env
 $ open mysite/mysite/.env
 ```
 in mysite/mysite/.env
 
 ```
 DJANGO_KEY = <your SECRET_KEY>
 ```
 
7. Make your migrations
 
 ``` 
 $ cd mysite
 $ python manage.py makemigrations
 $ python manage.py migrate
 ```

8. Create a new superuser

 ```
$ python manage.py createsuperuser
```

9. Final checks

 Start the development server and ensure everything is running without errors.

 ```
$ python manage.py runserver
```
10. To run tests:
 ```
 $ python manage.py test polls