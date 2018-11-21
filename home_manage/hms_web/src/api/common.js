import request from '@/utils/request'

// # 获取测试用例客户端种类 -- 返回所有
// # 条件：无
export function getClientType(data) {
  return request({
    url: 'bankcard/api/get_client_type_list',
    method: 'post',
    data
  })
}

// # 获取测试用例版本列表 -- 返回所有
// # 条件：测试用例客户端类型
export function getVersionOptions(data) {
  return request({
    url: 'bankcard/api/get_testversion_operation_list',
    method: 'post',
    data
  })
}

// # 获取测试用例模块 -- 返回所有
// # 条件：无
export function getModuleOptions(data) {
  return request({
    url: 'bankcard/api/get_module_list',
    method: 'post',
    data
  })
}

// # 获取测试用例子模块 -- 返回所有
// # 条件：模块
export function getSubModuleOptions(data) {
  return request({
    url: 'bankcard/api/get_submodule_list',
    method: 'post',
    data
  })
}

// # 获取测试用例等级 -- 返回所有
// # 条件：无
export function getLevelOptions(data) {
  return request({
    url: 'bankcard/api/get_level_list',
    method: 'post',
    data
  })
}

// # 获取测试用例标签 -- 返回所有
// # 条件 无
export function getTagOptions(data) {
  return request({
    url: 'bankcard/api/get_tag_list',
    method: 'post',
    data
  })
}

// # 过滤模块 -- 返回所有
// # 条件 用例版本
export function filterModuleOptions(data) {
  return request({
    url: 'bankcard/api/filter_modules',
    method: 'post',
    data
  })
}

// # 查询阶段 -- 返回所有
// # 条件 无
export function getStageOptions(data) {
  return request({
    url: 'bankcard/api/get_stage_list',
    method: 'post',
    data
  })
}

// # 查询阶段 -- 返回所有
// # 条件 无
export function getexecuteTypeOptions(data) {
  return request({
    url: 'bankcard/api/get_executetype_list',
    method: 'post',
    data
  })
}

