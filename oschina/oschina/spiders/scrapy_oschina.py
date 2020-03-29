import scrapy
from oschina.items import OschinaItem
from urllib.parse import unquote



class ScrapyOschinaSpider(scrapy.Spider):
    name = "scrapy_oschina"
    allowed_domains = ["oschina.net"]
    start_urls = (
        'http://www.oschina.net',
    )

    def parse(self, response):
        sel = scrapy.Selector(response)
        links_in_a_page = sel.xpath('//a[@href]')  # 页面内的所有链接

        for link_sel in links_in_a_page:
            item = OschinaItem()
            link = str(link_sel.re('href="(.*?)"')[0])  # 每一个url
            if link:
                if not link.startswith('http'):  # 处理相对URL
                    link = response.url + link
                item['links'] = link
                link_text = link_sel.xpath('text()').extract()   # 每个url的链接文本, 若不存在设为None
                if link_text:
                    item['title'] = str(unquote(link_text[0]))
                else:
                    item['title'] = None

                yield item

