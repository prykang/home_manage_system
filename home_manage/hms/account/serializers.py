#-*- coding: UTF-8 -*-
# @Author  : countofdane
# @Email   : countofdane@163.com
# @Blog    ：https://blog.csdn.net/countofdane


from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


from rest_framework import serializers
from .models import Authoritycontrol
from django.contrib.auth.models import User




class AuthoritycontrolSerializer(serializers.ModelSerializer):
    # ModelSerializer和Django中ModelForm功能相似
    # Serializer和Django中Form功能相似
    class Meta:
        model = Authoritycontrol
        fields = ('owner', 'testcase_auth', 'sys_auth')

    def create(self,validated_data):
        """
        传入验证过的数据, 创建并返回`Authoritycontrol`实例。
        """
        return Authoritycontrol.objects.create(**validated_data)


    def update(self,instance,validated_data):
        """
        传入验证过的数据, 更新并返回已有的`Authoritycontrol`实例。
        """
        instance.testcase_auth = validated_data.get('testcase_auth',instance.testcase_auth)
        instance.sys_auth = validated_data.get('sys_auth',instance.sys_auth)
        instance.save()
        return instance



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')


    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username',instance.username)
        instance.password = validated_data.get('password',instance.password)
        instance.save()
        return instance

