from django.urls import path
from . import views

urlpatterns = [
    path('item_create/', views.item_create, name='item_create'),
    path('item/', views.list_items, name='list_item'),
    path('uom/', views.add_uom, name='uom'),
    path('uom_list/', views.uom_list, name='uom_list'),
]