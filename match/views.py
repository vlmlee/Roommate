from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, 'index.html', {
		'title': 'Index'
		})

def assessment(request):
	return render(request, 'assessment.html', {
		'title': 'Assessment'
		})

def profile(request):
	return render(request, 'profile.html', {
		'title': 'Profile'
		})