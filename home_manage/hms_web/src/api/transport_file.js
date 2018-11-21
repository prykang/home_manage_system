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
