# -*- coding: utf-8 -*-
"""
@Time ： 2022/4/8 0:36
@Author ： jiafei
@email ： 1723957366@qq.com
@File ：zol_phoneType.py
@feature：获取中关村手机型号到数据库
@source：
"""

import aiohttp
import asyncio
from lxml import etree
from db_change import Aiomysql_DbHelper

cookies = {
    'v4_compare_57': '1366979',
    'ip_ck': '4sSA7//0j7QuNTMxODUzLjE2NDk0OTUyOTQ%3D',
    'realLocationId': '9',
    'userFidLocationId': '9',
    'Hm_lvt_ae5edc2bc4fc71370807f6187f0a2dd0': '1649495294,1649575847',
    'listSubcateId': '57',
    'Adshow': '0',
    'z_day': 'icnmo11564=1&ixgo20=1&rdetail=3',
    'lv': '1649583257',
    'vn': '5',
    'questionnaire_pv': '1649548822',
    'Hm_lpvt_ae5edc2bc4fc71370807f6187f0a2dd0': '1649583259',
    'z_pro_city': 's_provice%3Dguangdong%26s_city%3Dguangzhou',
}

headers = {
    'authority': 'top.zol.com.cn',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'v4_compare_57=1366979; ip_ck=4sSA7//0j7QuNTMxODUzLjE2NDk0OTUyOTQ%3D; realLocationId=9; userFidLocationId=9; Hm_lvt_ae5edc2bc4fc71370807f6187f0a2dd0=1649495294,1649575847; listSubcateId=57; Adshow=0; z_day=icnmo11564=1&ixgo20=1&rdetail=3; lv=1649583257; vn=5; questionnaire_pv=1649548822; Hm_lpvt_ae5edc2bc4fc71370807f6187f0a2dd0=1649583259; z_pro_city=s_provice%3Dguangdong%26s_city%3Dguangzhou',
    'pragma': 'no-cache',
    'referer': 'https://top.zol.com.cn/compositor/57/manu_98.html',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
}


url_format = 'https://top.zol.com.cn/compositor/57/manu_{}.html'
arr = ['1795', '1673', '613', '544', '55731', '50840', '55075', '34645', '55535', '98']
brands = ['vivo', 'oppo', 'huawei', 'iphone', 'redmi', 'honour', 'iqoo', 'xiaomi', 'realme', 'samsung', 'meizu',
          'oneplus']
dict_phoneType = {'vivo': 'vivo', 'OPPO': 'oppo', '华为': 'huawei', '苹果': 'iphone', '荣耀': 'honour', '小米': 'xiaomi', '红米': 'redmi',
        'realme': 'realme', '三星': 'samsung', '魅族': 'meizu', '一加': 'oneplus', 'iQOO': 'iqoo'}
dbHelper = Aiomysql_DbHelper(host='localhost', user='root', pwd='123456789', db='product_information')

'class="rank-list"' 'class="rank-list__item clearfix"'


async def fetch_data(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, cookies=cookies) as res:
            if int(res.status) != 200:
                print('状态码出错')
                return 'err'
            result = await res.text()
            return result


async def insert(data: list, tablename: str) -> int:
    inset_sql = "INSERT IGNORE INTO {} (brand, type) VALUES (%s, %s);".format(tablename)
    result = await dbHelper.fetch(sql=inset_sql, data=data, excutemany=1)
    print(f'插入了{result}条数据')
    return result


def get_list(text: str, brand: str) -> list:
    html = etree.HTML(text)
    types = html.xpath('//div[@class="rank__name"]/a/text()')
    return [[brand, phone_type] for phone_type in types]


async def handle(index: str, id: str):
    brand = brands[index]
    text = await fetch_data(url_format.format(id))
    await insert(get_list(text, brand), 'phone')


async def main():
    await asyncio.gather(*[handle(index, id) for index, id in enumerate(arr)])


if __name__ == '__main__':
    asyncio.run(main())
