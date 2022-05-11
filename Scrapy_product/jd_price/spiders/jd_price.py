# -*- coding: utf-8 -*-
"""
@Time ： 2022/4/20 15:03
@Author ： jiafei
@email ： 1723957366@qq.com
@File ：jd_price.py
@feature：获取京东价格
"""
import requests
from lxml import etree
from datetime import datetime
import asyncio

from db_change import Aiomysql_DbHelper

dbHelper = Aiomysql_DbHelper(host='localhost', user='root', pwd='123456789', db='product_information')

fetch_format = 'https://search.jd.com/s_new.php?psort=3&keyword={}'
cookies = {
    'ipLoc-djd': '1-72-2799-0',
}

headers = {
    'referer': 'https://search.jd.com/Search?keyword=k40s&suggest=1.his.0.0&wq=k40s&pvid=520b616c26fb40a28a6f8fba07edf10e&psort=3&click=0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
    # 'Cookie': 'ipLoc-djd=1-72-2799-0',
}
# a = '小米'
# response = requests.get(fetch_format.format('redmik40'), headers=headers, cookies=cookies)
# with open('./jd.html','w') as f:
#     f.write(response.text)
# class="gl-i-wrap"
async def main():
    dict_phone = await dbHelper.fetch("select brand,type from phone")
    for item in dict_phone:
        type = item['type'].split('（')[0].lower()
        response = requests.get(fetch_format.format(type), headers=headers, cookies=cookies)
        jd_html = etree.HTML(response.text)
        price_divList = jd_html.xpath('//div[@class="gl-i-wrap"]')
        price_list = [int(price_div.xpath('./div[@class="p-price"]/strong/i/text()')[0].split('.')[0])
                     for price_div in price_divList
                     if type in price_div.xpath('./div[@class="p-name p-name-type-2"]/a/em/text()')[0].lower() or
                     type in price_div.xpath('./div[@class="p-name p-name-type-2"]/a/i/text()')[0].lower()]
        if price_list == []:
            continue
        price = min(price_list)
        sql = "INSERT INTO {} (brand,price,price_date) VALUES (%s, %s, %s);".format(item['brand'])
        now = datetime.now()
        await dbHelper.fetch(sql=sql,data=[type,price,datetime(now.year,now.month,now.day)])

if __name__ == '__main__':
    asyncio.run(main())