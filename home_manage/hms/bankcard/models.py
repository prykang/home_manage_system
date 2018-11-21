#-*- coding: UTF-8 -*-
# @Author  : countofdane
# @Email   : countofdane@163.com
# @Blog    ：https://blog.csdn.net/countofdane

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ConsumptionType(models.Model):
    type = models.CharField('消费类型', max_length=100, unique=True)
    def __str__(self):
        return "%s" % self.type

    def natural_key(self):
        return (self.type)

class ConsumptionSubType(models.Model):
    higher_type = models.ForeignKey(ConsumptionType, verbose_name='父类型', related_name='%(class)s_higher_type')
    type = models.CharField('消费子类型', max_length=100, unique=True)

    def __str__(self):
        return "%s" % self.type

    def natural_key(self):
        return (self.type)

# class ConsumptionChannel(models.Model):
#     # 微信 支付宝 花呗 银行卡 信用卡
#     type = models.CharField('消费渠道', max_length=100, unique=True)

# 交易记录
class TransactionLog(models.Model):
    money = models.FloatField('交易金额')
    consumption_type = models.ForeignKey(ConsumptionSubType, verbose_name='消费类型', related_name='%(class)s_consumption_type')
    type = models.BooleanField('交易类型',default=True) # 1 是 消费  0 是 入账
    transaction_datetime = models.DateTimeField('交易时间', blank=True, null=True)

    remark = models.CharField('备注', max_length=100, blank=True, null=True)
    create_datetime = models.DateTimeField('创建时间',auto_now_add=True)#auto_now_add 则只是第一次创建添加，之后的更新不再改变。
    update_datetime = models.DateTimeField('更新时间',auto_now=True)#auto_now =True则每次更新都会更新这个时间；
    def __str__(self):
        return "%s" % self.money

    def natural_key(self):
        return (self.money)


class Bank(models.Model):
    name = models.CharField('银行', max_length=100)

    def __str__(self):
        return "%s" % self.name

    def natural_key(self):
        return (self.name)

class BankCardType(models.Model):
    name = models.CharField('类型名称', max_length=100)

    def __str__(self):
        return "%s" % self.name

    def natural_key(self):
        return (self.name)

# 银行卡信息
class BankCardInfo(models.Model):
    # 测试任务 字段： 任务名、执行方式、创建者、更改者，创建时间、更新时间、备注
    bank = models.ForeignKey(Bank, on_delete=models.DO_NOTHING, verbose_name='银行',
                      related_name='%(class)s_bank',default=1)

    bankcard_num = models.CharField('银行卡号', max_length=100,unique=True)
    bankcard_type = models.ForeignKey(BankCardType, on_delete=models.DO_NOTHING, verbose_name='银行卡类型',
                      related_name='%(class)s_bankcard_type',default=1)
    valid_until = models.DateTimeField('有效期至', blank=True, null=True)
    bill_day = models.IntegerField('账单日', blank=True, null=True)
    repay_day = models.IntegerField('还款日', blank=True, null=True)
    annual_fee = models.FloatField('年费/元', blank=True, null=True)
    is_free = models.BooleanField('是否可免费', default=True)
    free_condition = models.CharField('免费条件', max_length=100, blank=True, null=True)
    # transaction_log = models.ForeignKey(TransactionLog, on_delete=models.DO_NOTHING, verbose_name='交易记录', related_name='%(class)s_transaction_log',default=1)


    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='创建者', related_name='%(class)s_creator')
    mender = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='修改者', related_name='%(class)s_mender')
    remark = models.CharField('备注', max_length=100, blank=True, null=True)
    create_datetime = models.DateTimeField('创建时间',auto_now_add=True)#auto_now_add 则只是第一次创建添加，之后的更新不再改变。
    update_datetime = models.DateTimeField('更新时间',auto_now=True)#auto_now =True则每次更新都会更新这个时间；

    def __str__(self):
        return "%s" % self.bank

    def natural_key(self):
        return (self.bank)