from django.urls import path
from core import views


urlpatterns = [
    path('', views.index, name='index'),
    path('categories', views.show_categories, name='categories'),
]
