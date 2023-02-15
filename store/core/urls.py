from django.urls import path
from core.views import index, CategoryListView


urlpatterns = [
    path('', index, name='index'),
    path('categories', CategoryListView.as_view(), name='categories'),
]
