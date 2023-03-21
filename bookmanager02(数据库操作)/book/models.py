from django.db import models

# Create your models here.
"""
1. 模型类需要继承自 models.Model

2. 定义属性
    属性名 = models.类型(选项)     
    
    2.1 属性名 对应 字段名
        不要使用python，mysql关键字
        不要使用连续的下划线
    2.2 字段类型要和 mysql的字段类型对应，例如： CharField 对应 varchar
    2.3 选项  对应的就是数据库里的约束，例如NOT NULL, PRIMARY KEY, UNIQUE KEY, DEFAULT, FOREIGN KEY
             CharField 必须设置 max_length
             verbose_name 这个主要是在站点里使用
    2.4 id字段，系统会默认自动生成

3. 改变表的名称
    默认表的名字是： 子应用_类名   都是小写
    修改表的名字：class Meta  固定写法
    
"""
class BookInfo(models.Model):
    name = models.CharField(max_length=10, unique=True)
    pub_date = models.DateField(null=True)
    readcount = models.IntegerField(default=0)
    commentcount = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)

    """
    注意：因为在模型Peopleinfo中定义了关联BookInfo的外键
    所以系统会为我们在本模型中自动添加一个字段为 关联模型类名小写_set
    也就是 peopleinfo_set = [Peopleinfo, Peopleinfo, ...]，这个字段是看不见的。
    另外，还有一个就是 peopleinfo 字段，也是看不见的。
    """

    class Meta:
        db_table = 'bookinfo'    # 修改表的名字为bookinfo
        verbose_name = '书籍管理'   # admin站点使用的（了解）

    def __str__(self):
        return self.name

class Peopleinfo(models.Model):

    #　定义一个有序字典
    GENDER_CHOICE = ((1, 'male'), (2, 'female'))
    # print(type(GENDER_CHOICE))

    name = models.CharField(max_length=10, unique=True)
    gender = models.SmallIntegerField(choices=GENDER_CHOICE, default=1)
    description = models.CharField(max_length=100, null=True)
    is_delete = models.BooleanField(default=False)

    #　外键
    # CASCADE级联，删除主表数据时连通一起删除外键表中数据
    # 系统会自动为外键添加　_id，所以这里的外键名会变成　book_id　而不是　book
    # 注意：这里的外键它也是一个字段，在数据库里就是 book_id
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)
    # 注意：这里的 book 其实相当于 book = BookInfo()，也就是说它是BookInfo类的一个对象

    class Meta:
        db_table = 'peopleinfo'        # 修改表的名字为peopleinfo

    def __str__(self):
        return self.name