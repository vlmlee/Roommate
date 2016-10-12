from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^assessment/', views.assessment, name='assessment'),
    url(r'^profile/', views.profile, name='profile'),
]