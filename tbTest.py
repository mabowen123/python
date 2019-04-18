import time
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import re
import requests
import datetime
import threading

cookies = [{'domain': '.taobao.com', 'expiry': 1570364392, 'httpOnly': False, 'name': 'l', 'path': '/', 'secure': False,
            'value': 'bBNKgFDrvnQ1j422BOCanurza77OSIRYYuPzaNbMi_5pV6T_Q57OlMnbVF96VjfRsl8BqUZ28g99-etuZ'},
           {'domain': '.taobao.com', 'httpOnly': False, 'name': '_tb_token_', 'path': '/', 'secure': False,
            'value': 'ee718e8831156'},
           {'domain': '.taobao.com', 'expiry': 1562588389.392603, 'httpOnly': False, 'name': 't', 'path': '/',
            'secure': False, 'value': '9e4bf4590e087e875be768d4fbc7fb5f'},
           {'domain': '.taobao.com', 'httpOnly': False, 'name': 'sg', 'path': '/', 'secure': False, 'value': '222'},
           {'domain': '.taobao.com', 'expiry': 2185532384, 'httpOnly': False, 'name': 'cna', 'path': '/',
            'secure': False, 'value': '4XszFeqkEVECAd9dsPrUxpAB'},
           {'domain': '.taobao.com', 'httpOnly': True, 'name': 'cookie2', 'path': '/', 'secure': False,
            'value': '101b94a284815be9faa5694d2a5802dc'},
           {'domain': '.taobao.com', 'httpOnly': False, 'name': '_l_g_', 'path': '/', 'secure': False,
            'value': 'Ug%3D%3D'},
           {'domain': '.taobao.com', 'httpOnly': False, 'name': 'v', 'path': '/', 'secure': False, 'value': '0'},
           {'domain': '.taobao.com', 'httpOnly': False, 'name': 'uc1', 'path': '/', 'secure': False,
            'value': 'cookie14=UoTZ4Mc8RM%2F%2BMA%3D%3D&lng=zh_CN&cookie16=U%2BGCWk%2F74Mx5tgzv3dWpnhjPaQ%3D%3D&existShop=false&cookie21=Vq8l%2BKCLjhS4UhJVbCU7&tag=8&cookie15=V32FPkk%2Fw0dUvg%3D%3D&pas=0'},
           {'domain': '.taobao.com', 'httpOnly': True, 'name': 'unb', 'path': '/', 'secure': False,
            'value': '1685630092'},
           {'domain': '.taobao.com', 'httpOnly': True, 'name': 'skt', 'path': '/', 'secure': False,
            'value': '0d2f92b6774ebf58'},
           {'domain': '.taobao.com', 'httpOnly': True, 'name': 'cookie1', 'path': '/', 'secure': False,
            'value': 'U7lT5VA%2BUZPijwypX4uHMQ%2FCRNwnM%2FJvJMClXZd8oqo%3D'},
           {'domain': '.taobao.com', 'httpOnly': False, 'name': 'csg', 'path': '/', 'secure': False,
            'value': 'd16ab5e1'},
           {'domain': '.taobao.com', 'expiry': 1557404389.392775, 'httpOnly': True, 'name': 'uc3', 'path': '/',
            'secure': False,
            'value': 'vt3=F8dByEiUtP2dE2W1sZY%3D&id2=Uoe8j2Frb7X9Rw%3D%3D&nk2=AiA3LoCn8TFGpLP%2B&lg2=V32FPkk%2Fw0dUvg%3D%3D'},
           {'domain': '.taobao.com', 'httpOnly': False, 'name': 'existShop', 'path': '/', 'secure': False,
            'value': 'MTU1NDgxMjM5MA%3D%3D'},
           {'domain': '.taobao.com', 'expiry': 1586348389.392817, 'httpOnly': False, 'name': 'tracknick', 'path': '/',
            'secure': False, 'value': 'a13002685722'},
           {'domain': '.taobao.com', 'expiry': 1557404389.392838, 'httpOnly': False, 'name': 'lgc', 'path': '/',
            'secure': False, 'value': 'a13002685722'},
           {'domain': '.taobao.com', 'expiry': 1586348389.392859, 'httpOnly': False, 'name': '_cc_', 'path': '/',
            'secure': False, 'value': 'U%2BGCWk%2F7og%3D%3D'},
           {'domain': '.taobao.com', 'expiry': 1555417190.097793, 'httpOnly': False, 'name': 'mt', 'path': '/',
            'secure': False, 'value': 'ci=1_1'},
           {'domain': '.taobao.com', 'httpOnly': False, 'name': 'dnk', 'path': '/', 'secure': False,
            'value': 'a13002685722'},
           {'domain': '.taobao.com', 'httpOnly': False, 'name': '_nk_', 'path': '/', 'secure': False,
            'value': 'a13002685722'},
           {'domain': '.taobao.com', 'httpOnly': True, 'name': 'cookie17', 'path': '/', 'secure': False,
            'value': 'Uoe8j2Frb7X9Rw%3D%3D'},
           {'domain': '.taobao.com', 'expiry': 1608812389.392929, 'httpOnly': False, 'name': 'tg', 'path': '/',
            'secure': False, 'value': '0'},
           {'domain': '.taobao.com', 'expiry': 1586348389.466765, 'httpOnly': False, 'name': 'thw', 'path': '/',
            'secure': False, 'value': 'cn'},
           {'domain': '.taobao.com', 'expiry': 1570364389, 'httpOnly': False, 'name': 'isg', 'path': '/',
            'secure': False, 'value': 'BGNjXz1IO-as-vfSCBC1b-1F8qfN8Pb9uXvmXJXAokI51IP2HSiH6kGGyqVa9E-S'}]


def get_detail_urls(goods, page):
    total = 0
    urls = {}
    while True:
        if total / 20 == page:
            break
        browser.get("https://shopsearch.taobao.com/browse/shop_search.htm?q=" + str(goods) + "&isb=1&s=" + str(total))
        total += 20
        # 下拉加载

        for i in range(0, 10000, 300):
            browser.execute_script("var q=document.documentElement.scrollTop=" + str(i))
            time.sleep(0.5)
        time.sleep(2)
        html = BeautifulSoup(browser.page_source.encode('utf-8'), 'lxml')
        detail_urls = html.findAll("a", {"trace": "auction"})
        if not detail_urls:
            break
        for url in detail_urls:
            urls[url.get('trace-uid')] = url.get('href').strip()
    return urls


def get_detail_info(urls):
    for k, v in urls.items():
        browser.get("https:" + str(v))
        time.sleep(1)

        html = BeautifulSoup(browser.page_source.encode('utf-8'), 'lxml')
        promise = html.findAll("ul", {"class": "tb-serPromise"})
        for i in promise:
            if "材质保真险" in i.get_text().strip():
                txt = open('test.txt', 'a', encoding="utf-8")
                txt.write(str(v) + '\n')
                txt.close()
                time.sleep(1)


if __name__ == '__main__':
    #goods = input('商品名称')
    goods = "男鞋"
    # 加载谷歌驱动
    browser = webdriver.Chrome()
    # 登陆淘宝
    browser.get("https://login.taobao.com/member/login.jhtml")
    time.sleep(5)

    #for cookie in cookies:
        # setCookies 跳过登陆
     #   browser.add_cookie(cookie)

    page = 50
    # 拿到detail_url数组
    urls = get_detail_urls(goods, page)
    if not urls:
        exit("没商品信息")

    print("开始抓取")
    #urls.keys()
    get_detail_info(urls)
