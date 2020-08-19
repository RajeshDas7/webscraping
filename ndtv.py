import scrapy
from scrapy.selector import Selector 
from scrapy.http import HtmlResponse

class JokesSpider(scrapy.Spider):
    name='ndtv'
    start_urls = [
        'https://www.ndtv.com/search?searchtext=mumbai'
    ]

    def parse(self, responce):
        f=0
        for joke in responce.xpath("//li[@style='padding: 5px;']"):
        # for joke in responce.xpath("//li[@style='padding: 5px;']/p/a/strong"):
            print(f)
            f+=1
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            # print(joke)
            
            # print(joke.xpath("//li[@style='padding: 5px;']/p/a/strong").extract())
            yield {
                'joke_text' : joke.xpath("//li[@style='padding: 5px;']/p/a/strong").extract()
            }
            break

        # next_page = responce.xpath("//li[@class='next']/a/@href").extract_first()
        # if next_page is not None:
        #     next_page_link = responce.urljoin(next_page)
        #     yield scrapy.Request(url=next_page_link, callback=self.parse)
    

