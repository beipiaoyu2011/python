#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import time
import json
from datetime import datetime


class JD:
    headers = {
        'referer': '', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
        }

    def __init__(self):
        self.index = 'https://www.jd.com/'
        self.user_url = 'https://passport.jd.com/user/petName/getUserInfoForMiniJd.action?&callback=jsonpUserinfo&_=' + str(int(time.time() * 1000))  # 检测用户信息
        self.buy_url = 'https://cart.jd.com/gate.action?pid={}&pcount=1&ptype=1'  # 添加到购物车
        self.pay_url = 'https://cart.jd.com/gotoOrder.action'  # 提交订单
        self.pay_success = 'https://trade.jd.com/shopping/order/submitOrder.action'  # 付款页面
        self.goods_id = ''
        self.thor = 'D5C7F962E429595EFA3FC4E15230FB451C002BCA2357BF7617BEEDC18840A1579C70F4014A79EB0BEE909D8D90CE22A6FAE2D3A877DFD4A94F6948EA67F446D91516662400C6A1E36989D55E4E6CB8D53152560E701A30E79EB4C86EF72681DA0CC4A2CA2E8150077F4F4EC9E066219086725C5C39C280599FF631ADD23BE7D097762B8D208D32A41D54AD6B024132'  # 用户的cookie
        self.session = requests.session()

    def login(self):  # 直接加上cookie访问用户信息。
        JD.headers['referer'] = 'https://cart.jd.com/cart.action'
        c = requests.cookies.RequestsCookieJar()
        c.set('thor', self.thor)  # 添加用户的thor
        self.session.cookies.update(c)
        response = self.session.get(url=self.user_url, headers=JD.headers).text.strip('jsonpUserinfo()\n')
        user_info = json.loads(response)
        print("nickName", user_info.get('nickName'))
        if user_info.get('nickName'):
            print("start shopping")
            self.shopping()

    def format(txt):
        print(str(txt).encode('utf-8'))

    def shopping(self):
        # goods_url = input('商品链接：')
        goods_url = 'https://item.jd.com/100012043978.html'
        # goods_url = 'https://item.jd.com/100006622021.html'
        # goods_url = 'https://item.jd.com/393841.html'
        self.goods_id = goods_url[goods_url.rindex('/') + 1:goods_url.rindex('.')]
        print(self.goods_id)
        JD.headers['referer'] = goods_url
        buy_url = self.buy_url.format(self.goods_id)
        print("buyUrl", buy_url)
        self.session.get(url=buy_url, headers=JD.headers)  # 添加到购物车
        self.session.get(url=self.pay_url, headers=JD.headers)  # 提交订单
        response = self.session.post(url=self.pay_success, headers=JD.headers)  # 提交订单
        order_id = json.loads(response.text).get('orderId')
        print("order_id", order_id)
        if order_id:
            print("success")
            print('success order_id:', order_id)


jd = JD()


# jd.login()

# 每n秒执行一次
def timer(n):
    while True:
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        time.sleep(n)
        jd.login()


# 1s
timer(1)
