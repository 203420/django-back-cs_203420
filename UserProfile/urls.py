from django.urls import path, re_path
from django.conf.urls import include

from UserProfile.views import UserProfileView
from UserProfile.views import UserProfileDetail
from UserProfile.views import UserProfileData

urlpatterns = [
    re_path(r'^list/$', UserProfileView.as_view()),
    re_path(r'^data/(?P<pk>\d+)$', UserProfileDetail.as_view()),
    re_path(r'^updateData/(?P<pk>\d+)$', UserProfileData.as_view()),
]