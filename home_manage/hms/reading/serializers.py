#-*- coding: UTF-8 -*-
# @Author  : countofdane
# @Email   : countofdane@163.com
# @Blog    ：https://blog.csdn.net/countofdane

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import serializers
from .models import *


class ReadingPlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReadingPlan #
        fields = ('name','book','start_datetime','end_datetime','overdue_day','status','creator','mender',
                  'remark','update_datetime','create_datetime')


    def create(self,validated_data):
        """
        传入验证过的数据, 创建并返回`BankCardInfo`实例。
        """
        return ReadingPlan.objects.create(**validated_data)


    def update(self,instance,validated_data):
        """
        传入验证过的数据, 更新并返回已有的`BankCardInfo`实例。
        """
        instance.name = validated_data.get('name',instance.name)
        instance.book = validated_data.get('book',instance.book)
        instance.start_datetime = validated_data.get('start_datetime',instance.start_datetime)
        instance.end_datetime = validated_data.get('end_datetime',instance.end_datetime)
        instance.overdue_day = validated_data.get('overdue_day',instance.overdue_day)
        instance.status = validated_data.get('status',instance.status)
        instance.mender = validated_data.get('mender',instance.mender)
        instance.remark = validated_data.get('remark',instance.remark)
        instance.save()
        return instance


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book  #
        fields = (
        'name', 'author', 'word_count', 'desc', 'language', 'book_type', 'tags', 'creator', 'mender', 'remark',
        'create_datetime', 'update_datetime')

    def create(self, validated_data):
        # 传入验证过的数据, 创建并返回`Book`实例。
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # 传入验证过的数据, 更新并返回已有的`Book`实例。
        instance.name = validated_data.get('name', instance.name)
        instance.author = validated_data.get('author', instance.author)
        instance.word_count = validated_data.get('word_count', instance.word_count)
        instance.desc = validated_data.get('desc', instance.desc)
        instance.language = validated_data.get('language', instance.language)
        instance.book_type = validated_data.get('book_type', instance.book_type)
        instance.tags = validated_data.get('tags', instance.tags)
        instance.creator = validated_data.get('creator', instance.creator)
        instance.mender = validated_data.get('mender', instance.mender)
        instance.remark = validated_data.get('remark', instance.remark)
        instance.create_datetime = validated_data.get('create_datetime', instance.create_datetime)
        instance.update_datetime = validated_data.get('update_datetime', instance.update_datetime)
        instance.save()
        return instance


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status  #
        fields = ('name',)

    def create(self, validated_data):
        # 传入验证过的数据, 创建并返回`Status`实例。
        return Status.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # 传入验证过的数据, 更新并返回已有的`Status`实例。
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language  #
        fields = ('tag', 'create_datetime', 'update_datetime', 'creator', 'mender')

    def create(self, validated_data):
        # 传入验证过的数据, 创建并返回`Language`实例。
        return Language.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # 传入验证过的数据, 更新并返回已有的`Language`实例。
        instance.tag = validated_data.get('tag', instance.tag)
        instance.create_datetime = validated_data.get('create_datetime', instance.create_datetime)
        instance.update_datetime = validated_data.get('update_datetime', instance.update_datetime)
        instance.creator = validated_data.get('creator', instance.creator)
        instance.mender = validated_data.get('mender', instance.mender)
        instance.save()
        return instance


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author  #
        fields = ('name', 'country')

    def create(self, validated_data):
        # 传入验证过的数据, 创建并返回`Author`实例。
        return Author.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # 传入验证过的数据, 更新并返回已有的`Author`实例。
        instance.name = validated_data.get('name', instance.name)
        instance.country = validated_data.get('country', instance.country)
        instance.save()
        return instance


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country  #
        fields = ('name',)

    def create(self, validated_data):
        # 传入验证过的数据, 创建并返回`Country`实例。
        return Country.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # 传入验证过的数据, 更新并返回已有的`Country`实例。
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class ReadingSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadingSummary  #
        fields = ('book_count', 'language_count', 'word_count', 'creator', 'mender', 'remark', 'create_datetime',
                  'update_datetime')

    def create(self, validated_data):
        # 传入验证过的数据, 创建并返回` ReadingSummary`实例。
        return ReadingSummary.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # 传入验证过的数据, 更新并返回已有的` ReadingSummary`实例。
        instance.book_count = validated_data.get('book_count', instance.book_count)
        instance.language_count = validated_data.get('language_count', instance.language_count)
        instance.word_count = validated_data.get('word_count', instance.word_count)
        instance.creator = validated_data.get('creator', instance.creator)
        instance.mender = validated_data.get('mender', instance.mender)
        instance.remark = validated_data.get('remark', instance.remark)
        instance.create_datetime = validated_data.get('create_datetime', instance.create_datetime)
        instance.update_datetime = validated_data.get('update_datetime', instance.update_datetime)
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