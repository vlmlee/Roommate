from django.db import models

# So we write our models here and use django commands through
# the terminal to create the rows in the database. 
# The commands we use are:
# python manage.py makemigrations
# python manage.py migrate
#
# And this will create the database table for us (a *User* table). 
# 'Name' and 'email' will be *columns* and every instance of a User
# will be a row in the 'User' table.

class User(models.Model):
	name = models.CharField(max_length=20)
	email = models.EmailField(max_length=30)