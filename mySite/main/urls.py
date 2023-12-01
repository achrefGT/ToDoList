from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.create, name="create"),
    path("", views.home, name="home"),
    path("V1/",views.view1,name="v1"),
    path("<str:name>", views.index, name="index"),
    
]