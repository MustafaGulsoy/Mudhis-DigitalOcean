
from django.urls import path, include
from .views import TestView

urlpatterns = [
    path('mustafa',TestView.as_view()),


]
