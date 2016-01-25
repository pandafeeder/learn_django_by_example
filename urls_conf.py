from django.conf.urls import include, url

urlpatterns = [
    url(r'^learnview/', include('learnview.urls'))
]
