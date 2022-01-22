from django.contrib import admin
from .models import Category, Product, Comment


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent_id', 'depth', 'priority']
    search_fields = ['name']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category_id', 'about', 'discount', 'pub_date']
    search_fields = ['name']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['content_list', 'content', 'author', 'create_date', 'modify_date']
    search_fields = ['author']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Comment, CommentAdmin)

