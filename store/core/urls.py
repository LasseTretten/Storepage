from django.urls import path
from core.views import index, categoryList


urlpatterns = [
    path('', index, name='index'),
    path('categories/', categoryList, name='categoryList'),
]
