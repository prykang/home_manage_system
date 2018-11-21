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
# 如何让返回的提示信息更具体一点？比如用户已经存在了---》修改底层提示语即可 在相应的models 文件中修改
# 注册接口
@api_view(['POST'])
@csrf_exempt
def registe(request):
    try:
        if request.method == 'POST':
            serializers = UserSerializer(data=request.data)
            if serializers.is_valid():
                serializers.save()
                create_data = {}
                user = User.objects.filter(username=request.data['username'])
                create_data['owner'] = user[0].id
                create_data['sys_auth'] = request.data['sys_auth'] if 'sys_auth' in request.data else ''
                create_data['testcase_auth'] = request.data['testcase_auth'] if 'testcase_auth' in request.data else ''
                serializers = AuthoritycontrolSerializer(data=create_data)
                if serializers.is_valid():
                    serializers.save()
                    return JsonResponse(
                        {
                            'data':serializers.data,
                            'code':'000000',
                            'msg':'创建用户成功！'
                        },
                        status=201)
                else:
                    return JsonResponse(
                        {
                            'data': serializers.errors,
                            'code': '400001',
                            'msg': '接口' + get_current_function_name() + '入参校验失败!'
                        },
                        status=400)
            else:
                return JsonResponse(
                    {
                        'data':serializers.errors,
                        'code':'400001',
                        'msg':'接口'+ get_current_function_name() +'入参校验失败!'
                    },
                    status=400)
    except Exception as e:
        body = {
            'code':'400002',
            'msg':"接口"+ get_current_function_name() +"发生内部错误，并抛出异常"+ str(e),
        }
        return  JsonResponse(body, status=500)



# 登录接口
@api_view(['POST'])
@csrf_exempt
def login(request):
    try:
        if request.method == 'POST':
            if 'username' in request.data:
                username = request.data['username'] #身份证号
                if 'password' in request.data:
                    password = request.data['password']
                    user = authenticate(username=username,password=password)
                    if user is not None:
                        if user.is_active:
                            try:
                                token = Token.objects.get(user=user)
                            except Token.DoesNotExist:
                                token = Token.objects.create(user=user)
                            return JsonResponse(
                                {
                                    'token':'Token ' + str(token),
                                    'code':'000000',
                                    'msg':'登录成功！'
                                },
                                status=200)
                    else:
                        return JsonResponse(
                            {
                                'code':'400001',
                                'msg':'账号或者密码错误'
                            },
                            status=200)
                else:
                    return JsonResponse(
                        {
                            'data':{
                              'password':'This field is required.'
                            },
                            'code': '400003',
                            'msg': '登录失败'
                        },
                        status=200)
            else:
                return JsonResponse(
                    {
                        'data': {
                            'username': 'This field is required.'
                        },
                        'code': '400004',
                        'msg': '登录失败'
                    },
                    status=200)
    except Exception as e:
        body = {
            'code':'400002',
            'msg':"接口"+ get_current_function_name() +"发生内部错误，并抛出异常"+ str(e),
        }
        return  JsonResponse(body, status=500)




# 登出接口
@api_view(['POST'])
@csrf_exempt
def get_userinfo(request):
    try:
        if  request.user.is_authenticated():
            try:
                print(request.user.id)
                authdata = Authoritycontrol.objects.get(owner=request.user.id)
            except Authoritycontrol.DoesNotExist:
                roles = ['normal']
            else:
                if authdata.sys_auth != '':
                    roles = ['admin']
                else:
                    roles = ['normal']
            return JsonResponse(
                {
                    'name':str(request.user),
                    'roles': roles,
                    'avatar':'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',
                    'introduction': '我是超级管理员',
                    'code': '000000',
                    'msg': '查询成功！'
                },
                status=200)

    except Exception as e:
        print(str(e))
        body = {
            'code':'400002',
            'msg':"接口"+ get_current_function_name() +"发生内部错误，并抛出异常"+ str(e),
        }
        return  JsonResponse(body, status=500)


# 用户列表
@api_view(['POST'])
@csrf_exempt
def get_user_list(request):
    try:
        if  request.user.is_authenticated():
            data = User.objects.all()
            serialized_data = serialize('python', data, use_natural_foreign_keys=True,fields=('username'))
            return JsonResponse(
                {
                    'data': {
                        'items': serialized_data,
                        'total': len(serialized_data)
                    },
                    'code': '000000',
                    'msg': '查询测试客户端类型成功'
                },
                status=200)
    except Exception as e:
        print(str(e))
        body = {
            'code':'400002',
            'msg':"接口"+ get_current_function_name() +"发生内部错误，并抛出异常"+ str(e),
        }
        return  JsonResponse(body, status=500)

# 登出接口
@api_view(['POST'])
@csrf_exempt
def logout(request):
    try:
        if  request.user.is_authenticated():
            Token.objects.get(user=request.user).delete()
            return JsonResponse(
                {
                    'code': '000000',
                    'msg': '登出成功！'
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
        print(str(e))
        body = {
            'code':'400002',
            'msg':"接口"+ get_current_function_name() +"发生内部错误，并抛出异常"+ str(e),
        }
        return  JsonResponse(body, status=500)




# 添加用例权限
@api_view(['POST'])
@csrf_exempt
def add_testcase_auth(request):
    pass


# 添加平台权限
@api_view(['POST'])
@csrf_exempt
def add_sys_auth(request):
    pass

