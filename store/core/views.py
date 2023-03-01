from django.shortcuts import render
from core.models import Category
from django.shortcuts import get_list_or_404


def index(request):
    return render(request, 'core/index.html', {})


def categoryList(request):
    categories = get_list_or_404(Category)

    template = 'core/category_list.html'
    context = {'categories': categories}

    return render(request, template, context)
