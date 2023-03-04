from django.shortcuts import render
from core.models import Category
from django.shortcuts import get_list_or_404
from django.shortcuts import get_object_or_404


def index(request):
    return render(request, 'core/index.html', {})


def categoryList(request, path):

    category_path = path.split('/')
    if category_path[-1] == '':
        category_path = category_path[:-1]

    # REWRITE TO FETCH OBJECTS.
    category = get_object_or_404(Category,
                                 slug__exact=category_path[-1])
    categories = Category.objects.filter(parent__exact=category.id)

    print(categories)

    template = 'core/category_list.html'
    context = {'categories': categories, 'path': path}

    return render(request, template, context)
