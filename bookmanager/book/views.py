from django.shortcuts import render

# Create your views here.
"""
所谓的视图其实就是python函数
视图函数有两个要求：
    1. 第一个参数是HttpRequest类型的对象reqeust，包含了所有请求信息。
    2. 必须返回HttpResponse对象，包含返回给请求者的响应信息，render就能返回HttpResponse对象。
"""
from django.http import HttpRequest
from django.http import HttpResponse

def index(request):
    # return HttpResponse('ok')

    # render 作用：渲染模板   它的前三个参数如下
    # 参数1：request　请求
    # 参数2：template_name 模板名字，注意：这里是指路径名
    # 参数3：context=None 将视图中的数据传递给HTML(模板)

    # 模拟从数据库里查询出来的数据
    value = {
        'name':'马上双11，点击有惊喜'
    }
    return render(request, 'book/index.html', context=value)