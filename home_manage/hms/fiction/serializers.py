#-*- coding: UTF-8 -*-
# @Author  : countofdane
# @Email   : countofdane@163.com
# @Blog    ：https://blog.csdn.net/countofdane

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import serializers
from .models import *


class FictionInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = FictionInfo #
        fields = ('name','author','file_path','status','tags','dialysis_pic','source',
                  'creator','mender','remark','update_datetime','create_datetime')


    def create(self,validated_data):
        """
        传入验证过的数据, 创建并返回`FictionInfo`实例。
        """
        if "tags" in validated_data:
            tags = validated_data.pop('tags')
        else:
            tags = []
        fiction = FictionInfo.objects.create(**validated_data)
        for tg in tags:
            fiction.tags.add(tg)
        return fiction


    def update(self,instance,validated_data):
        """
        传入验证过的数据, 更新并返回已有的`FictionInfo`实例。
        """
        instance.name = validated_data.get('name',instance.name)
        instance.author = validated_data.get('author',instance.author)
        instance.status = validated_data.get('status',instance.status)
        instance.dialysis_pic = validated_data.get('dialysis_pic',instance.dialysis_pic)
        instance.source = validated_data.get('source',instance.source)
        instance.tags = validated_data.get('tags', instance.tags)
        instance.mender = validated_data.get('mender',instance.mender)
        instance.remark = validated_data.get('remark',instance.remark)
        instance.save()
        return instance


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type  #
        fields = ('name',)

    def create(self, validated_data):
        # 传入验证过的数据, 创建并返回`Type`实例。
        return Type.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # 传入验证过的数据, 更新并返回已有的`Type`实例。
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance



class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author  #
        fields = ('name',)

    def create(self, validated_data):
        # 传入验证过的数据, 创建并返回`Type`实例。
        return Author.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # 传入验证过的数据, 更新并返回已有的`Type`实例。
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class SourceInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SourceInfo  #
        fields = (
        'name', 'site_url', 'search_script', 'download_script', 'status', 'use_count', 'success_count', 'success_rate',
        'creator', 'mender', 'remark', 'create_datetime', 'update_datetime')

    def create(self, validated_data):
        # 传入验证过的数据, 创建并返回`SourceInfo`实例。
        return SourceInfo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # 传入验证过的数据, 更新并返回已有的`SourceInfo`实例。
        instance.name = validated_data.get('name', instance.name)
        instance.site_url = validated_data.get('site_url', instance.site_url)
        instance.search_script = validated_data.get('search_script', instance.search_script)
        instance.download_script = validated_data.get('download_script', instance.download_script)
        instance.status = validated_data.get('status', instance.status)
        instance.use_count = validated_data.get('use_count', instance.use_count)
        instance.success_count = validated_data.get('success_count', instance.success_count)
        instance.success_rate = validated_data.get('success_rate', instance.success_rate)
        instance.mender = validated_data.get('mender', instance.mender)
        instance.remark = validated_data.get('remark', instance.remark)
        instance.save()
        return instance


class SourceStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = SourceStatus  #
        fields = ('name',)

    def create(self, validated_data):
        # 传入验证过的数据, 创建并返回`SourceStatus`实例。
        return SourceStatus.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # 传入验证过的数据, 更新并返回已有的`SourceStatus`实例。
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
