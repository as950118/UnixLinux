#-*- encoding: utf8 -*-
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
from konlpy.tag import Kkma, Okt
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

debug = 0

class wcClass:
    def __init__(self, query):
        self.query = query

    def crawl(self, display=100, start=10):
        default_url = "https://openapi.naver.com/v1/search/webkr.xml"
        query = self.query
        display = display
        start = start
        query = "?query=" + urllib.parse.quote_plus(query)
        display = "&display=" + str(display)
        start = "&start=" + str(start)
        ret_url = default_url + query + display + start
        if debug:
            print(ret_url)

        headers = {
            "Host" : "openapi.naver.com",
            "User-Agent" : "curl/7.49.1",
            "Accept" : "*/*",
            "X-Naver-Client-Id" : "Ko1CYny7gsmuM8AIglgZ",
            "X-Naver-Client-Secret" : "8SBGA9yStB"
        }
        req = urllib.request.Request(ret_url, headers = headers)
        ret = urllib.request.urlopen(req)
        ret_XML = ret.read()
        xmlsoup = BeautifulSoup(ret_XML, 'html.parser')
        items = xmlsoup.find_all('item')

        sentences = ""
        for item in items:
            Type = type(item) #bs4.element.Tag
            for elem in item:
              if type(elem) == Type:
                sentences += elem.get_text(strip = 1)
        if debug:
            print(sentences)
        return sentences

    def nouns(self, sentences):
        okt = Okt()
        count = Counter(okt.nouns(sentences))
        if debug:
            print(count)
        return count

    def makewc(self, count, mask="./mask/mask_default.png", font_path="./font/font_default.ttf"):
        mask = np.array(Image.open(mask))
        wc = WordCloud(font_path=font_path, background_color='white', width=1000, height=1000, mask=mask)
        cloud = wc.generate_from_frequencies(count)
        plt.imshow(cloud)
        plt.axis("off")
        fig = plt.gcf()
        fig.savefig("./wcimg/"+self.query+".png")
        if debug:
            print("./wcimg/"+self.query+".png")
        return "./wcimg/"+self.query+".png"

    def main(self):
        obj = wcClass(self.query)
        sentences = obj.crawl()
        nouns = obj.nouns(sentences)
        obj.makewc(nouns)
        if debug:
            print("Completed WordCloud")
        return 1

if __name__=="__main__":
    wcClass(str(input())).main()
