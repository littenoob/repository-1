import axios, { AxiosRequestConfig, AxiosError } from 'axios';
import settings from '@/config/settings';
import baseURL from '@/config/baseURL'

let baseurl = baseURL
if (settings.useProxy) {
    baseurl = '/api'
}


const request = axios.create({
    baseURL: baseurl,
    timeout: 5000,
});

request.interceptors.request.use((config: AxiosRequestConfig) => {
    // 如果有一些接口需要认证才可以访问，就在这统一设置
    // const token = window.localStorage.getItem('token');
    // if (token)
    //     config.headers.Authorization = 'Bearer' + token;
    console.log(config)
    return config
}, (error: AxiosError) => {
    console.log('拦截请求错误：' + error)
}),
    request.interceptors.response.use((response) => { return response.data }, (error: AxiosError) => {
        console.log('拦截回复错误');
        if (error.response) {
            console.log(error.response.data)
        }

        // console.log(error.response.data.errors[Object.keys(error.response.data.errors)[0]][0]);
    })
request.get = (url, params, headers = {}): any => {
    return request({
        url,
        method: 'get',
        params,
        headers
    })
}
export default request