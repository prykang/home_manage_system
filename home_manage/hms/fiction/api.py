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
            expected_key = {'name':''}
            query_data = dict.copy(expected_key)
            # print(request.data)
            query_data.update(request.data)
            parameter_body = {}
            for item in query_data:
                if item in expected_key.keys():
                    parameter_body[item + '__startswith'] = query_data[item]
                elif item in ['author'] and re.match(r'^[0-9]+$',str(query_data[item]).strip()):
                    # parameter_body[item+'_id'] = query_data[item]
                    parameter_body[item] = query_data[item]
                else:
                    pass
            if 'sort' in request.data and request.data['sort'] == '-id':
                data = FictionInfo.objects.filter(
                    **parameter_body
                    # module_id__module_name=expected_key['module_name'],   # 这个就是外键查询的方法
                ).order_by('-id')
            else:
                data = FictionInfo.objects.filter(
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
                data = FictionInfo.objects.filter(id=str(request.data['pk']).strip())
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
            # if 'valid_until' in request.data and request.data['valid_until'] == '':
            #     request.data.pop('valid_until')
            serializers = FictionInfoSerializer(data=request.data)
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



# 修改记录单元
@api_view(['POST'])
@csrf_exempt
def edit_item(request):
    try:
        if request.user.is_authenticated():
            request.data['mender'] = request.user.id
            if 'pk' in request.data and re.match(r'^[0-9]+$',str(request.data['pk']).strip()):
                bankcard_info = FictionInfo.objects.get(id=str(request.data['pk']).strip())
                serializers = FictionInfoSerializer(bankcard_info, data=request.data)
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
def delete_item(request):
    try:
        if  request.user.is_authenticated():
            print(request.data)
            if 'pks' in request.data:
                delete_list = []
                for item in request.data['pks']:
                    print(type(item))
                    if  re.match(r'^[0-9]+$', str(item).strip()):
                        data = FictionInfo.objects.filter(id=str(item).strip())
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


# 获取小说作者列表接口
@api_view(['POST'])
@csrf_exempt
def get_author_list(request):
    try:
        if  request.user.is_authenticated():
            data = Author.objects.all()
            if len(data):
                serialized_data = serialize('python', data,use_natural_foreign_keys=True)
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




# 添加记录单元
@api_view(['POST'])
@csrf_exempt
def add_author(request):
    try:
        if  request.user.is_authenticated():
            print("------------d-----------")
            print(request.data)
            print("------------d-----------")
            serializers = AuthorSerializer(data=request.data)
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



# 修改记录单元
@api_view(['POST'])
@csrf_exempt
def edit_fiction_type(request):
    try:
        if request.user.is_authenticated():
            if 'pk' in request.data and re.match(r'^[0-9]+$',str(request.data['pk']).strip()):
                bankcard_info = Author.objects.get(id=str(request.data['pk']).strip())
                serializers = AuthorSerializer(bankcard_info, data=request.data)
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
def delete_fiction_type(request):
    try:
        if  request.user.is_authenticated():
            print(request.data)
            if 'pks' in request.data:
                delete_list = []
                for item in request.data['pks']:
                    print(type(item))
                    if  re.match(r'^[0-9]+$', str(item).strip()):
                        data = Type.objects.filter(id=str(item).strip())
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


# 获取小说类型列表接口
@api_view(['POST'])
@csrf_exempt
def get_fiction_type_list(request):
    try:
        if  request.user.is_authenticated():
            data = Type.objects.all()
            if len(data):
                serialized_data = serialize('python', data,use_natural_foreign_keys=True)
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




# 添加记录单元
@api_view(['POST'])
@csrf_exempt
def add_fiction_type(request):
    try:
        if  request.user.is_authenticated():
            print("------------d-----------")
            print(request.data)
            print("------------d-----------")
            serializers = TypeSerializer(data=request.data)
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



# 修改记录单元
@api_view(['POST'])
@csrf_exempt
def edit_fiction_type(request):
    try:
        if request.user.is_authenticated():
            if 'pk' in request.data and re.match(r'^[0-9]+$',str(request.data['pk']).strip()):
                bankcard_info = Type.objects.get(id=str(request.data['pk']).strip())
                serializers = TypeSerializer(bankcard_info, data=request.data)
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
def delete_fiction_type(request):
    try:
        if  request.user.is_authenticated():
            print(request.data)
            if 'pks' in request.data:
                delete_list = []
                for item in request.data['pks']:
                    print(type(item))
                    if  re.match(r'^[0-9]+$', str(item).strip()):
                        data = Type.objects.filter(id=str(item).strip())
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


# 获取小说类型列表接口
@api_view(['POST'])
@csrf_exempt
def get_source_status_list(request):
    try:
        if  request.user.is_authenticated():
            data = SourceStatus.objects.all()
            if len(data):
                serialized_data = serialize('python', data,use_natural_foreign_keys=True)
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




# 获取资源列表接口
@api_view(['POST'])
@csrf_exempt
def get_source_list(request):
    try:
        if  request.user.is_authenticated():
            page_expected = {'page':'1','limit':'20'}
            page_expected.update(request.data)
            print("===============")
            print(request.data)
            expected_key = {'name':''}
            query_data = dict.copy(expected_key)
            # print(request.data)
            query_data.update(request.data)
            parameter_body = {}
            for item in query_data:
                if item in expected_key.keys():
                    parameter_body[item + '__startswith'] = query_data[item]
                elif item in ['status'] and re.match(r'^[0-9]+$',str(query_data[item]).strip()):
                    # parameter_body[item+'_id'] = query_data[item]
                    parameter_body[item] = query_data[item]
                else:
                    pass
            if 'sort' in request.data and request.data['sort'] == '-id':
                data = SourceInfo.objects.filter(
                    **parameter_body
                    # module_id__module_name=expected_key['module_name'],   # 这个就是外键查询的方法
                ).order_by('-id')
            else:
                data = SourceInfo.objects.filter(
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



# 获得资源记录单元
@api_view(['POST'])
@csrf_exempt
def get_source(request):
    try:
        if request.user.is_authenticated():
            if 'pk' in request.data and re.match(r'^[0-9]+$',str(request.data['pk']).strip()):
                data = SourceInfo.objects.filter(id=str(request.data['pk']).strip())
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



# 添加资源记录单元
@api_view(['POST'])
@csrf_exempt
def add_source(request):
    try:
        if  request.user.is_authenticated():
            request.data['creator'] = request.user.id
            request.data['mender'] = request.user.id
            print("------------d-----------")
            print(request.data)
            print("------------d-----------")
            # if 'valid_until' in request.data and request.data['valid_until'] == '':
            #     request.data.pop('valid_until')
            serializers = SourceInfoSerializer(data=request.data)
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



# 修改资源记录单元
@api_view(['POST'])
@csrf_exempt
def edit_source(request):
    try:
        if request.user.is_authenticated():
            request.data['mender'] = request.user.id
            if 'pk' in request.data and re.match(r'^[0-9]+$',str(request.data['pk']).strip()):
                bankcard_info = SourceInfo.objects.get(id=str(request.data['pk']).strip())
                serializers = SourceInfoSerializer(bankcard_info, data=request.data)
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


# 删除资源记录单元
@api_view(['POST'])
@csrf_exempt
def delete_source(request):
    try:
        if  request.user.is_authenticated():
            print(request.data)
            if 'pks' in request.data:
                delete_list = []
                for item in request.data['pks']:
                    print(type(item))
                    if  re.match(r'^[0-9]+$', str(item).strip()):
                        data = SourceInfo.objects.filter(id=str(item).strip())
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



# 开始处理录入的小说
@api_view(['POST'])
@csrf_exempt
def to_start_handle(request):
    # 根据已有资源搜索资源找到就停止
    # 根据资源逐个下载，只要有一个成功即可
    pass