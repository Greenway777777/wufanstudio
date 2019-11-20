# -*- coding: utf-8 -*-

from django.http import HttpResponse

from testModel.models import UserInfo

# 数据库操作
def testdb(request):
  test1 = UserInfo(name='tom',sex='male',age=21,group='2017',idpassword='440923199803145733')
  test1.save()
  return HttpResponse("<p>数据添加成功！</p>")

def testdb2(request):
  # 初始化
  response = ""
  response1 = ""
  # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
  list = UserInfo.objects.all()
# filter相当于SQL中的WHERE，可设置条件过滤结果
# response2 = UserInfo.objects.filter(id=1)
# 获取单个对象
# response3 = UserInfo.objects.get(id=1)
# 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
  UserInfo.objects.order_by('name')[0:2]
# 数据排序
#UserInfo.objects.order_by("id")
#
#UserInfo.objects.filter(name="").order_by("id")
# 输出所有数据
  for var in list:
    response1 += var.name + " "
    response = response1
  return HttpResponse("<p>" + response + "</p>")