from django.shortcuts import get_object_or_404, render
from .models import Product, Category


def index(request):
    content_list = Product.objects.order_by('-pub_date')
    context = {'content_list': content_list}
    return render(request, 'mysite/index.html', context)


def detail(request, content_id):
    content_list = get_object_or_404(Product, pk=content_id)
    context = {'content_list': content_list}
    return render(request, 'mysite/content_detail.html', context)