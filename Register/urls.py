from django.urls import path, re_path
from Register.views import registro

urlpatterns = [
    re_path(r'^crear/$', registro, name="registro" ),
]