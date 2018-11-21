import request from '@/utils/request'
/* 资源相关的接口*/
export function getSourceStatusList(data) {
  return request({
    url: 'fiction/api/get_source_status_list',
    method: 'post',
    data
  })
}

export function getList(data) {
  return request({
    url: 'fiction/api/get_source_list',
    method: 'post',
    data
  })
}

export function addItem(data) {
  return request({
    url: 'fiction/api/add_source',
    method: 'post',
    data
  })
}

export function editItem(data) {
  return request({
    url: 'fiction/api/edit_source',
    method: 'post',
    data
  })
}

export function getItem(data) {
  return request({
    url: 'fiction/api/get_source',
    method: 'post',
    data
  })
}

export function deleteItems(data) {
  return request({
    url: 'fiction/api/delete_source',
    method: 'post',
    data
  })
}
