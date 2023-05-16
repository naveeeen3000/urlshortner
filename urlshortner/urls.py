from django.contrib import admin
from django.urls import path,include
from .views import index
from url_shortner.views import get_absolute_url

urlpatterns = [
    path('',index,name='index-view'),
    path('api/',include('url_shortner.urls')),
    path('<slug:slug>',get_absolute_url,name='absolute-url-view')
]
