#-*- coding: UTF-8 -*-
# @Author  : countofdane
# @Email   : countofdane@163.com
# @Blog    ：https://blog.csdn.net/countofdane

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#  基金功能相关的表

# 交易记录
class TransactionLog(models.Model):
    money = models.FloatField('交易金额')
    sha = models.FloatField('上证指数', blank=True, null=True)
    nav = models.FloatField('单位净值', blank=True, null=True)
    #执行方式
    TYPE_CHOICES = (
        ('buy', '买入'),
        ('sell', '卖出'),
    )
    type = models.BooleanField('交易类型',choices=TYPE_CHOICES,default='buy')
    transaction_datetime = models.DateTimeField('交易时间')

    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='创建者', related_name='%(class)s_creator')
    mender = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='修改者', related_name='%(class)s_mender')
    remark = models.CharField('备注', max_length=100, blank=True, null=True)
    create_datetime = models.DateTimeField('创建时间',auto_now_add=True)#auto_now_add 则只是第一次创建添加，之后的更新不再改变。
    update_datetime = models.DateTimeField('更新时间',auto_now=True)#auto_now =True则每次更新都会更新这个时间；
    def __str__(self):
        return "%s" % self.money

    def natural_key(self):
        return (self.money)

# 基金信息
class FundInfo(models.Model):
    # 测试任务 字段： 任务名、执行方式、创建者、更改者，创建时间、更新时间、备注
    name = models.CharField('基金名称', max_length=100)

    transaction_log = models.ForeignKey(TransactionLog, on_delete=models.DO_NOTHING, verbose_name='交易记录', related_name='%(class)s_creator',default=2)


    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='创建者', related_name='%(class)s_creator')
    mender = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='修改者', related_name='%(class)s_mender')
    remark = models.CharField('备注', max_length=100, blank=True, null=True)
    create_datetime = models.DateTimeField('创建时间',auto_now_add=True)#auto_now_add 则只是第一次创建添加，之后的更新不再改变。
    update_datetime = models.DateTimeField('更新时间',auto_now=True)#auto_now =True则每次更新都会更新这个时间；

    total = models.FloatField('交易金额')
    def __str__(self):
        return "%s" % self.name

    def natural_key(self):
        return (self.name)