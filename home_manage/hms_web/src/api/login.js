import request from '@/utils/request'

export function loginByUsername(username, password) {
  const data = {
    username,
    password
  }
  return request({
    url: '/account/api/login',
    method: 'post',
    type: 'application/json',
    data
  })
}

export function logout() {
  return request({
    url: '/account/api/logout',
    method: 'post'
  })
}

export function getUserInfo() {
  return request({
    url: '/account/api/get_userinfo',
    method: 'post'
    // params: { token }
  })
}

export function getUserList() {
  return request({
    url: '/account/api/get_user_list',
    method: 'post'
    // params: { token }
  })
}
// get 接口请求
// export function getUserInfo(token) {
//   return request({
//     url: '/user/info',
//     method: 'get',
//     params: { token }
//   })
// }
