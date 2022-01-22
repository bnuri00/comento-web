from django.shortcuts import get_object_or_404, render
from .models import Product, Category


def index(request):
    content_list = Product.objects.order_by('-pub_date')
    context = {'content_list': content_list}
    return render(request, 'mysite/index.html', context)

def prodAll(request):
    product_list = Product.objects.order_by('-pub_date')
    product = {'product_list': product_list}
    return render(request, 'mysite/product_list.html', product)

# Category Product list
def prodList(request, cate_name):
    category_list = Category.objects.get(name=cate_name)
    product_list = Product.objects.filter(category_id=category_list.id).order_by('-pub_date')
    content = {'product_list': product_list, 'category_list': category_list}
    return render(request, 'mysite/product_list.html', content)

def detail(request, product_id):
    product_list = get_object_or_404(Product, pk=product_id)
    product = {'product_list': product_list}
    return render(request, 'mysite/content_detail.html', product)
