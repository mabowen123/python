import requests
import json
import urllib

# query = input('search')
query = '古武狂兵'

search = requests.get('https://api01pbmp.zhuishushenqi.com/book/fuzzy-search?query={' + query + '}&v={1}').text
search = json.loads(search)['books']
for v in search:
    print(str(search.index(v) + 1) + '\n' + '作者:' + v['author'] + '\n' + "简介:" + v['shortIntro'])
id = int(input('list_id')) - 1
res = requests.get('https://api01pbmp.zhuishushenqi.com/toc?view=summary&book=' + search[int(id)]['_id']).text
chapter_list = json.loads(
    requests.get('http://api.zhuishushenqi.com/toc/' + json.loads(res)[0]['_id'] + "?view=chapters").text)
chapters = chapter_list['chapters']

chapter_id = int(input('从第几章开始')) - 1
detail = requests.get(
    'https://chapter2.zhuishushenqi.com/chapter/' + urllib.parse.quote(chapters[chapter_id]["link"])).text
print(json.loads(detail)['chapter']['cpContent'])

while True:
    next_page = input('下一页').upper()

    if next_page == 'N':
        chapter_id = chapter_id + 1
        detail = requests.get(
            'https://chapter2.zhuishushenqi.com/chapter/' + urllib.parse.quote(chapters[chapter_id]["link"])).text
        print(json.loads(detail)['chapter']['cpContent'])


