#-*- coding: UTF-8 -*-
# @Author  : countofdane
# @Email   : countofdane@163.com
# @Blog    ：https://blog.csdn.net/countofdane

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import serializers
from .models import *


class BankCardInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = BankCardInfo #
        fields = ('bank','bankcard_num','bankcard_type','valid_until','bill_day','repay_day','annual_fee','is_free',
                  'free_condition','creator','mender','remark','update_datetime','create_datetime')


    def create(self,validated_data):
        """
        传入验证过的数据, 创建并返回`BankCardInfo`实例。
        """
        return BankCardInfo.objects.create(**validated_data)


    def update(self,instance,validated_data):
        """
        传入验证过的数据, 更新并返回已有的`BankCardInfo`实例。
        """
        instance.bank = validated_data.get('bank',instance.bank)
        instance.bankcard_type = validated_data.get('bankcard_type',instance.bankcard_type)
        instance.bankcard_num = validated_data.get('bankcard_num',instance.bankcard_num)
        instance.valid_until = validated_data.get('valid_until',instance.valid_until)
        instance.bill_day = validated_data.get('bill_day',instance.bill_day)
        instance.repay_day = validated_data.get('repay_day',instance.repay_day)
        instance.annual_fee = validated_data.get('annual_fee',instance.annual_fee)
        instance.free = validated_data.get('free',instance.free)
        instance.free_condition = validated_data.get('free_condition',instance.free_condition)
        instance.transaction_log = validated_data.get('transaction_log',instance.transaction_log)
        instance.mender = validated_data.get('mender',instance.mender)
        instance.remark = validated_data.get('remark',instance.remark)
        instance.save()
        return instance


# class BankCardInfoSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = BankCardInfo #
#         fields = ('bank','bankcard_num','bankcard_type','valid_until','bill_day','repay_day','annual_fee','is_free',
#                   'free_condition','creator','mender','remark','update_datetime','create_datetime')
#
#
#     def create(self,validated_data):
#         """
#         传入验证过的数据, 创建并返回`BankCardInfo`实例。
#         """
#         return BankCardInfo.objects.create(**validated_data)
#
#
#     def update(self,instance,validated_data):
#         """
#         传入验证过的数据, 更新并返回已有的`BankCardInfo`实例。
#         """
#         instance.bank = validated_data.get('bank',instance.bank)
#         instance.bankcard_type = validated_data.get('bankcard_type',instance.bankcard_type)
#         instance.bankcard_num = validated_data.get('bankcard_num',instance.bankcard_num)
#         instance.valid_until = validated_data.get('valid_until',instance.valid_until)
#         instance.bill_day = validated_data.get('bill_day',instance.bill_day)
#         instance.repay_day = validated_data.get('repay_day',instance.repay_day)
#         instance.annual_fee = validated_data.get('annual_fee',instance.annual_fee)
#         instance.free = validated_data.get('free',instance.free)
#         instance.free_condition = validated_data.get('free_condition',instance.free_condition)
#         instance.transaction_log = validated_data.get('transaction_log',instance.transaction_log)
#         instance.mender = validated_data.get('mender',instance.mender)
#         instance.remark = validated_data.get('remark',instance.remark)
#         instance.save()
#         return instance