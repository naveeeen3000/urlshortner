from django.urls import path
from .views import URLView

urlpatterns = [
    path('shorturl/',URLView.as_view(),name='url-view')
]