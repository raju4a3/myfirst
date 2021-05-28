from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('about/',views.about),
    path('index/',views.index),
    path('contact/',views.contact),
    path('employees/',views.employees)
]