from django.db import models

# Create your models here.
"""
使用Django进行数据库开发的步骤：
１．定义模型类
２．迁移模型
３．操作数据库
"""
"""
1. 我们的模型类 需要继承自 models.Model
2. 创建类之后，系统会自动为我们添加一个主键--id
3. 字段的定义是
    字段名=model.类型(选项)
    字段名其实就是数据表的字段名，不要采用python、mysql等关键字
    
    char(M)
    varchar(M)
    M 就是这里的选项
"""
# 准备书籍列表信息的模型类
class BookInfo(models.Model):
    # id 字段已自动添加

    # 添加name字段
    name = models.CharField(max_length=10)          #　这里就相当于在数据库里定义了　name vachar(10)

    # 重写 str方法以让admin来显示书籍名字
    def __str__(self):
        return self.name


# 准备人物列表信息的模型类
class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    # 添加外键约束：人物属于哪本书
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    # 重写 str方法以让admin来显示人物名字
    def __str__(self):
        return self.name