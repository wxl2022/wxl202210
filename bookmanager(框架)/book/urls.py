from django.urls import path
from book.views import index

# 这个是固定写法 urlpatterns = []
urlpatterns = [
    # path(路由, 视图函数名)
    path('index/', index)      # 在客户端进行访问的时候需要 工程的路由 + 子应用的路由
]