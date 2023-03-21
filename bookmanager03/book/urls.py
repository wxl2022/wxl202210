from django.urls import path
from book.views import create_book
from book.views import shop, register

urlpatterns = [
    # path('11005/', create_book),
    path('<city_id>/<shop_id>/', shop),
    path('register/', register),
]