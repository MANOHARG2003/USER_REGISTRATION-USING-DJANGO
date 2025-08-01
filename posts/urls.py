from django.urls import path
from . import views

urlpatterns = [
    path("",views.post_List,name="post_List"),
    path("contact/",views.contact,name="contact"),
    path("<slug:slug>/",views.post_Detail,name="post_Detail"),
]