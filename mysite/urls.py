from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='главная'),
    path('add', views.add, name='добавить'),
]