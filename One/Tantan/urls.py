from django.conf.urls import url
from Tantan import views
urlpatterns=[
    url(r'^index/',views.index),
    url(r'^login/',views.login),
    url(r'^register/',views.register)
]