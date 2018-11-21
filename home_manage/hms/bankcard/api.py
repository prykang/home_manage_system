
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
import re
from django.core.paginator import Paginator

# 获取列表接口
@api_view(['POST'])
@csrf_exempt
def get_list(request):
    try:
        if  request.user.is_authenticated():
            page_expected = {'page':'1','limit':'20'}
            page_expected.update(request.data)
            print("===============")
            print(request.data)
            expected_key = {'bankcard_num':''}
            query_data = dict.copy(expected_key)
            # print(request.data)
            query_data.update(request.data)
            parameter_body = {}
            for item in query_data:
                if item in expected_key.keys():
                    parameter_body[item + '__startswith'] = query_data[item]
                elif item in ['bankcard_type','bank','creator'] and re.match(r'^[0-9]+$',str(query_data[item]).strip()):
                    # parameter_body[item+'_id'] = query_data[item]
                    parameter_body[item] = query_data[item]
                else:
                    pass
            if 'sort' in request.data and request.data['sort'] == '-id':
                data = BankCardInfo.objects.filter(
                    **parameter_body
                    # module_id__module_name=expected_key['module_name'],   # 这个就是外键查询的方法
                ).order_by('-id')
            else:
                data = BankCardInfo.objects.filter(
                    **parameter_body
                    # module_id__module_name=expected_key['module_name'],   # 这个就是外键查询的方法
                )
            if data.exists():
                p = Paginator(data, int(page_expected['limit']))
                page_data = p.page(int(page_expected['page']))
                serialized_data = serialize('python', page_data,use_natural_foreign_keys=True)
                print(serialized_data)
                return JsonResponse(
                    {
                        'data': {
                            'items':serialized_data,
                            'total':len(data)
                        },
                        'code': '000000',
                        'msg': '查询列表成功'
                    },
                    status=200)
            else:
                return JsonResponse(
                    {
                        'data':'',
                        'code': '400001',
                        'msg': '没有查询到符合条件的数据'
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
            'code':'400002',
            'msg':"接口"+ get_current_function_name() +"发生内部错误，并抛出异常"+ str(e),
        }
        return  JsonResponse(body, status=500)



# 获得记录单元
@api_view(['POST'])
@csrf_exempt
def get_item(request):
    try:
        if request.user.is_authenticated():
            if 'pk' in request.data and re.match(r'^[0-9]+$',str(request.data['pk']).strip()):
                data = BankCardInfo.objects.filter(id=str(request.data['pk']).strip())
                if data.exists():
                    serialized_data = serialize('python', data, use_natural_foreign_keys=False)
                    # serialized_data[0]['fields']['id'] = serialized_data[0]['pk']
                    return JsonResponse(
                        {
                            'data': serialized_data[0],
                            'code': '000000',
                            'msg': '查询成功'
                        },
                        status=200)
                else:
                    return JsonResponse(
                        {
                            'data': '',
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



# 添加记录单元
@api_view(['POST'])
@csrf_exempt
def add_item(request):
    try:
        if  request.user.is_authenticated():
            request.data['creator'] = request.user.id
            request.data['mender'] = request.user.id
            print("------------d-----------")
            print(request.data)
            print("------------d-----------")
            if 'valid_until' in request.data and request.data['valid_until'] == '':
                request.data.pop('valid_until')
            serializers = BankCardInfoSerializer(data=request.data)
            if serializers.is_valid():
                serializers.save()
                return JsonResponse(
                    {
                        'data': serializers.data,
                        'code': '000000',
                        'msg': '新增成功'
                    },
                    status=200)
            else:
                return JsonResponse(
                    {
                        'data':serializers.errors,
                        'code': '400001',
                        'msg': '新增失败'
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
            'code':'400002',
            'msg':"接口"+ get_current_function_name() +"发生内部错误，并抛出异常"+ str(e),
        }
        return  JsonResponse(body, status=500)
#-*- coding: UTF-8 -*-
# @Author  : countofdane
# @Email   : countofdane@163.com
# @Blog    ：https://blog.csdn.net/countofdane


# 修改记录单元
@api_view(['POST'])
@csrf_exempt
def edit_item(request):
    try:
        if request.user.is_authenticated():
            request.data['mender'] = request.user.id
            if 'pk' in request.data and re.match(r'^[0-9]+$',str(request.data['pk']).strip()):
                bankcard_info = BankCardInfo.objects.get(id=str(request.data['pk']).strip())
                serializers = BankCardInfoSerializer(bankcard_info, data=request.data)
                if serializers.is_valid():
                    serializers.save()
                    return JsonResponse(
                        {
                            'data': serializers.data,
                            'code': '000000',
                            'msg': '修改成功'
                        },
                        status=200)
                else:
                    return JsonResponse(
                        {
                            'data': serializers.errors,
                            'code': '400001',
                            'msg': '修改失败'
                        },
                        status=200)
            else:
                return JsonResponse(
                    {
                        'data': {
                            'pk': 'This field is required.'
                        },
                        'code': '400001',
                        'msg': '修改失败'
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


# 删除记录单元
@api_view(['POST'])
@csrf_exempt
def delete_items(request):
    try:
        if  request.user.is_authenticated():
            print(request.data)
            if 'pks' in request.data:
                delete_list = []
                for item in request.data['pks']:
                    print(type(item))
                    if  re.match(r'^[0-9]+$', str(item).strip()):
                        data = BankCardInfo.objects.filter(id=str(item).strip())
                        if data.exists():
                            ret = data[0].delete()
                            if len(ret) > 0:
                                delete_list.append(ret[0])
                if len(delete_list) == len(request.data['pks']):
                    return JsonResponse(
                        {
                            'code': '000000',
                            'msg': '删除成功'
                        },
                        status=200)
                elif len(delete_list) < len(request.data['pks']) and len(delete_list) > 0:
                    return JsonResponse(
                        {
                            'data':{
                                'delete_count': len(delete_list)
                            },
                            'code': '400001',
                            'msg': '删除部分成功'
                        },
                        status=200)
                else:
                    return JsonResponse(
                        {
                            'code': '400001',
                            'msg': '对象不存在'
                        },
                        status=200)
            else:
                return JsonResponse(
                    {
                        'data': {
                            'pks': 'This field is required.'
                        },
                        'code': '400001',
                        'msg': '删除失败'
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
            'code':'400002',
            'msg':"接口"+ get_current_function_name() +"发生内部错误，并抛出异常"+ str(e),
        }
        return  JsonResponse(body, status=500)



# 获取银行卡类型列表
@api_view(['POST'])
@csrf_exempt
def get_bankcard_type_list(request):
    try:
        if  request.user.is_authenticated():
            data = BankCardType.objects.all()
            if data.exists():
                serialized_data = serialize('python', data,use_natural_foreign_keys=True)
                return JsonResponse(
                    {
                        'data': {
                            'items':serialized_data,
                            'total':len(serialized_data)
                        },
                        'code': '000000',
                        'msg': '查询银行卡类型成功'
                    },
                    status=200)
            else:
                return JsonResponse(
                    {
                        'code': '400001',
                        'msg': '查询银行卡类型为空'
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
            'code':'400002',
            'msg':"接口"+ get_current_function_name() +"发生内部错误，并抛出异常"+ str(e),
        }
        print(body)
        return  JsonResponse(body, status=500)



# 获取银行列表
@api_view(['POST'])
@csrf_exempt
def get_bank_list(request):
    try:
        if  request.user.is_authenticated():
            data = Bank.objects.all()
            if data.exists():
                serialized_data = serialize('python', data,use_natural_foreign_keys=True)
                return JsonResponse(
                    {
                        'data': {
                            'items':serialized_data,
                            'total':len(serialized_data)
                        },
                        'code': '000000',
                        'msg': '查询银行列表成功'
                    },
                    status=200)
            else:
                return JsonResponse(
                    {
                        'code': '400001',
                        'msg': '查询银行列表为空'
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
            'code':'400002',
            'msg':"接口"+ get_current_function_name() +"发生内部错误，并抛出异常"+ str(e),
        }
        print(body)
        return  JsonResponse(body, status=500)
