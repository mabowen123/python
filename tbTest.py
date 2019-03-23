import time
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import re
import requests
import datetime
import threading

cookies = [{'domain': '.taobao.com', 'expiry': 1568869181, 'httpOnly': False, 'name': 'l', 'path': '/', 'secure': False,
            'value': 'bB_-WRfnvpRwMYQQBOCanurza77OSIRYYuPzaNbMi_5aJ6T6Xx7OlTiOkF96VjfRsl8BqUZ28g99-etuZ'},
           {'domain': '.taobao.com', 'httpOnly': False, 'name': '_tb_token_', 'path': '/', 'secure': False,
            'value': '5e746b831d013'},
           {'domain': '.taobao.com', 'expiry': 1561093168.986557, 'httpOnly': False, 'name': 't', 'path': '/',
            'secure': False, 'value': '70936f2c047dfd4a916efcee366e7fce'},
           {'domain': 's.taobao.com', 'httpOnly': True, 'name': 'JSESSIONID', 'path': '/', 'secure': False,
            'value': 'AE9AD4E8477CF6A7B435D60F9D8720D9'},
           {'domain': '.taobao.com', 'httpOnly': False, 'name': 'sg', 'path': '/', 'secure': False, 'value': '222'},
           {'domain': '.taobao.com', 'expiry': 2184037164, 'httpOnly': False, 'name': 'cna', 'path': '/',
            'secure': False, 'value': 'LKscFc6krSECAd9dsPoS8aUv'},
           {'domain': '.taobao.com', 'httpOnly': True, 'name': 'cookie2', 'path': '/', 'secure': False,
            'value': '1008a580602672d9e816abccf0a731a2'},
           {'domain': '.taobao.com', 'httpOnly': False, 'name': '_l_g_', 'path': '/', 'secure': False,
            'value': 'Ug%3D%3D'},
           {'domain': '.taobao.com', 'httpOnly': False, 'name': 'v', 'path': '/', 'secure': False, 'value': '0'},
           {'domain': '.taobao.com', 'httpOnly': False, 'name': 'uc1', 'path': '/', 'secure': False,
            'value': '"cookie15=URm48syIIVrSKA%3D%3D"'},
           {'domain': '.taobao.com', 'httpOnly': True, 'name': 'unb', 'path': '/', 'secure': False,
            'value': '1685630092'},
           {'domain': '.taobao.com', 'httpOnly': True, 'name': 'skt', 'path': '/', 'secure': False,
            'value': 'e31045e33eb5c334'},
           {'domain': '.taobao.com', 'httpOnly': True, 'name': 'cookie1', 'path': '/', 'secure': False,
            'value': 'U7lT5VA%2BUZPijwypX4uHMQ%2FCRNwnM%2FJvJMClXZd8oqo%3D'},
           {'domain': '.taobao.com', 'httpOnly': False, 'name': 'csg', 'path': '/', 'secure': False,
            'value': '75ce645d'},
           {'domain': '.taobao.com', 'expiry': 1555909168.986694, 'httpOnly': True, 'name': 'uc3', 'path': '/',
            'secure': False,
            'value': 'vt3=F8dByErZTBjvP%2Fp5Al8%3D&id2=Uoe8j2Frb7X9Rw%3D%3D&nk2=AiA3LoCn8TFGpLP%2B&lg2=UtASsssmOIJ0bQ%3D%3D'},
           {'domain': '.taobao.com', 'httpOnly': False, 'name': 'existShop', 'path': '/', 'secure': False,
            'value': 'MTU1MzMxNzE2OA%3D%3D'},
           {'domain': '.taobao.com', 'expiry': 1584853168.986729, 'httpOnly': False, 'name': 'tracknick', 'path': '/',
            'secure': False, 'value': 'a13002685722'},
           {'domain': '.taobao.com', 'expiry': 1555909168.986744, 'httpOnly': False, 'name': 'lgc', 'path': '/',
            'secure': False, 'value': 'a13002685722'},
           {'domain': '.taobao.com', 'expiry': 1584853168.986761, 'httpOnly': False, 'name': '_cc_', 'path': '/',
            'secure': False, 'value': 'U%2BGCWk%2F7og%3D%3D'},
           {'domain': '.taobao.com', 'expiry': 1553921980.556727, 'httpOnly': False, 'name': 'mt', 'path': '/',
            'secure': False, 'value': 'ci=0_1'},
           {'domain': '.taobao.com', 'httpOnly': False, 'name': 'dnk', 'path': '/', 'secure': False,
            'value': 'a13002685722'},
           {'domain': '.taobao.com', 'httpOnly': False, 'name': '_nk_', 'path': '/', 'secure': False,
            'value': 'a13002685722'},
           {'domain': '.taobao.com', 'httpOnly': True, 'name': 'cookie17', 'path': '/', 'secure': False,
            'value': 'Uoe8j2Frb7X9Rw%3D%3D'},
           {'domain': '.taobao.com', 'expiry': 1607317168.986813, 'httpOnly': False, 'name': 'tg', 'path': '/',
            'secure': False, 'value': '0'},
           {'domain': '.taobao.com', 'expiry': 1584421181, 'httpOnly': False, 'name': 'thw', 'path': '/',
            'secure': False, 'value': 'cn'},
           {'domain': '.taobao.com', 'expiry': 1868677180.810174, 'httpOnly': True, 'name': 'enc', 'path': '/',
            'secure': True,
            'value': 'fgqFjaafH%2B12X9GdZCSg9%2FigoP8wAaNXJmVVwgNT25Hqke1v03i%2Fk8BmKGKX9LAhARVEBX2HrEOpdh%2FkAoeORw%3D%3D'},
           {'domain': '.taobao.com', 'expiry': 1568869181, 'httpOnly': False, 'name': 'isg', 'path': '/',
            'secure': False, 'value': 'BPDwLsbHWGYbMARiJx1k7ggpwb6CkdXrfor1FepBvMsepZBPkkmkE0YX-exgNYxb'},
           {'domain': '.taobao.com', 'expiry': 1584853181.625184, 'httpOnly': False, 'name': 'hng', 'path': '/',
            'secure': False, 'value': 'CN%7Czh-CN%7CCNY%7C156'}]


def tb_dir(goods):
    # 创建文件夹
    path = "./tb/" + str(goods) + "/"
    tb = os.path.exists(path)
    if not tb:
        os.makedirs(path)
    return path


def get_detail_urls(goods, page):
    total = 0
    urls = []
    while True:
        if total / 44 == page:
            break
        browser.get("https://s.taobao.com/search?q=" + str(goods) + "&sort=sale-desc" + "&s=" + str(total))
        total += 44
        time.sleep(5)
        html = BeautifulSoup(browser.page_source.encode('utf-8'), 'lxml')
        detail_urls = html.findAll("a", {"class": "J_ClickStat"})
        if not detail_urls:
            break
        for url in detail_urls:
            urls.append(url.get('href').strip())

    return list(set(urls))


def get_detail_info(urls, hanld, path):
    for url in urls:
        url = str(url)
        # 切换到指定的选项页
        browser.switch_to.window(hanld)
        browser.get("https:" + url)
        # 下拉加载
        browser.execute_script("var q=document.documentElement.scrollTop=10000")
        time.sleep(5)
        # 存储静态数据
        html = BeautifulSoup(browser.page_source.encode('utf-8'), 'xml')
        title = html.find("h1", {'data-spm': '1000983'})
        if not title:
            title = html.find("h3", {'class': 'tb-main-title'})

        if not title:
            continue
        # 去除特殊字符 创建文件夹
        title = re.sub('[^A-Z^a-z^0-9^\u4e00-\u9fa5]', "", title.get_text().strip())
        print("t1" + title + url)
        title_path = path + title
        tb = os.path.exists(title_path)
        if not tb:
            os.makedirs(title_path)

        price = html.findAll("span", {'class': 'tm-price'})
        if not price:
            price = html.findAll(class_="tb-rmb-num")
        sale = html.findAll("span", {'class': 'tm-count'})
        argument = html.findAll("ul", {"id": "J_AttrUL"})
        if not argument:
            argument = html.findAll("ul", {"class": "attributes-list"})

        print("t1商品信息写入")
        txt = open(title_path + '/test.txt', 'w', encoding="utf-8")
        txt.write("商品名称:" + str(title) + '\n')
        if not price:
            txt.write("商品价格:" + str(price[0].get_text()) + '\n')
            if price.__len__() > 1:
                txt.write("商品促销价:" + str(price[1].get_text()) + '\n')

        if sale:
            txt.write("商品销量:" + str(sale[0].get_text()) + '\n')
            txt.write("商品评论:" + str(sale[1].get_text()) + '\n')

        if argument:
            for i in argument:
                txt.write("商品参数:" + str(i.get_text()) + '\n')

        txt.close()

        imgs = html.findAll(class_="content ke-post")
        if not imgs:
            imgs = html.findAll(id="J_DivItemDesc")
        print("t1抓取图片中")
        for i in BeautifulSoup(str(imgs), 'lxml').findAll("img"):
            if i.get('data-ks-lazyload'):
                url = i.get('data-ks-lazyload')

            else:
                url = i.get('src')

            if url:
                r = requests.get(str(url))
                fp = open(title_path + "/" + '{0:%Y%m%d%H%M%S%f}'.format(datetime.datetime.now()) + ".jpg", "wb")
                fp.write(r.content)
                fp.close()
                time.sleep(0.5)

        time.sleep(5)


def get_detail_info1(urls, hanld1, path):
    for url in urls:
        url = str(url)
        # 切换到指定的选项页
        browser1.switch_to.window(hanld1)
        browser1.get("https:" + url)
        # 下拉加载
        browser1.execute_script("var q=document.documentElement.scrollTop=10000")
        time.sleep(5)
        # 存储静态数据
        html = BeautifulSoup(browser1.page_source.encode('utf-8'), 'lxml')
        title = html.find("h1", {'data-spm': '1000983'})
        if not title:
            title = html.find("h3", {'class': 'tb-main-title'})

        if not title:
            continue
        # 去除特殊字符 创建文件夹
        title = re.sub('[^A-Z^a-z^0-9^\u4e00-\u9fa5]', "", title.get_text().strip())
        print("t2" + title + url)
        title_path = path + title
        tb = os.path.exists(title_path)
        if not tb:
            os.makedirs(title_path)

        price = html.findAll("span", {'class': 'tm-price'})
        if not price:
            price = html.findAll(class_="tb-rmb-num")

        sale = html.findAll("span", {'class': 'tm-count'})
        argument = html.findAll("ul", {"id": "J_AttrUL"})
        if not argument:
            argument = html.findAll("ul", {"class": "attributes-list"})

        print("t2商品信息写入")
        txt = open(title_path + '/test.txt', 'w', encoding="utf-8")
        txt.write("商品名称:" + str(title) + '\n')
        if not price:
            txt.write("商品价格:" + str(price[0].get_text()) + '\n')
            if price.__len__() > 1:
                txt.write("商品促销价:" + str(price[1].get_text()) + '\n')

        if sale:
            txt.write("商品销量:" + str(sale[0].get_text()) + '\n')
            txt.write("商品评论:" + str(sale[1].get_text()) + '\n')

        if argument:
            for i in argument:
                txt.write("商品参数:" + str(i.get_text()) + '\n')

        txt.close()

        imgs = html.findAll(class_="content ke-post")
        if not imgs:
            imgs = html.findAll(id="J_DivItemDesc")
        print("t2抓取图片中")
        for i in BeautifulSoup(str(imgs), 'lxml').findAll("img"):
            if i.get('data-ks-lazyload'):
                url = i.get('data-ks-lazyload')

            else:
                url = i.get('src')

            if url:
                r = requests.get(str(url))
                fp = open(title_path + "/" + '{0:%Y%m%d%H%M%S%f}'.format(datetime.datetime.now()) + ".jpg", "wb")
                fp.write(r.content)
                fp.close()
                time.sleep(0.5)

        time.sleep(5)


if __name__ == '__main__':
    # goods = input('商品名称')
    goods = "手机"
    # 加载谷歌驱动
    browser = webdriver.Chrome()
    browser1 = webdriver.Chrome()
    # 创建文件夹
    path = tb_dir(goods)
    # 登陆淘宝
    browser.get("https://login.taobao.com/member/login.jhtml")
    browser1.get("https://login.taobao.com/member/login.jhtml")
    for cookie in cookies:
        # setCookies 跳过登陆
        browser.add_cookie(cookie)
        browser1.add_cookie(cookie)

    page = 1
    # 拿到detail_url数组
    urls = get_detail_urls(goods, page)
    if not urls:
        exit("没商品信息")

    print("开始抓取")
    # 多打开一个浏览器 分给不同线程处理
    hanld = browser.current_window_handle
    hanld1 = browser1.current_window_handle

    # 线程处理
    t1 = threading.Thread(target=get_detail_info, args=(urls[0:int(len(urls) / 2)], hanld, path))
    t2 = threading.Thread(target=get_detail_info1, args=(urls[int(len(urls) / 2):], hanld1, path))
    t1.start()
    t2.start()
