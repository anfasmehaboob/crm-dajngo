from django.urls import path
from . import views
urlpatterns = [

  path('register/',views.register,name='register'),
  path('loginpage/',views.loginpage,name='loginpage'),
  path('logout/',views.logoutUser,name='logout'),


  path('',views.home,name="home"),
  path('products/',views.products,name="products"),
  path('customer/<str:pk_test>/',views.customer,name="customer"),

  path('create_order',views.createOrder,name="createorder"),
  path('update_order/<str:pk>/',views.updateOrder,name="updateorder"),
  path('delete/<str:pk_del>/',views.Delete,name='delete'),
  
  path('create_product/',views.createProduct,name='createproduct')
] 