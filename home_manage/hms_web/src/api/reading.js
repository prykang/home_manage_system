
import request from '@/utils/request'

export function getList(data) {
  return request({
    url: 'reading/api/get_list',
    method: 'post',
    data
  })
}

export function getItem(data) {
  return request({
    url: 'reading/api/get_item',
    method: 'post',
    data
  })
}

export function editItem(data) {
  return request({
    url: 'reading/api/edit_item',
    method: 'post',
    data
  })
}

export function addItem(data) {
  return request({
    url: 'reading/api/add_item',
    method: 'post',
    data
  })
}

export function deleteItems(data) {
  return request({
    url: 'reading/api/delete_items',
    method: 'post',
    data
  })
}

export function getBookList(data) {
  return request({
    url: 'reading/api/get_book_list',
    method: 'post',
    data
  })
}

export function addBook(data) {
  return request({
    url: 'reading/api/add_book',
    method: 'post',
    data
  })
}

export function editBook(data) {
  return request({
    url: 'reading/api/edit_book',
    method: 'post',
    data
  })
}

export function deleteBook(data) {
  return request({
    url: 'reading/api/delete_book',
    method: 'post',
    data
  })
}

export function addAuthor(data) {
  return request({
    url: 'reading/api/add_author',
    method: 'post',
    data
  })
}

export function getAuthorList(data) {
  return request({
    url: 'reading/api/get_author_list',
    method: 'post',
    data
  })
}

export function addCountry(data) {
  return request({
    url: 'reading/api/add_country',
    method: 'post',
    data
  })
}

export function getCountryList(data) {
  return request({
    url: 'reading/api/get_country_list',
    method: 'post',
    data
  })
}
