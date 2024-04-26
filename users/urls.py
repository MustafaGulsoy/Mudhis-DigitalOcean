from django.urls import path
from django.contrib.auth import views as auth_views
from .views import RegisterView,LoginView,UserView,LogoutView

urlpatterns = [
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user',UserView.as_view(),name='userView'),
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),




]