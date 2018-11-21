#-*- coding: UTF-8 -*-
# @Author  : countofdane
# @Email   : countofdane@163.com
# @Blog    ：https://blog.csdn.net/countofdane

"""hms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^account/', include('account.urls')),
    url(r'^bankcard/', include('bankcard.urls')),
    url(r'^fiction/', include('fiction.urls')),
    url(r'^fund/', include('fund.urls')),
    url(r'^health/', include('health.urls')),
    url(r'^internet_account/', include('internet_account.urls')),
    url(r'^project/', include('project.urls')),
    url(r'^reading/', include('reading.urls')),
    url(r'^wechat_blog/', include('wechat_blog.urls')),

    url(r'^filemanager/', include('filemanager.urls')),
    url(r'^download/(?P<path>.*)$', serve, {'document_root': './files', 'show_indexes':True}),
]
