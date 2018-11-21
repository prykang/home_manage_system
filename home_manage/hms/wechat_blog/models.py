# -*- coding: UTF-8 -*-
# @Author  : countofdane
# @Email   : countofdane@163.com
# @Blog    ：https://blog.csdn.net/countofdane

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# 每日名言



class SayingEveryday(models.Model):
    # 测试任务 字段： 任务名、执行方式、创建者、更改者，创建时间、更新时间、备注
    content = models.TextField('内容')
    source = models.CharField('出处', max_length=100, blank=True, null=True)

    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='创建者', related_name='%(class)s_creator')
    mender = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='修改者', related_name='%(class)s_mender')
    remark = models.CharField('备注', max_length=100, blank=True, null=True)
    create_datetime = models.DateTimeField('创建时间',auto_now_add=True)#auto_now_add 则只是第一次创建添加，之后的更新不再改变。
    update_datetime = models.DateTimeField('更新时间',auto_now=True)#auto_now =True则每次更新都会更新这个时间；

    def __str__(self):
        return "%s" % self.name

    def natural_key(self):
        return (self.name)