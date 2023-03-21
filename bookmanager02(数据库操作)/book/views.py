from django.http import HttpResponse
from django.shortcuts import render
from book.models import BookInfo
from book.models import Peopleinfo

# Create your views here.
def index(request):
    # books = BookInfo.objects.all()
    # print(books)
    try:
        book = BookInfo.objects.get(id=1)
        print(type(book))
        print(book.id, book.name, book.pub_date, book.readcount)
    except BookInfo.DoesNotExist:
        print('查询结果不存在')
    return HttpResponse(('编号:', book.id, '名称:', book.name, '发布日期:', book.pub_date, '阅读次数:', book.readcount))

###############################　增加数据　###############################
"""
增加数据有两种方法：
1）save
通过创建模型类对象，执行对象的save()方法保存到数据库中。

2）create
通过模型类.objects.create()保存。

注意：要提前导入模型类，这里因为前面已经导入了，所以后面我们就不导入　BookInfo　或　Peopleinfo　了
"""

# 方式１：
book = BookInfo(
    name = 'Django',
    pub_date = '2000-1-1',
    readcount = 10
)
# 必须要调用对象的　save方法　才能将数据保存到数据库中
book.save()

# 方式２：
# objects -- 相当于一个代理　实现增删改查
BookInfo.objects.create(
    name = '测试开发入门',
    pub_date = '2020-1-1',
    readcount = 100
)

###############################　修改数据　###############################
# 修改更新有两种方法
# 方式1
book = BookInfo.objects.get(id=8)
book.name = '运维开发入门'
# 想要保存数据，需要调用对象的save方法
book.save()

# 方式2
BookInfo.objects.filter(id=8).update(name='爬虫入门', commentcount = 666)

###############################　删除数据　###############################
# 删除数据分两种：物理删除（这条数据被删除） 和 逻辑删除（修改标记为，例如：is_delete = False）

# 物理删除方式1：
book = BookInfo.objects.get(id=8)
book.delete()

# 物理删除方式2：
BookInfo.objects.get(id=9).delete()
BookInfo.objects.filter(id=5).delete()

###############################　基本查询　###############################
# get查询单一结果，如果不存在会抛出模型类.DoesNotExist异常
try:
    book = BookInfo.objects.get(id=1)
    print(book)
except BookInfo.DoesNotExist:
    print('查询结果不存在')

# all查询多个结果
BookInfo.objects.all()
Peopleinfo.objects.all()

# count查询结果数量(两种写法一样)
BookInfo.objects.all().count()
BookInfo.objects.count()

###############################　过滤查询　###############################
#　模型类名.objects.filter(属性名__运算符=值)
#　模型类名.objects.exclude(属性名__运算符=值)
#　模型类名.objects.get(属性名__运算符=值)

# 查询编号为１的图书
book = BookInfo.objects.get(id=1)   # 简写形式
book = BookInfo.objects.get(id__exact=1)   # 完整形式
BookInfo.objects.get(pk=1)       # pk: primary key 主键

# 查询书名包含 '湖' 的图书
BookInfo.objects.filter(name__contains='湖')

# 查询书名包含 '部' 的图书
BookInfo.objects.filter(name__endswith='部')

# 查询书名为空的图书
BookInfo.objects.filter(name__isnull=True)

# 查询编号为１或３或５的图书
BookInfo.objects.filter(id__in=[1, 3, 5])

# 查询编号大于３的图书
# gt大于
# gte大于等于
# lt小于
# lte小于等于
BookInfo.objects.filter(id__gt=3)

# 查询编号不等于３的图书
BookInfo.objects.exclude(id=3)

# 查询1980年发布的图书
BookInfo.objects.filter(pub_date__year=1980)

# 查询1990年１月１日后发表的图书
BookInfo.objects.filter(pub_date__gt='1990-1-1')

###############################　F对象　###############################
from django.db.models import F

# 作用：２个属性的比较
# 语法形式：以　filter　为例：　模型类名.objects.filter(属性名__运算符=F('第二个属性名'))

# 查询阅读量大于等于评论量的图书
BookInfo.objects.filter(readcount__gte=F('commentcount'))

# 可以在Ｆ对象上使用算术运算
# 查询阅读量大于２倍评论量的图书
BookInfo.objects.filter(readcount__gt=F('commentcount')*2)

###############################　Q对象　###############################
# 不用Q对象的并且查询
# 查询阅读量大于20，并且编号小于3的图书。
BookInfo.objects.filter(readcount__gt=20).filter(id__lt=3)
# 或者
BookInfo.objects.filter(readcount__gt=20, id__lt=3)


# Q 对象能实现 或 查询，也能实现 与 查询，还能实现 非 查询
from django.db.models import Q
# 或者语法：　模型类名.objects.filter(Q(属性名__运算符=值)|Q(属性名__运算符=值)|...)
# 并且语法:  模型类名.objects.filter(Q(属性名__运算符=值)&Q(属性名__运算符=值)&...)
# not 非 语法:  模型类名.objects.filter(～Q(属性名__运算符=值))

# 查询阅读量大于20，或者编号小于3的图书。
BookInfo.objects.filter(Q(readcount__gt=20)|Q(id__lt=3))
# 查询阅读量大于20，并且编号小于3的图书。
BookInfo.objects.filter(Q(readcount__gt=20)&Q(id__lt=3))
# 查询编号不等于3的图书
BookInfo.objects.filter(~Q(id__exact=3))
BookInfo.objects.filter(~Q(id=3))

###############################　聚合函数　###############################
from django.db.models import Sum, Max, Min, Avg, Count
# 模型类名.objects.aggregate(聚合函数('字段名'))
# 注意：aggregate的返回值是一个字典类型，格式: {'属性名__聚合类小写':值}  如:{'readcount__sum': 126}
BookInfo.objects.aggregate(Sum('readcount'))
BookInfo.objects.count()

###############################　排序　###############################
# 使用 order_by 对结果进行排序
# 默认是升序
BookInfo.objects.all().order_by('readcount')
BookInfo.objects.filter(id__in=[1, 3, 5]).order_by('readcount')
# 降序
BookInfo.objects.all().order_by('-readcount')


###############################　关联查询　###############################
# 由1到多的查询
# 查询书籍为1的所有人物信息（关联查询）
# 获取了id为1的书籍
book = BookInfo.objects.get(id=1)

# 获取到了人物信息
book.peopleinfo_set.all()
book.peopleinfo_set.filter(id=1)
book.peopleinfo_set.filter(id=2)

# 当然上面的这个查询也可以用以下方式来代替，但这就不是关联查询了
Peopleinfo.objects.filter(book=1)            # 注意：这里的 book 是 Peopleinfo模型里的一个字段

# 由多到1的查询
# 查询人物为1的书籍信息
person = Peopleinfo.objects.get(id=1)
person.book.name               # 获取书籍的名称
person.book.readcount　　　　　　# 获取书籍的阅读次数
person.book.pub_date　　　　　　　# 获取书籍的发布日期

###############################　关联过滤查询　###############################
# 查询图书，要求图书人物为“郭靖”，以下两种写法一样
BookInfo.objects.filter(peopleinfo__name__exact='郭靖')           #　注意这里不写成　peopleinfo_set　了
BookInfo.objects.filter(peopleinfo__name='郭靖')

# 查询图书，要求图书中人物的描述包含“八”
BookInfo.objects.filter(peopleinfo__description__contains='八')

# 查询书名为“天龙八部”的所有人物，以下两种写法是一样的
Peopleinfo.objects.filter(book__name__exact='天龙八部')
Peopleinfo.objects.filter(book__name='天龙八部')

# 查询图书阅读量大于30的所有人物
Peopleinfo.objects.filter(book__readcount__gt=30)