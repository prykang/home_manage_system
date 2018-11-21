#-*- coding: UTF-8 -*-
# @Author  : countofdane
# @Email   : countofdane@163.com
# @Blog    ：https://blog.csdn.net/countofdane


from .models import *
from files.upload.source.search import search_task
from files.upload.source.download import download_task

from hms import celery_app
# 查询可用的搜索下载资源
from celery import task

@task()
def handle_search_and_download_source(pk,title,author):
    data = FictionInfo.objects.get(id=pk)
    source_list = SourceInfo.objects.all().order_by('success_rate','-id')
    for item in source_list:
        print(item.name)
        print(item.search_script)
        print(item.download_script)
        search_task_ret = search_task.call_search(filename=item.search_script,keyword=title,author=author)
        print(search_task_ret)
        if search_task_ret['flag']:
            status = Status.objects.filter(name__startswith='下载中')
            data.source = item
            data.status = status[0]
            data.save()
            print("-----------------")
            print(status[0])
            print('下载中')
            print(data.status)
            download_task_ret = download_task.call_download(filename=item.download_script,
                                                            start_url=search_task_ret['start_url'],
                                                            title=title,
                                                            author=author)
            if download_task_ret['flag']:
                status = Status.objects.filter(name__startswith='已下载')
                data.file_path = download_task_ret['file_path']
                data.status = status[0]
                data.remark = ''
                data.save()
                print("-----------------")
                print(status[0])
                print('已下载')
                print(data.status)
            else:
                # 下载失败
                status = Status.objects.filter(name__startswith='下载失败')
                data.status = status[0]
                data.remark = '下载失败原因：'+ download_task_ret['msg']
                data.save()
                print("-----------------")
                print(status[0])
                print('下载失败')
                print(download_task_ret['msg'])
                print(data.status)
        else:
            status = Status.objects.filter(name__startswith='未找到')
            data.status = status[0]
            data.save()
            print("-----------------")
            print(status[0])
            print('未找到')
            # print(download_task_ret['msg'])
            print(data.status)