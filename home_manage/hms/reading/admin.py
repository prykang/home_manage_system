#-*- coding: UTF-8 -*-
# @Author  : countofdane
# @Email   : countofdane@163.com
# @Blog    ：https://blog.csdn.net/countofdane

from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Type)
admin.site.register(Country)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Language)
admin.site.register(Book)
admin.site.register(Status)
admin.site.register(ReadingPlan)
admin.site.register(ReadingSummary)