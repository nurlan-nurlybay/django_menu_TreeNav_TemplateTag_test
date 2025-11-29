from django.urls import path

from . import views

app_name = "menu"
urlpatterns = [
    # ex: /menu/
    path("", views.IndexView.as_view(), name="index"),
    path("nodes-dict", views.NodesDictView.as_view(), name="nodes_dict"),
]