import requests
from bs4 import BeautifulSoup
import re
#
# formdata = {"page": 1}
# r = requests.post("http://www.mafengwo.cn/gonglve/",data= formdata)
#
# #print(r.text)
#
# urls_list = []
# soup = BeautifulSoup(r.text, 'lxml')
#
# div = soup.find_all(class_="feed-item _j_feed_item")
# for urls in div:
#     url = urls.find("a", {"href": re.compile('.*?\.html')}, target="_blank")
#     if (url != None):
#         urls_list.append(url.get("href"))
#         # print(urls_list)
# print(urls_list)

item = dict()
articles = [1,2,3,4]

def fun(self):
    for i in range(1):
        item['article'] = articles[i]
        yield item

print(fun())