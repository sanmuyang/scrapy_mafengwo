import scrapy
import re
from bs4 import BeautifulSoup
from scrapy.http import Request
from urllib.request import urlopen
import requests
import pymysql
from ..items import *

#from mafengwo.items import MafengwoItem


class MafengwoSpider(scrapy.Spider):
    name = 'mafengwo'
    #start_urls = ['https://www.mafengwo.cn/gonglve/']

    def start_requests(self):
        for i in range(1, 2):
            form = {"page": str(i)}
            yield  scrapy.FormRequest(url = 'https://www.mafengwo.cn/gonglve/',method='POST', formdata =form)

    def parse(self, response):
        #self.get_title(response)
        item = MafengwoItem()
        urls = self.get_urls(response)
        articles = self.get_article(urls)
        items = []
        for i in range(len(articles)):
            items.append( {'article':articles[i]})
        return items

    # def get_title(self, response):
    #     titles_list = []
    #     soup = BeautifulSoup(response.text,'lxml')
    #     div = soup.find(name="div",attrs={'class': 'cont-main _j_feed_list'})
    #     titles = div.find_all(name = "div", class_ = "title")
    #     for title in titles:
    #         print(title.string)
    #         titles_list.append(title.string)
    #     return titles_list

    def get_urls(self,response):
        urls_list = []
        soup = BeautifulSoup(response.text, 'lxml')
        div =  soup.find_all(class_ = "feed-item _j_feed_item")
        for urls in div:
            url= urls.find("a",{"href": re.compile('.*?\.html')}, target = "_blank" )
            if(url != None):
                urls_list.append(url.get("href"))
       # print(urls_list)
        return urls_list


    def get_article(self, urls_list):

        articles_list = []
        for i in range(len(urls_list)):
            article = ""
            html = urlopen(urls_list[i]).read().decode('utf-8')
            soup = BeautifulSoup(html, features='lxml')
            divs = soup.find_all(name="div", attrs={'class': 'p-section'})
            for div in divs:
                if (div.get_text()!= None):
                    article += div.get_text()
            # print(article)

            # 如果没爬到，说明是另一种网页布局
            if (article == ""):
                divs = soup.find_all(name="p", attrs={'class': '_j_note_content _j_seqitem'})
                for div in divs:
                    if (div.get_text() != None):
                        article += div.get_text()

            # 去掉空格
            b = article.split()
            article = "".join(b)

            articles_list.append(article)
            # print(article)
            # print("########")

        #print(articles_list)
        return articles_list



