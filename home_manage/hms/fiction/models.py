#-*- coding: UTF-8 -*-
# @Author  : countofdane
# @Email   : countofdane@163.com
# @Blog    ：https://blog.csdn.net/countofdane

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Type(models.Model):
    name = models.CharField('类型名称', max_length=100)

    def __str__(self):
        return "%s" % self.name

    def natural_key(self):
        return (self.name)


class Tag(models.Model):
    tag = models.CharField('标签', max_length=20, blank=True, null=True,unique=True)
    def __str__(self):
        return "%s" % self.tag

    def natural_key(self):
        return (self.tag)


class Status(models.Model):
    '''
            ('ready', '未开始'),
            ('finding', '搜索中'),
            ('downing', '下载中'),
            ('done', '已下载'),
            ('not_found', '未找到'),
    '''
    name = models.CharField('状态名称', max_length=100)

    def __str__(self):
        return "%s" % self.name

    def natural_key(self):
        return (self.name)


class Author(models.Model):
    name = models.CharField('作者名', max_length=100,unique=True)
    def __str__(self):
        return "%s" % self.name

    def natural_key(self):
        return (self.name)





class SourceStatus(models.Model):
    '''
        STATUS_CHOICES = (
        ('ready', '待录入'),
        ('able', '可用'),
        ('disable', '失效'),
    )
    '''
    name = models.CharField('状态名称', max_length=100)

    def __str__(self):
        return "%s" % self.name

    def natural_key(self):
        return (self.name)

# 资源信息
class SourceInfo(models.Model):
    # 测试任务 字段： 任务名、执行方式、创建者、更改者，创建时间、更新时间、备注
    name = models.CharField('网站名称', max_length=100)
    site_url = models.CharField('网址', max_length=100)
    search_script = models.CharField('搜索脚本地址', max_length=100, blank=True, null=True)
    download_script = models.CharField('下载脚本地址', max_length=100, blank=True, null=True)

    #资源状态

    status = models.ForeignKey(SourceStatus, on_delete=models.DO_NOTHING, verbose_name='资源状态', related_name='%(class)s_source_status'
                                )
    use_count = models.IntegerField('使用次数',default=0)
    success_count = models.IntegerField('成功下载资源次数',default=0)
    success_rate = models.FloatField('成功率',default=0)

    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='创建者', related_name='%(class)s_creator'
                                )
    mender = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='修改者', related_name='%(class)s_mender'
                               )
    remark = models.CharField('备注', max_length=100, blank=True, null=True)
    create_datetime = models.DateTimeField('创建时间', auto_now_add=True)  # auto_now_add 则只是第一次创建添加，之后的更新不再改变。
    update_datetime = models.DateTimeField('更新时间', auto_now=True)  # auto_now =True则每次更新都会更新这个时间；



# 小说
class FictionInfo(models.Model):
    # 测试任务 字段： 任务名、执行方式、创建者、更改者，创建时间、更新时间、备注
    name = models.CharField('小说名称', max_length=100)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING, verbose_name='作者',
                      related_name='%(class)s_author',default=1)
    file_path = models.CharField('文件地址', max_length=100, blank=True, null=True)
    fiction_type = models.ForeignKey(Type, on_delete=models.DO_NOTHING, verbose_name='小说类型',
                      related_name='%(class)s_fiction_type',default=1)
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING, verbose_name='小说状态',
                      related_name='%(class)s_fiction_status',default=1)
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='标签')
    dialysis_pic = models.CharField('透析图地址', max_length=100, blank=True, null=True)
    source = models.ForeignKey(SourceInfo, on_delete=models.DO_NOTHING, verbose_name='资源来源', related_name='%(class)s_source',null=True)

    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='创建者', related_name='%(class)s_creator')
    mender = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='修改者', related_name='%(class)s_mender')
    remark = models.CharField('备注', max_length=100, blank=True, null=True)
    create_datetime = models.DateTimeField('创建时间',auto_now_add=True)#auto_now_add 则只是第一次创建添加，之后的更新不再改变。
    update_datetime = models.DateTimeField('更新时间',auto_now=True)#auto_now =True则每次更新都会更新这个时间；

    def __str__(self):
        return "%s" % self.name

    def natural_key(self):
        return (self.name)




