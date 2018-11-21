import request from '@/utils/request'

export function getList(data) {
  return request({
    url: 'bankcard/api/get_list',
    method: 'post',
    data
  })
}

export function getItem(data) {
  return request({
    url: 'bankcard/api/get_item',
    method: 'post',
    data
  })
}

export function editItem(data) {
  return request({
    url: 'bankcard/api/edit_item',
    method: 'post',
    data
  })
}

export function addItem(data) {
  return request({
    url: 'bankcard/api/add_item',
    method: 'post',
    data
  })
}

export function deleteItems(data) {
  return request({
    url: 'bankcard/api/delete_items',
    method: 'post',
    data
  })
}

export function getBankCardType(data) {
  return request({
    url: 'bankcard/api/get_bankcard_type_list',
    method: 'post',
    data
  })
}

export function getBankList(data) {
  return request({
    url: 'bankcard/api/get_bank_list',
    method: 'post',
    data
  })
}

export function addBank(data) {
  return request({
    url: 'bankcard/api/add_bank',
    method: 'post',
    data
  })
}

