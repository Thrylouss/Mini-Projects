from django.urls import path

from DataBaseApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin-page/', views.admin_page, name='admin'),
    path('new-product/', views.new_product, name='new-product'),
    path('discount-product/', views.discount_product, name='discount-product'),
    path('category-page/<int:cat_id>/', views.category_page, name='category-page'),
    path('add-product-to-session/<int:product_id>/', views.add_product_to_session, name='add-product-to-session'),
    path('basket-page/', views.basket_page, name='basket-page'),
    path('basket-page/delete-product/<int:product_id>/', views.delete_product, name='delete-product'),
    path('order-page/', views.order_page, name='order-page'),
]