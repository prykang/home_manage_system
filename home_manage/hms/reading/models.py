#-*- coding: UTF-8 -*-
# @Author  : countofdane
# @Email   : countofdane@163.com
# @Blog    ：https://blog.csdn.net/countofdane

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Type(models.Model):
    name = models.CharField('类型名称', max_length=100,unique=True)

    def __str__(self):
        return "%s" % self.name

    def natural_key(self):
        return (self.name)


class Country(models.Model):
    name = models.CharField('国家', max_length=100,unique=True)
    def __str__(self):
        return "%s" % self.name

    def natural_key(self):
        return (self.name)


class Author(models.Model):
    name = models.CharField('作者名', max_length=100,unique=True)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, verbose_name='国家', related_name='%(class)s_country')
    def __str__(self):
        return "%s" % self.name

    def natural_key(self):
        return (self.name)

class Tag(models.Model):
    tag = models.CharField('标签', max_length=20, blank=True, null=True,unique=True)
    create_datetime = models.DateTimeField('创建时间',auto_now_add=True)#auto_now_add 则只是第一次创建添加，之后的更新不再改变。
    update_datetime = models.DateTimeField('更新时间',auto_now=True)#auto_now =True则每次更新都会更新这个时间；
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='创建者', related_name='%(class)s_creator',
                                blank=True, null=True)
    mender = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='修改者', related_name='%(class)s_mender',
                               blank=True, null=True)
    def __str__(self):
        return "%s" % self.tag

    def natural_key(self):
        return (self.tag)

class Language(models.Model):

    name = models.CharField('语言', max_length=100)
    def __str__(self):
        return "%s" % self.name

    def natural_key(self):
        return (self.name)



# 小说信息
class Book(models.Model):
    # 测试任务 字段： 任务名、执行方式、创建者、更改者，创建时间、更新时间、备注
    name = models.CharField('书名', max_length=100)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING, verbose_name='作者', related_name='%(class)s_author')
    word_count = models.FloatField('字数（万字）', blank=True, null=True)
    desc = models.TextField('描述', blank=True, null=True)
    language = models.ForeignKey(Language, on_delete=models.DO_NOTHING, verbose_name='语言', related_name='%(class)s_language',default=1)

    book_type = models.ForeignKey(Type, on_delete=models.DO_NOTHING, verbose_name='图书类型',
                      related_name='%(class)s_book_type',default=1)
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='标签')

    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='创建者', related_name='%(class)s_creator')
    mender = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='修改者', related_name='%(class)s_mender')
    remark = models.CharField('备注', max_length=100, blank=True, null=True)
    create_datetime = models.DateTimeField('创建时间',auto_now_add=True)#auto_now_add 则只是第一次创建添加，之后的更新不再改变。
    update_datetime = models.DateTimeField('更新时间',auto_now=True)#auto_now =True则每次更新都会更新这个时间；

    def __str__(self):
        return "%s" % self.name

    def natural_key(self):
        return (self.name)



#  未开始  进行中  逾期中  已完成
class Status(models.Model):
    name = models.CharField('状态名称', max_length=100)

    def __str__(self):
        return "%s" % self.name

    def natural_key(self):
        return (self.name)

#
# class ReadingLog(models.Model):
#
#     creator = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='创建者', related_name='%(class)s_creator')
#     mender = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='修改者', related_name='%(class)s_mender')
#     remark = models.CharField('备注', max_length=100, blank=True, null=True)
#     create_datetime = models.DateTimeField('创建时间',auto_now_add=True)#auto_now_add 则只是第一次创建添加，之后的更新不再改变。
#     update_datetime = models.DateTimeField('更新时间',auto_now=True)#auto_now =True则每次更新都会更新这个时间；



class ReadingPlan(models.Model):
    name = models.CharField('计划名称', max_length=100)

    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING, verbose_name='图书',
                                  related_name='%(class)s_book', default=1)
    start_datetime = models.DateTimeField('开始时间')  #
    end_datetime = models.DateTimeField('截至时间')  #
    overdue_day = models.IntegerField('逾期天数',default=0)
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING, verbose_name='计划状态', related_name='%(class)s_plan_status',default=1)
    # readinglog = models.ForeignKey(ReadingLog, on_delete=models.DO_NOTHING, verbose_name='计划状态', related_name='%(class)s_plan_status')
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='创建者', related_name='%(class)s_creator')
    mender = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='修改者', related_name='%(class)s_mender')
    remark = models.CharField('备注', max_length=100, blank=True, null=True)
    create_datetime = models.DateTimeField('创建时间', auto_now_add=True)  #
    update_datetime = models.DateTimeField('更新时间', auto_now=True)  #

    def __str__(self):
        return "%s" % self.name

    def natural_key(self):
        return (self.name)


class  ReadingSummary(models.Model):
    book_count = models.IntegerField('图书数量',default=0)
    language_count = models.IntegerField('语言计数',default=1)
    word_count = models.FloatField('总字数（万字）', default=0)


    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='创建者', related_name='%(class)s_creator')
    mender = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='修改者', related_name='%(class)s_mender')
    remark = models.CharField('备注', max_length=100, blank=True, null=True)
    create_datetime = models.DateTimeField('创建时间', auto_now_add=True)  #
    update_datetime = models.DateTimeField('更新时间', auto_now=True)  #


