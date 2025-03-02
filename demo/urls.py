from django.urls import path
from .import views

urlpatterns = [
    path("demo/" , views.demo , name='demo'),
    path("" , views.home , name='home'),
    path("about/" , views.about , name='about'),
    path("contact/" , views.contact , name='contact'),
    path("blog/" , views.blog , name='blog'),
    path('user/<person>/',views.greet, name='greet'),
     path('favorite/<int:n>/',views.favnum, name='favnum')
]