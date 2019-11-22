# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

#用户个人信息模型
class TestmodelUserinfo(models.Model):
    name = models.CharField(max_length=20)
    sex = models.CharField(max_length=10)
    email = models.EmailField()

    class Meta:
        managed = True   #是否修改映射数据库表
        db_table = 'testModel_userinfo'

#
class TestmodelPressinfo(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    class Meta:
        managed = True
        db_table = 'testModel_pressinfo'


#书籍信息
class TestmodelBookinfo(models.Model):
    name=models.CharField(max_length=40)
    author=models.ManyToManyField(TestmodelUserinfo)
    press=models.ForeignKey(TestmodelPressinfo,on_delete=models.CASCADE,)
    pub_date=models.DateField()

    class Meta:
        managed = True
        db_table = 'testModel_bookinfo'