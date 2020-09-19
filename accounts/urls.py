from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('customer/<str:customer_id>', views.customer, name='customer'),
    path('products/', views.products, name='products'),
    path('create_order/', views.create_order, name='create_order'),
    path('update_order/<str:order_id>', views.update_order, name='update_order'),
    path('delete_order/<str:order_id>', views.delete_order, name='delete_order'),
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('logout/', views.logout_user, name='logout')
]