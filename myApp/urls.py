from django.contrib import admin
from django.urls import path 
from myApp import views
urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("login/", views.login_page, name="login"),
    path("register/", views.register_page, name="register"),
    path("logout/", views.logoutuser, name="logout"),
    path("hero/", views.hero_page, name="hero"),
    path("user/<str:source>/settings", views.settings_page, name="settings"),
    path("upload/",views.upload,name="upload"),
    path("dashboard/",views.dashboard,name="dashboard"),
    path("profile/<str:pk>/",views.profile,name="profile"),
    path("post/",views.post,name="post"),
    path("post/<uuid:pk>/delete/",views.delete_post,name="delete_post"),
    path("search/",views.search,name="search"),
]
