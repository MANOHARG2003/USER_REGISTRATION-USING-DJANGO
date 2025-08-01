from django.urls import path
from . import views

urlpatterns = [
    path("",views.user , name="user"),
    path("register/", views.create_user, name='register'),
    path("auth_user/",views.auth_user,name="auth_user"),
    path("logout/",views.logout_user,name="logout"),
]