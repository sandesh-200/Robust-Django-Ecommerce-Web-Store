from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="pasal_home"),
    path("category_items/<str:my_category>", views.category_items, name="category_items"),
    path("about/", views.about, name="pasal_about"),
    path("contact/", views.contact, name="pasal_contact"),
    path("firm/", views.firm, name="pasal_firm"),
    path("product/<int:myid>", views.product, name="pasal_product"),
    path("collection/", views.collection, name="pasal_collection"),
    path("register/", views.site_register, name="pasal_register"),
    path("login/", views.site_login, name="pasal_login"),
    path("account/", views.user_account, name="pasal_account"),
    path("logout/", views.user_logout, name="pasal_logout"),
    path("remove_pic/", views.remove_pic, name="pasal_remove_pic"),
    path("search/", views.search, name="pasal_search"),
    path("purchase/", views.purchase, name="pasal_purchase"),
    path("gateway/", views.purchase, name="pasal_gateway"),
]