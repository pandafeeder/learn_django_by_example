from django.conf.urls import include, url

urlpatterns = [
    url(r'^learnview/', include('learnview.urls', namespace="learnview")),
    url(r'^learnform/', include('learnform.urls', namespace="learnform")),
]
