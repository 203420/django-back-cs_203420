from django.urls import path, re_path
from django.conf.urls import include

from UserProfile.views import UserProfileView
from UserProfile.views import UserProfileDetail

urlpatterns = [
    re_path(r'^list/$', UserProfileView.as_view()),
    re_path(r'^getData/(?P<pk>\d+)$', UserProfileDetail.as_view())
]