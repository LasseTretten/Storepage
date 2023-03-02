from django.urls import path
from core.views import index, CategoryList


urlpatterns = [
    path('', index, name='index'),
    path('<path:path>', CategoryList, name='categoryList'),
]
