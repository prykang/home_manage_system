import request from '@/utils/request'

// # 获取测试用例客户端种类 -- 返回所有
// # 条件：无
export function parseFile(data) {
  return request({
    url: '/filemanager/api/parse_file',
    method: 'post',
    data
  })
}

export function generateTestcaseFile(data) {
  return request({
    url: 'filemanager/api/generate_testcase',
    method: 'post',
    data
  })
}

