from django.urls import path, re_path
from django.conf.urls import include

# IMPORTACIONES
from loadImage.views import ImagenViews
from loadImage.views import ImagenViewsDetail

urlpatterns = [
    re_path(r'^lista/$', ImagenViews.as_view()),
    re_path(r'^lista/(?P<pk>\d+)$', ImagenViewsDetail.as_view()),
]