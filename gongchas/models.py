from datetime import datetime

from django.db import models
from django.utils import timezone


# Create your models here.


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)


class Beverage(models.Model):
    id = models.AutoField(primary_key=True)  # 이걸 넣어 말어
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='beverages')
    name = models.CharField(max_length=80)
    size = models.CharField(max_length=80)
    price = models.IntegerField(null=False, blank=False)
    rec_sugar = models.CharField(max_length=80)  # 당도 고정이 있네!?
    rec_ice = models.CharField(max_length=80)
    is_ice_only = models.BooleanField(default=False)  # False 0 / True 1
    menu_image = models.URLField(max_length=200)

    class Meta:
        db_table = "beverages"


class Topping(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80)
    size = models.CharField(max_length=80)  # L / J
    price = models.IntegerField(null=False, blank=False)

    class Meta:
        db_table = "toppings"

# is_ice_only가 false(0)일때 hot인데 얼음량이 셋중 하나이면 주문하기 눌렀을때 에러 메세지
# is_ice_only가 true(1)일때 옵션이 hot이면 에러


class Receipt(models.Model):  # 주문할 음료의 정보를 저장 (나중에 영수증에 표시될거)
    id = models.AutoField(primary_key=True)
    beverage = models.CharField(max_length=80)
    size = models.CharField(max_length=80)  # L
    option = models.CharField(max_length=80)  # Hot
    sugar = models.CharField(max_length=80)  # 30%
    ice = models.CharField(max_length=80)  # regular
    topping = models.CharField(max_length=80, null=True, blank=True)  # 화이트펄 L (+ 300)
    # topping_size = models.CharField(max_length=80, null=True, blank=True)  # L (+ 300)
    # topping = models.ForeignKey(Topping, on_delete=models.CASCADE)  이건?
    total = models.IntegerField(default=0)
    order_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "receipt"

# my_choice -> snake case
# myChoice -> camel case
# my-choice -> kebab case

