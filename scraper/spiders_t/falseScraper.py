import scrapy
#from FxSpider.items import ForexItemTemplate
#import scrapy
from scrapy import signals
from scrapy.crawler import CrawlerProcess
from twisted.internet import reactor, defer
from scrapy.xlib.pydispatch import dispatcher
from time import sleep
from scrapy.utils.log import configure_logging
from scrapy.crawler import CrawlerRunner

result = None

class MySpider(scrapy.Spider):
    #urlPath=
    name = "fxSpider_f"
    start_urls = [
        #urlPath,
    ]
    ans=''

    def __init__(self, url = None, Filename=None):
        #dispatcher.connect(stop_reactor, signal=signals.spider_closed)
        self.url = url  # source file name
        self.start_urls = [url]
        self.Filename=Filename

    def parse(self, response):
        start_urls = self.url
        #for quote in response.xpath('//body/descendant-or-self::*'):
        try:
            file = open(self.Filename, "w")  # or "a+", whatever you need
        except IOError:
            print "Already opened!!"

        print response.xpath('//body/descendant-or-self::*/text()').extract()

        self.ans = self.ans + str(response.xpath('//body/descendant-or-self::*/text()').extract())
        
        '''yield {
                'text': quote.xpath('//p/text()').extract_first(),
                #'author': quote.xpath('.//small[@class="author"]/text()').extract_first(),
                #'tags': quote.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').extract()
            }'''
        print 'NUMBER OF TEXT ENTRIES: ',len(response.xpath('//body//text()'))

        file.write(self.ans.decode('string_escape').replace('u\'',''))
        file.close()

        next_page_url = response.xpath('//li[@class="next"]/a/@href').extract()
        if next_page_url is not None:
            print 'PLAYING REQUESTS: ', scrapy.Request(response.urljoin(next_page_url))
            yield scrapy.Request(response.urljoin(next_page_url))


#def stop_reactor():
#    reactor.stop()
#
#def set_result(item):
#    print 'THERE AND HERE!!'
#    result = 1

#i = 9
#while (i < 10):
#    Filename='misc_data_try\\'+str(i)+'.txt'
#    urlLink = 'https://www.youtube.com/watch?v=s-wORSZo7-w'
#    process = CrawlerProcess({
#        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
#    })
#    
#    process.crawl(MySpider, urlLink, Filename)
#    process.start(stop_after_crawl=False) # the script will block here until the crawling is finished
#    i=i+1


#i = 0
##while (i < 10):
##process = []
#while 1:
#    Filename='misc_data_try\\'+str(i)+'.txt'
#    urlLink = 'https://www.youtube.com/watch?v=s-wORSZo7-w'
#    process = (CrawlerProcess({
#        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
#    }))
#    #mySpider = MySpider()
#    #dispatcher.connect(set_result, signals.item_scraped)
#    
#    SpiderClass = type(MySpider)
#    process.queue.append_spider(SpiderClass())
#    process.crawl(mySpider, urlLink, Filename)
#    #try:
#    #if i==0:
#    process.start(stop_after_crawl=False)
#    #else:
#    #    process[i].join()
#
#    print i
#    #if i != 0:
#    #    process[i-1].stop()
#    #except:
#    #    print 'reactor failed'
#
#    i=i+1
#    if result is not None:
#        break
#    sleep(3)


configure_logging()
#Filename='misc_data_try\\'+str(1)+'.txt'
urlLink = 'https://www.youtube.com/watch?v=s-wORSZo7-w'
runner = CrawlerRunner()

@defer.inlineCallbacks
def crawl():
    yield runner.crawl(MySpider, urlLink, 'misc_data_try\\'+str(14)+'.txt')
    yield runner.crawl(MySpider, urlLink, 'misc_data_try\\'+str(25)+'.txt')
    reactor.stop()

crawl()
reactor.run()