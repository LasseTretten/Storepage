from django.shortcuts import render
from core.models import Category

def index(request):
    if request.method == 'GET':
        category_id = int(request.GET.get('category_id', default=1))
        current_category = Category.objects.get(pk=category_id)

        children = current_category.get_children()
        ancestors = current_category.get_ancestors()
        products = current_category.products.all()

        context = {
            'categories': children,
            'current_category': current_category,
            'ancestors': ancestors,
            'products': products,
        }

<<<<<<< HEAD
    return render(request, 'your_site/index.html', context)
=======
    return render(request, 'index.html', context)


def show_categories(request):
    return render(request,
                  "categories.html",
                  {'categories': Category.objects.all()})
>>>>>>> f327a02 (Added support for categories.)
