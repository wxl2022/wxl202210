from django.apps import AppConfig


class BookConfig(AppConfig):
    name = 'book'
    verbose_name = '图书管理'         # 在站点管理界面就会显示 '图书管理'，而不是 'book'
