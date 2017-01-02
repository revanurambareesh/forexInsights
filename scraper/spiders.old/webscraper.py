import scrapy
from twisted.internet import reactor, defer
from scrapy.utils.log import configure_logging
from scrapy.crawler import CrawlerRunner

class MySpider(scrapy.Spider):
    #urlPath=
    name = "RunFXspider"
    start_urls = [
        #urlPath,
    ]
    ans=''

    def __init__(self, url = None, Filename=None):
        self.url = url  # source file name
        self.start_urls = [url]
        self.Filename=Filename

    def parse(self, response):
        start_urls = self.url

        try:
            file = open(self.Filename, "w")
        except IOError:
            print "Already opened!!"

        print response.xpath('//body/descendant-or-self::*/text()').extract()

        self.ans = self.ans + str(response.xpath('//body/descendant-or-self::*/text()').extract())
        print 'NUMBER OF TEXT ENTRIES: ',len(response.xpath('//body//text()'))

        file.write(self.ans.decode('string_escape').replace('u\'',''))
        file.close()

        next_page_url = response.xpath('//li[@class="next"]/a/@href').extract()
        if next_page_url is not None:
            print 'PLAYING REQUESTS: ', scrapy.Request(response.urljoin(next_page_url))
            yield scrapy.Request(response.urljoin(next_page_url), self.parse)


configure_logging()
urlLink = 'https://www.youtube.com/watch?v=s-wORSZo7-w'
runner = CrawlerRunner()

@defer.inlineCallbacks
def crawl():
    yield runner.crawl(MySpider, urlLink, 'misc_data_try\\'+str(3)+'.txt')
    yield runner.crawl(MySpider, urlLink, 'misc_data_try\\'+str(4)+'.txt')
    reactor.stop()

crawl()
reactor.run()