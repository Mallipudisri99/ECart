from django.contrib import admin
from Store.models import Customer
from Store.models import Product
from Store.models import Order
from Store.models import OrderItem
from Store.models import ShippingAddress

class CustomerAdmin(admin.ModelAdmin):
    list_display=['user','name','email']
admin.site.register(Customer,CustomerAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display=['name','price','digital']
admin.site.register(Product,ProductAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display=['customer','date_ordered','complete','transaction_id']
admin.site.register(Order,OrderAdmin)

class OrderItemAdmin(admin.ModelAdmin):
    list_display=['product','order','quantity','date_added']
admin.site.register(OrderItem,OrderItemAdmin)

class ShippingAdmin(admin.ModelAdmin):
    list_display=['customer','order','address','city','state','zipcode','date_added']
admin.site.register(ShippingAddress,ShippingAdmin)
