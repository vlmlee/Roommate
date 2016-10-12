from django.shortcuts import render

# It's necessary to import from 'models.py' since that's where
# our object relational mapping is from. We can use 'match.models'
# to get specifically from the app 'Roommate/match' or use '.models'
# to get from every app in 'Roommate/'.
from match.models import User

def index(request):
	try: 
		# This is just a test to make sure that we can access the database.
		# I created a row that has my name and email address. I want to see if it 
		# is dynamically inserted into the index.html page when the server responds
		# to a client at 127.0.0.1:8000. We use 'try...except' to handle errors.
		# It is important to use 'objects'.

		person = User.objects.get(name='Michael Lee')

	except User.DoesNotExist:
		raise Http404("Users do not exist.")
		# 'render' is the helper method we use provided by django. You can see at the
		# very top, we imported it from 'django.shortcuts'. It takes 'request' as the first
		# argument, the template as the second argument, and the object we want to dynamically
		# insert as the third argument. 'person', here, is the query we have above.
		# In 'Roommate/templates/index.html', the variable we use to reference 'person' will be the key value, 'user'.
		# 'title' also gets replaced in 'Roommate/templates/index.html' to the string 'Index'.
	return render(request, 'index.html', {
		'title': 'Index',
		'user': person
		})

def assessment(request):
	return render(request, 'assessment.html', {
		'title': 'Assessment'
		})

def profile(request):
	return render(request, 'profile.html', {
		'title': 'Profile'
		})