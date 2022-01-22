from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Category, Comment
from .forms import CommentForm


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


@login_required(login_url='accounts:login')
def comment_create(request, product_id):
    product_list = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.content_list = product_list
            comment.author = request.user
            comment.save()
            return redirect('mysite:detail', product_id=product_list.id)
        else:
            form = CommentForm()

    context = {'content_list': product_list, 'form': form}
    return render(request, 'mysite/content_detail.html', context)


@login_required(login_url='accounts:login')
def comment_update(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        raise PermissionDenied
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect('mysite:detail', product_id=comment.content_list.id)
    else:
        form = CommentForm(instance=comment)
    context = {'comment': comment, 'form': form}
    return render(request, 'mysite/comment_form.html', context)


@login_required(login_url='accounts:login')
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        raise PermissionDenied
    else:
        comment.delete()
    return redirect('mysite:detail', product_id=comment.content_list.id)
