from django.http import HttpResponse
from django.shortcuts import render
from book.models import BookInfo

# Create your views here.
def create_book(request):
    book = BookInfo.objects.create(
        name = 'abc',
        pub_date = '2000-1-1',
        readcount = 10,
    )

    return HttpResponse('create')

def shop(request, city_id, shop_id):
    print(city_id, shop_id)

    # query_params = request.GET
    # print(query_params)                     # <QueryDict: {'order': ['readcount']}>
    # print(query_params.get('order'))        # readcount
    # print(query_params['order'])            # readcount

    query_params = request.GET
    print(query_params)                       # <QueryDict: {'order': ['readcount', 'commentcount'], 'page': ['1']}>}>
    print(query_params.get('k1'))          # commentcount
    # print(query_params['order'])              # commentcount
    print(query_params.getlist('k1'))      # ['readcount', 'commentcount']

    #　注意：get()方法只能获取　QueryDict　键　的最后一个值，而getlist()方法可以获取所有值，以列表返回

    return HttpResponse('齐哥的小饭店')

def register(request):
    data = request.POST
    print(data)

    return HttpResponse('ok')

