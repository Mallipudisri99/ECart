from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *

def Home(request):
    return render(request,"Ecommerce/Home.html")

def store(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created=Order.objects.get_or_create(customer=customer, complete=False)
        items= order.orderitem_set.all()
        cartItems =order.get_cart_items
    else:
        items=[]
        order={'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cartItems=order['get_cart_items']
    
    products=Product.objects.all()
    context={'items':items,'products':products,'cartItems':cartItems}
    return render(request,"Ecommerce/store.html",context)

def Login(request):
    return render(request,"Ecommerce/login.html")

def Cart(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created=Order.objects.get_or_create(customer=customer, complete=False)
        items= order.orderitem_set.all()
        cartItems =order.get_cart_items
    else:
        items=[]
        order={'get_cart_total':0, 'get_cart_items':0,'shipping':False}
        cartItems=order['get_cart_items']
    context={'items':items,'order':order,'cartItems':cartItems}
    return render(request,"Ecommerce/cart.html",context)

def Checkout(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created=Order.objects.get_or_create(customer=customer, complete=False)
        items= order.orderitem_set.all()
        cartItems =order.get_cart_items
    else:
        items=[]
        order={'get_cart_total':0, 'get_cart_items':0 ,'shipping':False}
        cartItems=order['get_cart_items']
    context={'items':items,'order':order,'cartItems':cartItems}
    return render(request,"Ecommerce/checkout.html",context)


def updateItem(request):
    data= json.loads(request.body)
    productId = data['productId']
    action=data['action']

    print('action:',action)
    print('productId:',productId)
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order,created=Order.objects.get_or_create(customer=customer, complete=False)

    orderItem,created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity =(orderItem.quantity + 1)
    elif action == 'remove':
        OrderItem.quantity = (orderItem.quantity + 1)

    orderItem.save()

    if orderItem.quantity<=0:
        orderItem.delete()
        

    return JsonResponse('Item was added',safe=False)