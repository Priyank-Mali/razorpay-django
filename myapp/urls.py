from django.urls import path
from . import views

urlpatterns = [
    path('',views.paymentView,name='paymentView'),
    path('success/',views.paymentSuccessView,name='paymentSuccessView'),
]
