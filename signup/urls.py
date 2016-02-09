from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^login/', views.user_login),
    url(r'^logout/', views.logout),
    url(r'^register/', views.register),
    url(r'^order/', views.order),
    url(r'^order1/', views.order1),
]