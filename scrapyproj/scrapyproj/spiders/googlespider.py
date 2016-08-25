# -*- coding: utf-8 -*-
import scrapy
import random
from scrapy.shell import inspect_response

SEARCH = 'asd'
START = 10

class GoogleSpider(scrapy.Spider):
    name = "google"
    allowed_domains = ["google.com"]
    start_urls = (
        'https://www.google.com.ua/search?q=' + SEARCH,
        'https://www.google.com.ua/search?q=' + SEARCH + '&start=' + str(START),
        'https://www.google.com.ua/search?q=' + SEARCH + '&start=' + str(START*2),
    )


    def parse(self, response):
        #inspect_response(response, self)
        links = response.xpath(".//h3[@class='r']")
        for link in links:
            link = link.xpath('.//a')[0].extract()
            if link.find("<b>") != -1:
                link.replace("<b>", "11111")
                link.replace("</b>", "1")
            try:
                key = link.split("?q=")[1]
            except:
                print("ERROR!", link)
            print(key)
           # val = link.split(">")[1].split('</a>')[0]
            val = link
            yield {key:val}


    def start_requests(self):
        for url in self.start_urls:
            headers = {}
            headers['User-Agent'] = str(random.randint(0,255))
#        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'   
            yield scrapy.Request(url, headers=headers, dont_filter=True)

