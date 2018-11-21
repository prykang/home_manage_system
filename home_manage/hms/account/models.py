#-*- coding: UTF-8 -*-
# @Author  : countofdane
# @Email   : countofdane@163.com
# @Blog    ：https://blog.csdn.net/countofdane

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Authoritycontrol(models.Model):
    # 权限控制表  数值之间用英文逗号分割 ,
    # testcase_auth 0，1，2...n 表示的是控制的模块 all 表示对所有的模块有删除、修改权限   空表示没有任何的权限
    owner = models.ForeignKey(User,on_delete=models.CASCADE, verbose_name='用户')
    testcase_auth = models.CharField('用例权限',max_length=100,blank=True,null=True,default='')
    # sys_auth 0 表示分发权限的功能，1 表示删除账号的功能 2 添加账号的功能  all 表示拥有所有权限   空表示没有任何的权限
    sys_auth = models.CharField('平台权限',max_length=100,blank=True,null=True,default='')


    def natural_key(self):
        return (self.owner,self.testcase_auth,self.sys_auth)



# class Usertype(models.Model):
#     # 用户类型 主要有 管理员 普通用户 测试模块所属owner
#     type_name = models.CharField('类型名称',max_length=10,blank=True,null=True,unique=True)
#     create_datetime = models.DateField('创建时间',auto_now_add=True)#auto_now_add 则只是第一次创建添加，之后的更新不再改变。
#     update_datetime = models.DateField('更新时间',auto_now=True)#auto_now =True则每次更新都会更新这个时间；
#     remark = models.CharField('备注',max_length=10,blank=True,null=True)
#     def __str__(self):
#         return "%s" % self.remark
#         # return self.type_name,self.remark
#
# class User(models.Model):
#     # 用户信息 主要有 用户类型，用户名，邮箱，密码
#     user_type = models.ForeignKey(Usertype,on_delete=models.DO_NOTHING)
#     user_name = models.CharField('用户名',max_length=100,blank=True,null=True,unique=True)
#     email = models.EmailField('邮箱',blank=True,null=True,unique=True)
#     password = models.CharField('密码',max_length=100)
#     create_datetime = models.DateField('创建时间',auto_now_add=True)#auto_now_add 则只是第一次创建添加，之后的更新不再改变。
#     update_datetime = models.DateField('更新时间',auto_now=True)#auto_now =True则每次更新都会更新这个时间；
#     def __str__(self):
#         return "%s" % self.user_name



