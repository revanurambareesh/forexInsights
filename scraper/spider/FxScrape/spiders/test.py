import scrapy
from sampleScrap.items import ForexItemTemplate
#import scrapy
from scrapy.crawler import CrawlerProcess

class MySpider(scrapy.Spider):
    urlPath='https://www.youtube.com/watch?v=s-wORSZo7-w'
    name = "fxSpider"
    start_urls = [
        urlPath,
    ]

    def parse(self, response):
        #for quote in response.xpath('//body/descendant-or-self::*'):
        print response.xpath('//body/descendant-or-self::*/text()').extract()
        '''yield {
                'text': quote.xpath('//p/text()').extract_first(),
                #'author': quote.xpath('.//small[@class="author"]/text()').extract_first(),
                #'tags': quote.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').extract()
            }'''
        print 'NUMBER OF TEXT ENTRIES: ',len(response.xpath('//body//text()'))

        next_page_url = response.xpath('//li[@class="next"]/a/@href').extract()
        if next_page_url is not None:
            print 'PLAYING REQUESTS: ', scrapy.Request(response.urljoin(next_page_url))
            yield scrapy.Request(response.urljoin(next_page_url))

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(MySpider)
process.start() # the script will block here until the crawling is finished