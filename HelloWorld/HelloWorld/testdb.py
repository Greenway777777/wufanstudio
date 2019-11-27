# -*- coding: utf-8 -*-

from django.http import HttpResponse

from TestModel.models import TestmodelUserinfo

# 数据库操作
def testdb(request):
  test1 = TestmodelUserinfo(name='tom', sex='male', email='393799961')
  test1.save()
  return HttpResponse("<p>数据添加成功！</p>")


# 数据库操作
def testdb2(request):
    # 初始化
    response = ""
    response1 = ""
    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = TestmodelUserinfo.objects.all()

    # filter相当于SQL中的WHERE，可设置条件过滤结果
    #response2 = TestmodelUserinfo.objects.filter(id=1)

    # 获取单个对象
    #response3 = TestmodelUserinfo.objects.get(id=1)

    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    #TestmodelUserinfo.objects.order_by('name')[0:2]

    # 数据排序
    #TestmodelUserinfo.objects.order_by("id")

    # 上面的方法可以连锁使用
    #TestmodelUserinfo.objects.filter(name="w3cschool.cn").order_by("id")

    # 输出所有数据
    for var in list:
        response1 += var.name + " "+var.sex+" "+var.email+" "
        response = response1
    return HttpResponse("<p>" + response + "</p>")


# 数据库操作
def testdb3(request):
    # 修改其中一个id=1的name字段，再save，相当于SQL中的UPDATE
    test1 = TestmodelUserinfo.objects.get(id=1)
    test1.name = 'w3cschoolW3Cschool教程'
    test1.save()
    # 另外一种方式
    # Test.objects.filter(id=1).update(name='w3cschoolW3Cschool教程')

    # 修改所有的列
    # Test.objects.all().update(name='w3cschoolW3Cschool教程')
    return HttpResponse("<p>修改成功</p>")


# 数据库操作
def testdb4(request):
    # 删除id=1的数据
    test1 = TestmodelUserinfo.objects.get(id=1)
    test1.delete()
    # 另外一种方式
    # Test.objects.filter(id=1).delete()

    # 删除所有数据
    # Test.objects.all().delete()
    return HttpResponse("<p>删除成功</p>")