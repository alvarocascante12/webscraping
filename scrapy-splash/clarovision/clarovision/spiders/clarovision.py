from scrapy.item import Field
from scrapy.item import Item 
from scrapy.spiders import CrawlSpider,Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader


class Movies(Item):
     title = Field()
     price = Field()
     description = Field()

class ClarovisionCrawler(CrawlSpider):
    name = 'clarovision'
    custom_settings = {
        'USER_AGENT' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
        # 'CLOSESPIDER_PAGECOUNT': 20
    }
    
    allowed_domains = ['infobae.com']
    download_delay = 1
    start_urls=['https://www.clarovideo.com']
    rules=(
        Rule(LinkExtractor(allow=r'/argentina/vcard/homeuser/'),follow=True , callback='parse_movies'),

    )


    def parse_movies(self , response):

        item = ItemLoader(Movies(), response)
        item.add_xpath('title','//div[@class="vcard-header"]/p/text()')
        item.add_xpath('price','//spam[@class="space"]/p/text()')
        item.add_xpath('description','//spam/p/text()')

        yield item.load_item()
