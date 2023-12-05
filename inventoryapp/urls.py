from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="home_view"),
    path('order/', order, name="order_view"),
    path('product/', product, name="product_view"),
    path('staff/', staff, name="staff_view"),
    path('edit/<pk>', edit, name="edit_view"),
    path('delete/<pk>', delete, name="delete_view"),
    path('register/', register, name="register_view"),
    path('login/', login_view, name="login_view"),
    path('logout/', logout_view, name="logout_view"),
]
