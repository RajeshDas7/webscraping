import scrapy
from scrapy.selector import Selector 
from scrapy.http import HtmlResponse

class JokesSpider(scrapy.Spider):
    name='hindu'
    start_urls = [
        'https://www.thehindu.com/search/?q=mumbai&order=DESC&sort=publishdate'
    ]

    def parse(self, responce):
        f=0
        for joke in responce.xpath("//a[@class='story-card75x1-text']"):
            print(f)
            f+=1
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            # print(joke)
            
            print(joke.xpath("//a[@class='story-card75x1-text']/text()").extract())
            yield {
                'joke_text' : joke.xpath("//a[@class='story-card75x1-text']/text()").extract(),
                'joke_url':joke.xpath("//a[@class='story-card75x1-text']/@href").extract()
            }
            break

        # next_page = responce.xpath("//li[@class='next']/a/@href").extract_first()
        # if next_page is not None:
        #     next_page_link = responce.urljoin(next_page)
        #     yield scrapy.Request(url=next_page_link, callback=self.parse)
    

