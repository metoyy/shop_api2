from django.urls import path
from . import views

urlpatterns = [
    path('', views.OrderApiView.as_view())
]