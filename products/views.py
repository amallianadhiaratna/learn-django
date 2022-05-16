from hashlib import new
from django.forms import forms
from django.shortcuts import get_object_or_404, render
from .models import Product
from .forms import ProductForm, RawProductForm
# Create your views here.

# RawProductForm
# def product_create_view(request):
#     form = RawProductForm()
#     if request.method == "POST":
#         print(request.POST)        
#         form = RawProductForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             Product.objects.create(**form.cleaned_data)
#         else:
#             print(form.errors)
#     context = {
#         'form': form
#     }
#     return render(request, "products/create.html", context)

# # HTML form
# def product_create_view(request):
#     print(request.POST)
#     new_title = request.POST.get('title')
#     # Product.objects.create(title=new_title)
#     context = {}
#     return render(request, "products/create.html", context)

# Django model form
def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form 
    }
    return render(request, "products/create.html", context)

def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description
    # }
    context = {
        'object': obj 
    }
    return render(request, "products/detail.html", context)

def render_initial_data(request):
    initial_data = {
        'title' : 'This awesome title'
    }
    obj = Product.objects.get(id=1)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        # form = ProductForm()
    context = {
        'form': form 
    }
    return render(request, "products/create.html", context)

def dynamic_lookup_view(request, product_id):
    # obj = Product.objects.get(id=product_id)
    obj = get_object_or_404(Product, id=product_id)
    context = {
        "object": obj
    }
    return render(request, "products/detail.html", context)