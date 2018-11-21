#-*- coding: UTF-8 -*-
# @Author  : countofdane
# @Email   : countofdane@163.com
# @Blog    ：https://blog.csdn.net/countofdane

import xlrd
from .common import *

from django.core.serializers import serialize
import re
import uuid
import os
import xlwt
from xlwt import XFStyle,Pattern,Style



class FileHandler(object):

    def __init__(self,path=''):
        self.path = path  # 生成或者读取的文件目录
        self.data_list = []  # 从文件或者数据库读取到的数据,
        self.ios_version = ''  # iOS 版本
        self.android_version = '' # Android 版本

    # def open_excel(self):
    #     try:
    #         data = xlrd.open_workbook(self.path)
    #         return {'flag':True,'data':data,'msg':'打开文件成功'}
    #     except Exception as e:
    #         print(str(e))
    #         return {'flag':False,'data':data,'msg':"函数"+ get_current_function_name() +"发生内部错误，并抛出异常"+ str(e)}
    #
    #
    #
    # #根据索引获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_index：表的索引
    # def get_excel_data(self,colnameindex=0,by_index=0):
    #     try:
    #         ret = self.open_excel()
    #         if ret['flag']:
    #             data = ret['data']
    #             table = data.sheets()[by_index]
    #             nrows = table.nrows #行数
    #             ncols = table.ncols #列数
    #
    #             print("===================")
    #             print(nrows)
    #             print(ncols)
    #             print("===================")
    #
    #             colnames =  table.row_values(colnameindex) #某一行数据
    #             data_list =[]
    #             for rownum in range(1,nrows):
    #                  row = table.row_values(rownum)
    #                  if row:
    #                      app = {}
    #                      for i in range(len(colnames)):
    #                         app[colnames[i]] = row[i]
    #                      data_list.append(app)
    #             self.data_list = data_list
    #             return {'flag':True,'list':data_list,'msg':'读取文件成功'}
    #         else:
    #             return {'flag': False, 'list': [],'msg':ret['msg']}
    #     except Exception as e:
    #         return {'flag':False,'list':[],'msg':"函数"+ get_current_function_name() +"发生内部错误，并抛出异常"+ str(e)}
    #
    #
    # def prase_excel_data(self):
    #     try:
    #         rsp = self.get_excel_data()
    #         if rsp['flag']:
    #             count = 1
    #             module_flag = submodule_flag = function_flag = ios_version_flag = android_version_flag = False
    #             msg = module_temp = submodule_temp = ios_version = android_version = function_temp = ''
    #             for row_value in rsp['list']:
    #                 print("1")
    #                 print("2")
    #                 for item in row_value:
    #                     print(item)
    #                 print(row_value['iOS版本'])
    #
    #                 if  ios_version_flag == False and android_version_flag == False and row_value['iOS版本'] =='' and row_value['Android版本'] =='':
    #                     # 有问题
    #                     msg = '监测到版本信息为空'
    #                     break
    #                 else:
    #                     if row_value['iOS版本']!='':
    #                         print("2")
    #                         print(row_value['iOS版本'])
    #                         self.ios_version = str(row_value['iOS版本']).strip()
    #                         ios_version_flag = True
    #                     if row_value['Android版本']!='':
    #                         self.android_version = str(row_value['Android版本']).strip()
    #                         android_version_flag = True
    #                 print("3")
    #                 if row_value['模块'] != '':
    #                     module_flag = True
    #                     submodule_flag = False
    #                     module_temp = row_value['模块']
    #                 elif  row_value['模块'] == ''  and  module_flag:
    #                     row_value['模块'] = module_temp
    #                 else:
    #                     #有问题
    #                     msg = '监测到第'+ str(count) +'行的模块字段为空'
    #                     break
    #                 if row_value['子模块'] != '':
    #                     submodule_flag = True
    #                     submodule_temp = row_value['子模块']
    #                 elif  row_value['子模块'] == ''  and  submodule_flag:
    #                     row_value['子模块'] = submodule_temp
    #                 else:
    #                     #有问题
    #                     msg = '监测到第' + str(count) + '行的子模块字段为空'
    #                     break
    #
    #                 if row_value['功能'] != '':
    #                     function_flag = True
    #                     function_temp = row_value['功能']
    #                 elif  row_value['功能'] == ''  and  function_flag:
    #                     row_value['功能'] = function_temp
    #                 else:
    #                     #有问题
    #                     msg = '监测到第' + str(count) + '行的功能字段为空'
    #                     break
    #                 if row_value['前提条件'] != '':
    #                     row_value['前提条件'] = row_value['前提条件'].replace('\u2028', '\n')
    #                 if row_value['备注'] != '':
    #                     row_value['备注'] = row_value['备注'].replace('\u2028', '\n')
    #                 if row_value['操作步骤'] == '':
    #                     msg = '监测到第' + str(count) + '行的操作步骤字段为空'
    #                     break
    #                 else:
    #                     row_value['操作步骤'] = row_value['操作步骤'].replace('\u2028', '\n')
    #                 if row_value['预期结果'] == '':
    #                     msg = '监测到第' + str(count) + '行的预期结果字段为空'
    #                     break
    #                 else:
    #                     row_value['预期结果'] = row_value['预期结果'].replace('\u2028', '\n')
    #                 if row_value['用例等级'] == '':
    #                     row_value['用例等级'] = '3'
    #                 else:
    #                     row_value['用例等级'] = str(int(row_value['用例等级']))
    #                 if row_value['标签'] != '':
    #                     row_value['标签'] = row_value['标签'].split('/')
    #                 else:
    #                     row_value['标签'] = []
    #                 if row_value['适用客户端'] == '':
    #                     row_value['适用客户端'] = 'ios/android'
    #                 split_data = row_value['适用客户端'].split('/')
    #                 for item in split_data:
    #                     if item.strip().lower() == 'ios':
    #                         if not ios_version_flag:
    #                             msg = '监测到第' + str(count) + '行用例适用iOS端，但是缺少必要的iOS版本信息'
    #                             break
    #                     if item.lower() == 'android':
    #                         if not android_version_flag:
    #                             msg = '监测到第' + str(count) + '行用例适用Android端，但是缺少必要的Android版本信息'
    #                             break
    #                 count += 1
    #             if count < len(rsp['list']):
    #                 ret = {'flag':False,'msg':msg}
    #             else:
    #                 ret = {'flag':True,'msg':'数据校验合格'}
    #         else:
    #             ret = {'flag': False, 'msg': rsp['msg']}
    #     except Exception as e:
    #         ret = {'flag': False, 'msg':"函数"+ get_current_function_name() +"发生内部错误，并抛出异常"+ str(e)}
    #     return ret
    #
    #
    # def save(self,user_id):
    #     # 处理版本
    #     version_list = []
    #     if self.ios_version != '':
    #         #创建 iOS 版本没有就创建，有就跳过
    #         # 先查询有没有
    #         ctid = Clienttype.objects.filter(client_type_name__icontains='ios')[0].id
    #         itv = Testversion.objects.filter(version__contains=self.ios_version,client_type=ctid)
    #         if not itv.exists():
    #             data = {}
    #             data['version'] = self.ios_version
    #             data['creator'] = data['mender'] = user_id
    #             data['client_type'] = ctid
    #             serializers = TestversionSerializer(data=data)
    #             if serializers.is_valid():
    #                 itv = serializers.save()
    #                 version_list.append(itv.id)
    #             else:
    #                 #保存失败返回
    #                 return {
    #                     'flag':False,
    #                     'data': serializers.errors,
    #                     'msg':'保存iOS版本信息:'+ self.ios_version +'失败'
    #                 }
    #         else:
    #             version_list.append(itv[0].pk)
    #     if self.android_version != '':
    #         #创建 Android 版本没有就创建，有就跳过
    #         # 先查询有没有
    #         ctid = Clienttype.objects.filter(client_type_name__icontains='android')[0].id
    #         atv = Testversion.objects.filter(version__contains=self.android_version, client_type=ctid)
    #         if not atv.exists():
    #             data = {}
    #             data['version'] = self.android_version
    #             data['creator'] = data['mender'] = user_id
    #             data['client_type'] = ctid
    #             serializers = TestversionSerializer(data=data)
    #             if serializers.is_valid():
    #                 atv = serializers.save()
    #                 # version_list.append(atv)
    #                 version_list.append(atv.id)
    #             else:
    #                 # 保存失败返回
    #                 return {
    #                     'flag': False,
    #                     'data': serializers.errors,
    #                     'msg': '保存Android版本信息:' + self.android_version + '失败'
    #                 }
    #         else:
    #             version_list.append(atv[0].pk)
    #     # 保存每条用例
    #     print(self.data_list)
    #     for item in self.data_list:
    #         print("smile:"+ str(item))
    #         #处理模块
    #         if item['模块'] != '':
    #             m = Module.objects.filter(module_name__contains=item['模块'])
    #             if not m.exists():
    #                 # 不存在就创建
    #                 module_data = {}
    #                 module_data['module_name'] = item['模块']
    #                 module_data['mender'] = user_id
    #                 module_data['creator'] = user_id
    #                 serializers = ModuleSerializer(data=module_data)
    #                 if serializers.is_valid():
    #                     m = serializers.save().id
    #                 else:
    #                     return {
    #                         'flag': False,
    #                         'data': serializers.errors,
    #                         'msg': '保存模块信息:' + item['模块'] + '失败'
    #                     }
    #             else:
    #                 m = m[0].pk
    #         #处理子模块
    #         if item['子模块'] != '':
    #             sm = Submodule.objects.filter(module__module_name__contains=item['模块'],sub_module_name__contains=item['子模块'])
    #             if not sm.exists():
    #                 #不存在就创建
    #                 submodule = {}
    #                 submodule['module'] = m
    #                 submodule['sub_module_name'] = item['子模块']
    #                 submodule['mender'] = user_id
    #                 submodule['creator'] = user_id
    #                 serializers = SubmoduleSerializer(data=submodule)
    #                 if serializers.is_valid():
    #                     sm = serializers.save().id
    #                 else:
    #                     return {
    #                         'flag': False,
    #                         'data': serializers.errors,
    #                         'msg': '保存子模块信息:' + item['子模块'] + '失败'
    #                     }
    #             else:
    #                 sm = sm[0].pk
    #         if item['标签'] != '':
    #             print("标签：----------")
    #             tg_list = []
    #             for tag in item['标签']:
    #                 print(tag)
    #                 tg = Tag.objects.filter(tag=tag)
    #                 if not tg.exists():
    #                     # 不存在就创建
    #                     tagdata = {}
    #                     tagdata['tag'] = tag
    #                     tagdata['mender'] = user_id
    #                     tagdata['creator'] = user_id
    #                     serializers = TagSerializer(data=tagdata)
    #                     if serializers.is_valid():
    #                         tg = serializers.save().id
    #                         # tg = serializers.save()
    #                         tg_list.append(tg)
    #                     else:
    #                         return {
    #                             'flag': False,
    #                             'data': serializers.errors,
    #                             'msg': '保存标签信息:' + tag + '失败'
    #                         }
    #                 else:
    #                     print("hello")
    #                     tg_list.append(tg[0].pk)
    #                     # tg_list.append(tg[0])
    #             item['标签'] = tg_list
    #         else:
    #             item['标签'] = []
    #         #处理用例
    #         query_data = {}
    #         data = {}
    #         vt_data = {}
    #         data['creator']  = user_id
    #         data['mender'] = user_id
    #         data['owner'] = user_id
    #         data['module'] = query_data['module'] = m
    #         data['sub_module'] = query_data['sub_module'] = sm
    #         data['function'] = query_data['function'] = item['功能']
    #         data['precondition'] = query_data['precondition'] = item['前提条件']
    #         data['operation_steps'] = query_data['operation_steps'] = item['操作步骤']
    #         data['expected'] = query_data['expected'] = item['预期结果']
    #         data['tags'] =  item['标签']
    #         data['level'] = Level.objects.filter(level__icontains=item['用例等级'])[0].id
    #         serializers = TestcaseSerializer(data=data)
    #         print(data['tags'])
    #         if serializers.is_valid():
    #             print("fuck!")
    #             # 校验这几个输入是合法的之后，需要自己主动查询一下是否已经存在这样的用例了，因为 text 不能作为主键来防止插入重复数据
    #             tc = Testcase.objects.filter(**query_data)
    #             if not tc.exists():
    #                 # 创建新的用例
    #                 tc = serializers.save()
    #                 vt_data['testcase'] = tc.id
    #                 # data['testcase'] = tc
    #             else:
    #                 vt_data['testcase'] = tc[0].pk
    #
    #
    #             print("+++++++++++++++++++++++++++")
    #             print(version_list)
    #             print("+++++++++++++++++++++++++++")
    #
    #             for version in version_list:
    #                 vt_data['version'] = version
    #                 #先校验是否存在
    #                 vt = Versiontestcase.objects.filter(testcase=vt_data['testcase'],version=vt_data['version'])
    #                 if not vt.exists():
    #                     print(data)
    #                     serializers = VersiontestcaseSerializer(data=vt_data)
    #                     if serializers.is_valid():
    #                         serializers.save()
    #                     else:
    #                         return {
    #                             'flag': False,
    #                             'data': serializers.errors,
    #                             'msg': '保存版本用例失败'
    #                         }
    #         else:
    #             return {
    #                 'flag': False,
    #                 'data': serializers.errors,
    #                 'msg': '保存用例失败'
    #             }
    #     # 成功处理所有的保存
    #     for version in version_list:
    #         count_module(version)
    #         count_testcase(version)
    #     return {
    #         'flag': True,
    #         'msg': '保存表格数据成功'
    #     }
    #
    # # 根据 version module 生成用例文件
    # def generate_file(self,query_data):
    #     try:
    #         parameter_body = {}
    #         for item in query_data:
    #             if item in ['module']:
    #                 if query_data[item] == 'all':
    #                     query_data[item] = ''
    #             if item in ['version', 'module'] and re.match(r'^[0-9]+$', str(query_data[item]).strip()):
    #                 parameter_body[item + '_id'] = str(query_data[item]).strip()
    #         data = Versiontestcase.objects.filter(
    #             **parameter_body
    #         ).order_by('testcase__module_id', 'testcase__sub_module_id')
    #         if data.exists():
    #             # todo 这个地方开始效率太低，暂时这样实现，后续优化  -- start
    #             # 主要原因是没有找到更好的实现返回键值 key-value 的更好方法,使用已知的快方法返回的是列表，前后端维护成本高
    #             items = []
    #             for item in data:
    #                 temp = {}
    #                 temp['pk'] = item.id
    #                 tc = Testcase.objects.filter(id=item.testcase.id)
    #                 vs = Testversion.objects.filter(id=item.version.id)
    #                 temp.update(serialize('python', vs, use_natural_foreign_keys=True)[0]['fields'])
    #                 temp.update(serialize('python', tc, use_natural_foreign_keys=True)[0]['fields'])
    #                 items.append(temp)
    #             # todo 这个地方开始效率太低，暂时这样实现，后续优化  -- end
    #             self.data_list = items
    #             # 需要考虑处理文件重名的考虑
    #             tv = Testversion.objects.filter(id=query_data['version'])
    #             if tv.exists():
    #                 file_name = str(uuid.uuid1()).replace('-', '') + '-' + str(tv[0].client_type) + '-' + str(tv[0].version)+'.xlsx'
    #                 file_path = os.path.join('./files/download',file_name)
    #                 self.path = file_path
    #                 # 写入表头
    #                 workbook = xlwt.Workbook()
    #                 sheet = workbook.add_sheet('用例', cell_overwrite_ok=True)
    #                 sheet.col(3).width=256*20
    #                 sheet.col(4).width=256*30
    #                 sheet.col(5).width=256*30
    #                 style = XFStyle()
    #                 pattern = Pattern()
    #                 pattern.pattern = Pattern.SOLID_PATTERN
    #                 pattern.pattern_fore_colour = Style.colour_map['gray_ega']  # 设置单元格背景色为黄色
    #                 style.pattern = pattern
    #
    #                 alignment = xlwt.Alignment()
    #                 alignment.horz = xlwt.Alignment.HORZ_CENTER
    #                 alignment.vert = xlwt.Alignment.VERT_CENTER
    #                 style.alignment = alignment
    #
    #                 # -----------------------------------------
    #
    #                 sheet.write_merge(0, 0, 0, 9, file_name)
    #                 colum_name = ['模块','子模块','功能','前提条件','操作步骤','预期结果','适用客户端','用例等级','标签','备注']
    #                 colum_index  = ['module','sub_module','function','precondition','operation_steps','expected','client_type','level','tags','remark']
    #                 for index in range(len(colum_name)):
    #                     sheet.write(1, index, colum_name[index],style)
    #                 # 创建文件并把数据写入
    #                 # row  = 2
    #                 style2 = XFStyle()
    #                 alignment2 = xlwt.Alignment()
    #                 alignment2.wrap = xlwt.Alignment.WRAP_AT_RIGHT
    #                 style2.alignment = alignment2
    #                 for row in range(len(items)):
    #                     for col in range(len(colum_name)):
    #                         if colum_index[col] == 'tags':
    #                             sheet.write(2 + row, col, '/'.join(items[row][colum_index[col]]),style2)
    #                         elif colum_index[col] == 'level':
    #                             sheet.write(2 + row, col, items[row][colum_index[col]][0])
    #                         elif colum_index[col] == 'remark':
    #                             pass
    #                         else:
    #                             print(items[row][colum_index[col]])
    #                             sheet.write(2 + row, col, items[row][colum_index[col]],style2)
    #                 workbook.save(file_path)
    #                 ret = {'flag': True, 'filename': file_name, 'msg': '生成测试用例文档成功'}#'items': items
    #             else:
    #                 ret = {'flag': False, 'msg': '没有查询到符合条件的数据'}
    #         else:
    #             ret = {'flag':False,'msg':'没有查询到符合条件的数据'}
    #     except Exception as e:
    #         ret = {'flag': False, 'msg': "函数" + get_current_function_name() + "发生内部错误，并抛出异常" + str(e)}
    #     return ret





# def main():
#    tables = excel_table_byindex()
#    for row in tables:
#        print(row)
#
#
#
# if __name__=="__main__":
#     main()