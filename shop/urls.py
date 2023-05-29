from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('about', about),
    path('video', video),
    path('product',product),
    path('remot', remot),
    path('contact', contact),
    path('product/<int:id>', get_product),
 
]
