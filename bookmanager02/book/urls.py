from django.urls import path
from book.views import index

urlpatterns = [
    # path(路由, 视图函数)
    path('home/', index)
]