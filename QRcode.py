import requests
import json


def getToken():
    url = 'https://api.weixin.qq.com/cgi-bin/token'
    para = {"grant_type": "client_credential", "appid": "wxa867107cd2c1c857",
            'secret': "43c8c7e80d7cba852f7ecc108d985818"}
    r = requests.get(url, para)
    json = r.json()
    return json['access_token']


def QRcode1():
    data = input('链接:')
    token = getToken()
    url = "https://api.weixin.qq.com/cgi-bin/wxaapp/createwxaqrcode?access_token=" + token
    para = {"path": str(data)}
    paras = json.dumps(para)
    r = requests.post(url, paras)
    fp = open("test.jpg", "wb")
    fp.write(r.content)
    fp.close()


def QRcode2():
    page = input('链接:')
    token = getToken()
    url = "https://api.weixin.qq.com/wxa/getwxacode?access_token=" + token
    para = {"path": str(page)}
    paras = json.dumps(para)
    r = requests.post(url, paras)
    fp = open("test.jpg", "wb")
    fp.write(r.content)
    fp.close()


def type():
    type = input("1-生成二维码\n2-生成小程序码:")
    if type == "1":
        QRcode1()
    if type == "2":
        QRcode2()


if __name__ == '__main__':
    type()
