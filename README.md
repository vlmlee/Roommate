I've left some comments in the Roommate/roommate/ folder for each file. Please read them in this order: 'settings.py', '__init__.py', and 'urls.py'. I put '#' around my comments.

## Templates

This is where the html files reside. 'base.html' is the entire layout of the app and every other file is dynamically loaded into base.html via the "extends" tag. You can read the comments in that file.

## Static

Our assets (images, javascript, and CSS) that is served to the client. Currently empty but it's just good to have for the project structure.

## match

This is the "modular app" approach of Django. All it is doing is organizing code. It contains the models ORM and views logic that is served to the client. Please open these files in the folder Roommate/match/ in this order: urls, views, models, __init__.py, and then admin.py. I've left some comments that will explain things more clearly.

# Running this project

Inside this root directory Roommate/, type in the command: `python manage.py runserver`

This will run the development server and you can then go to 127.0.0.1:8000 on a browser to check the project. The root will return you the 'index.html' page. If you go to 127.0.0.1:8000/profile, it will return you the 'profile.html' page. This is configured in 'Roommate/match/urls.py'.

# Using the django MongoDB engine:

http://django-mongodb-engine.readthedocs.io/en/latest/topics/setup.html

Unfortunately because of my slow internet, I wasn't able to download and install the django mongodb engine to test. But this is probably going to be the database we will use.

Here is useful link to get up and running on inserting rows in our sqlite database to pass into the templates. 

https://tutorial.djangogirls.org/en/django_orm/

