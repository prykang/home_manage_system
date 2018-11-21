
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
    pass



# 获得记录单元
@api_view(['POST'])
@csrf_exempt
def get_item(request):
    pass



# 添加记录单元
@api_view(['POST'])
@csrf_exempt
def add_item(request):
    pass



# 修改记录单元
@api_view(['POST'])
@csrf_exempt
def edit_item(request):
    pass


# 删除记录单元
@api_view(['POST'])
@csrf_exempt
def delete_item(request):
    pass