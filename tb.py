import time
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import re
import requests
import datetime

q = input("抓取商品得关键字")
info = {}
browser = webdriver.Chrome()
browser.get("https://login.taobao.com/member/login.jhtml")
dir = "./tb/" + str(q)
tb = os.path.exists(dir)
if not tb:
    os.makedirs(dir)

time.sleep(5)
browser.get("https://s.taobao.com/search?q=" + str(q) + "&sort=sale-desc")
time.sleep(5)
html = BeautifulSoup(browser.page_source.encode('utf-8'), 'lxml')
title = html.findAll("a", {'class': 'J_ClickStat'})
for a in title:
    name = re.sub('[^A-Z^a-z^0-9^\u4e00-\u9fa5]', "", a.get_text().strip())
    info[name] = a.get('href').strip()

for k, v in info.items():
    if not k:
        continue
    path = "./tb/" + str(q) + "/" + k
    detail = browser.get("https:" + v)
    time.sleep(5)
    js = "var q=document.documentElement.scrollTop=10000"
    browser.execute_script(js)
    time.sleep(10)
    print("正在抓取:" + v)
    html = BeautifulSoup(browser.page_source.encode('utf-8'), 'lxml')
    title = html.find("h1", {'data-spm': '1000983'}).get_text().strip()
    price = html.findAll("span", {'class': 'tm-price'})
    sale = html.findAll("span", {'class': 'tm-count'})
    argument = html.findAll("ul", {"id": "J_AttrUL"})
    imgs = html.findAll(class_="content ke-post")
    dir = os.path.exists(path)
    if not dir:
        os.makedirs(path)
    print("抓取图片中")
    for i in BeautifulSoup(str(imgs), 'lxml').findAll("img"):
        url = ''

        if i.get('data-ks-lazyload'):
            url = i.get('data-ks-lazyload')

        else:
            url = i.get('src')

        if url:
            r = requests.get(str(url))
            fp = open(path + "/" + '{0:%Y%m%d%H%M%S%f}'.format(datetime.datetime.now()) + ".jpg", "wb")
            fp.write(r.content)
            fp.close()
            time.sleep(1)

    print("抓取图片完成写入文本信息")
    txt = open(path + '/test.txt', 'w', encoding="utf-8")
    txt.write("商品名称:" + str(title) + '\n')
    txt.write("商品价格:" + str(price[0].get_text()) + '\n')
    if price.__len__() > 1:
        txt.write("商品促销价:" + str(price[1].get_text()) + '\n')

    txt.write("商品销量:" + str(sale[0].get_text()) + '\n')
    txt.write("商品评论:" + str(sale[1].get_text()) + '\n')

    if argument:
        for i in argument:
            txt.write("商品参数:" + str(i.get_text()) + '\n')

    txt.close()
    print("抓取结束")
