from django.shortcuts import render
from core.models import Category
from django.views import generic


def index(request):
    return render(request, 'core/index.html', {})


class CategoryListView(generic.ListView):
    model = Category
