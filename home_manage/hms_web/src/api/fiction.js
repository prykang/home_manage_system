import request from '@/utils/request'
export function getList(data) {
  return request({
    url: 'fiction/api/get_list',
    method: 'post',
    data
  })
}

export function getItem(data) {
  return request({
    url: 'fiction/api/get_item',
    method: 'post',
    data
  })
}

export function editItem(data) {
  return request({
    url: 'fiction/api/edit_item',
    method: 'post',
    data
  })
}

export function addItem(data) {
  return request({
    url: 'fiction/api/add_item',
    method: 'post',
    data
  })
}

export function deleteItems(data) {
  return request({
    url: 'fiction/api/delete_items',
    method: 'post',
    data
  })
}

export function getFictionType(data) {
  return request({
    url: 'fiction/api/get_fiction_type_list',
    method: 'post',
    data
  })
}

export function addFictionType(data) {
  return request({
    url: 'fiction/api/add_fiction_type',
    method: 'post',
    data
  })
}

export function addAuthor(data) {
  return request({
    url: 'fiction/api/add_author',
    method: 'post',
    data
  })
}

export function getAuthorList(data) {
  return request({
    url: 'fiction/api/get_author_list',
    method: 'post',
    data
  })
}

export function startSearchDownload(data) {
  return request({
    url: 'fiction/api/start_search_and_download',
    method: 'post',
    data
  })
}
