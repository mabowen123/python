#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author :mabowen
# @Time   :2018/10/23 20:04
import pymysql
import requests
import json
import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def data_base(id):
    # 连接内网数据库
    db = pymysql.connect('192.168.1.254', 'root', 'root123', 'ym_admin', charset='utf8')
    cursor = db.cursor()
    sql = "SELECT id,type,title,vip_price, cover FROM ym_commodity where id=" + str(id)
    cursor.execute(sql)
    results = cursor.fetchone()
    db.close()
    return results


def get_token():
    url = 'https://api.weixin.qq.com/cgi-bin/token'
    para = {"grant_type": "client_credential", "appid": "wx235fd97677921c7e",
            'secret': "2877b2a89c6c39ce07862cf25a2aa649"}
    r = requests.get(url, para)
    json = r.json()
    return json['access_token']


def qr_code(type, token):
    qr_name = "qr.jpg"
    if type == 3:
        page = "pages/group_details/index?commodity_id=" + str(id)
    else:
        page = "pages/goods_details/index?goods_id=" + str(id)
    url = "https://api.weixin.qq.com/cgi-bin/wxaapp/createwxaqrcode?access_token=" + token
    para = {"path": str(page)}
    paras = json.dumps(para)
    r = requests.post(url, paras)
    fp = open(qr_name, "wb")
    fp.write(r.content)
    fp.close()


def cover(cover):
    cover_name = "cover.jpg"
    url = "http://image.yemagongyinglian.com/" + str(cover)
    r = requests.get(url)
    fp = open(cover_name, "wb")
    fp.write(r.content)
    fp.close()


def add_cover(id):
    try:
        # 加载底图
        base_img = Image.open('baseImg.jpg')
        # 加载新图片
        new_img = Image.open("cover.jpg")
    except IOError:
        print(IOError.errno)
    else:
        new_img = new_img.resize((620, 620))
        base_img.paste(new_img, (0, 0))
        base_img.save(str(id) + ".jpg")  # 保存图片


def add_qr(id):
    try:
        # 加载底图
        base_img = Image.open(str(id) + ".jpg")
        # 加载新图片
        new_img = Image.open("qr.jpg")
    except IOError:
        print(IOError.errno)
    else:
        new_img = new_img.crop((0, 0, 460, 460))
        new_img = new_img.resize((200, 200))
        base_img.paste(new_img, (410, 655))
        base_img.save(str(id) + ".jpg")  # 保存图片


def add_text(id, title, price):
    title = title.replace(' ', '')
    if len(title) > 10:
        title = str(title[:18]) + "..."
    font = ImageFont.truetype('simhei.ttf', 30)
    img = Image.open(str(id) + '.jpg')
    draw = ImageDraw.Draw(img)
    draw.text((30, 690), title[:10], fill=(90, 90, 90), font=font)
    draw.text((30, 720), title[10:21], fill=(90, 90, 90), font=font)
    draw.text((30, 810), "￥" + str(price), fill=(253, 219, 0), font=font)
    img.save(str(id) + '.jpg')


if __name__ == '__main__':
    id = input("输入商品id")
    # 获取数据
    info = data_base(id)
    # 拿到token
    token = get_token()
    # 生成二维码
    qr_code(info[1], token)
    # 生成封面图
    cover(info[4])
    # 生成底图
    img = Image.new("RGB", [620, 864], "white")
    img.save('baseImg.jpg')
    # 加封面图
    add_cover(info[0])
    # 加二维码
    add_qr(info[0])
    # 添加文字
    add_text(info[0], info[2], info[3])

    #删除生成的多余文件
    os.remove('baseImg.jpg')
    os.remove('cover.jpg')
    os.remove('qr.jpg')

