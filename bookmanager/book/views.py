from django.shortcuts import render

# Create your views here.
"""
所谓的视图其实就是python函数
视图函数有两个要求：
    1. 第一个参数是HttpRequest类型的对象reqeust，包含了所有请求信息。
    2. 必须返回HttpResponse对象，包含返回给请求者的响应信息
"""
from django.http import HttpRequest
from django.http import HttpResponse
def index(request):
    return HttpResponse('ok')