from django.conf.urls import url
from . import views

app_name = "learnview"
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^all$', views.allrecord, name="allrecord"),
    url(r'^individual/(?P<pk>\d+)$', views.individual, name="individual"),
    url(r'^index$', views.temp_view.as_view()),
    url(r'^class_detail_view/(?P<cate>[\w_\d]+)/(?P<pk>\d+)$', views.detail_view.as_view()),
    url(r'^class_list_view/(?P<cate>\w+)$', views.list_view.as_view()),
]
