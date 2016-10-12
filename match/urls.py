from django.conf.urls import url

# It's necessary to import 'views' here because we're going to map
# urls to functions.
from . import views

urlpatterns = [
	# views.index, views.assessment, and views.profile are just the functions
	# imported from 'views.py'. 'name' in this case is just going to be a way for us to
	# reference this url pattern, nothing more.
    url(r'^$', views.index, name='index'),
    url(r'^assessment/', views.assessment, name='assessment'),
    url(r'^profile/', views.profile, name='profile'),
]