#-*- coding: UTF-8 -*-
# @Author  : countofdane
# @Email   : countofdane@163.com
# @Blog    ：https://blog.csdn.net/countofdane

from .serializers import *
from django.http import  JsonResponse
# from rest_framework.response import Response
# from rest_framework import status
from rest_framework.decorators import api_view
# from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,logout
import json
from common.common import *
from rest_framework.authtoken.models import Token
from django.core.serializers import serialize
from django.core.paginator import Paginator
import re
from .task import *
import os


# 开始搜索和下载接口
@api_view(['POST'])
@csrf_exempt
def start_search_and_download(request):
    try:
        if request.user.is_authenticated():
            if 'pk' in request.data and re.match(r'^[0-9]+$',str(request.data['pk']).strip()):
                pk = str(request.data['pk']).strip()
                data = FictionInfo.objects.filter(id=pk)
                if data.exists():
                    status = Status.objects.filter(name__startswith='搜索中')
                    data[0].status = status[0]
                    data[0].save()
                    serialized_data = serialize('python', data, use_natural_foreign_keys=True)
                    title = serialized_data[0]['fields']['name']
                    author = serialized_data[0]['fields']['author']
                    print(title)
                    print(author)
                    handle_search_and_download_source.delay(pk,title,author)
                    return JsonResponse(
                        {
                            'code': '000000',
                            'msg': '正在后台进行搜索和下载，完成后会有消息通知，请注意查收'
                        },
                        status=200)
                else:
                    return JsonResponse(
                        {
                            'code': '400001',
                            'msg': '查询失败'
                        },
                        status=200)
            else:
                return JsonResponse(
                    {
                        'data': {
                            'pk': 'This field is required.'
                        },
                        'code': '400001',
                        'msg': '查询失败'
                    },
                    status=200)

        else:
            return JsonResponse(
                {
                    'code': '400000',
                    'msg': '无效的token'
                },
                status=401)
    except Exception as e:
        body = {
            'code': '400002',
            'msg': "接口" + get_current_function_name() + "发生内部错误，并抛出异常" + str(e),
        }
        return JsonResponse(body, status=500)