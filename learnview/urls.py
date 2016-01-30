from django.conf.urls import url
from . import views

app_name = "learnview"
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^all/$', views.allrecord, name="allrecord"),
    url(r'individual/(?P<pk>\d+)$', views.individual, name="individual"),
]
