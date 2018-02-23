from django.urls import include, re_path

# import views
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
]