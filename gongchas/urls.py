from django.urls import path
from . import views

app_name = 'gongchas'
urlpatterns = [
    # ex : /gongchas/
    path('', views.hello, name='hello'),
    # ex : /gongchas/beverage/1/
    path('beverage/<int:bev_id>/', views.order_page, name='order_page'),
    # # ex : /gongchas/beverage/1/check/
    path('beverage/<int:bev_id>/check/', views.check, name='check'),
    # # ex : /gongchas/receipt/
    path('receipt/', views.receipt, name='receipt'),
    # # ex : /gongchas/receipt/1/
    path('receipt/<int:rec_id>/', views.receipt_detail, name='receipt_detail'),
    # # ex : /gongchas/receipt/1/delete/
    path('receipt/<int:rec_id>/delete/', views.receipt_delete, name='receipt_delete'),
    # # ex : /gongchas/topping/
    path('topping/', views.topping, name='topping'),
    # # ex : /gongchas/topping/1/
    path('topping/<int:top_id>/', views.topping_detail, name='topping_detail'),
    # # ex : /gongchas/topping/1/update/
    path('topping/<int:top_id>/update/', views.topping_update, name='topping_update'),

]
