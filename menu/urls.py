from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    re_path(r'^.*$', views.IndexView.as_view(), name='catch_all'),
]
