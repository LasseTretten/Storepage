from django.shortcuts import render, redirect, get_object_or_404
from core.models import Category
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


def index(request):
    if request.method == 'GET':
        category_id = int(request.GET.get('category_id', default=1))
        current_category = Category.objects.get(pk=category_id)

        children = current_category.get_children()
        ancestors = current_category.get_ancestors()
        products = current_category.products.all()

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


def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user_username = form.cleaned_data['username']
            user_password = form.cleaned_data['password1']
            user = authenticate(username=user_username, password=user_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()

    template = "core/registration/register_user.html"
    context = {'form': form}

    return render(request, template, context)
