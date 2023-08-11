"""Ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from Store import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'Home', views.Home),
    url(r's1', views.store,name="store1"),
    url(r's2/<int:id>', views.Home,name="store2"),
    url(r's3/', views.Login,name="login1"),
    url(r's4/<int:id>', views.store,name="login2"),
    url(r's5/<int:id>', views.Cart,name="cart1"),
    url(r's6/<int:id>', views.store,name="cart2"),
    url(r's7/<int:id>', views.Checkout,name="check1"),
    url(r's8/<int:id>', views.Cart,name="check2"),
    url(r'update_item/', views.updateItem,name="update_item"),
    
]
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)