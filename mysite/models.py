from django.db import models
from django.db.models import Q
from django.core.validators import MinValueValidator, MaxValueValidator
from accounts.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=100)
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
                                  limit_choices_to=~Q(depth=1))     # 2차 카테고리를 parent로 지정 불가하게 설정
    depth = models.PositiveSmallIntegerField(validators=[MaxValueValidator(1)], default=0) # 2차 카테고리까지 가능
    priority = models.PositiveSmallIntegerField()  # 정렬 우선순위

    def __str__(self):
        return self.name


# 제품
class Product(models.Model):
    name = models.CharField(max_length=200)
    about = models.CharField(max_length=50)    # 간단한 설명
    description = models.TextField()    # 상세 설명

    price = models.PositiveIntegerField()
    discount = models.PositiveSmallIntegerField(help_text='할인률(0~99 입력, default 0)', validators=[MaxValueValidator(99,'99 이하의 값을 입력하세요')], default=0)
    image = models.ImageField()

    category_id = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='Product')
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name



# Comment
class Comment(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content_list = models.ForeignKey(Product, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
