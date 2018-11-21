#-*- coding: UTF-8 -*-
# @Author  : countofdane
# @Email   : countofdane@163.com
# @Blog    ：https://blog.csdn.net/countofdane

from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(ConsumptionType)
admin.site.register(ConsumptionSubType)
admin.site.register(TransactionLog)
admin.site.register(BankCardType)
admin.site.register(BankCardInfo)
admin.site.register(Bank)