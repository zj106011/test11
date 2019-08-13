from django.conf.urls import url
from Tantan import views
urlpatterns=[
    url(r'^index/',views.index)
]