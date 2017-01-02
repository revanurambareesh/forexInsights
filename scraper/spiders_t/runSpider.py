import scrapy
#from twisted.internet import reactor
from FxScrape.items import ForexItemTemplate
from scrapy.crawler import CrawlerProcess
from scrapy.crawler import CrawlerRunner
from ast import literal_eval
import re
import twisted.internet
import os
from scrapy.utils.log import configure_logging
from twisted.internet import reactor, protocol
from twisted.protocols.basic import LineOnlyReceiver
from scrapy.crawler import Crawler
from scrapy.settings import Settings
import sys

# list of crawlers

# crawlers that are running
RUNNING_CRAWLERS = []

class MySpider(scrapy.Spider):
    name = "fxSpider"
    ans=''

    def __init__(self, url = None, Filename=None):
        self.url = url  # source file name
        self.start_urls = [url]
        self.Filename=Filename

    def parse(self, response):
        start_urls = self.url
        #print response.xpath('//body/descendant-or-self::*/text()').extract()
        try:
            #file = open(self.Filename, "w")  # or "a+", whatever you need
        except IOError:
            print "Already opened!!"

        self.ans = self.ans + str(response.xpath('//body/descendant-or-self::*/text()').extract())
        #print 'NUMBER OF TEXT ENTRIES: ',len(response.xpath('//body//text()'))

        next_page_url = response.xpath('//li[@class="next"]/a/@href').extract()
        if next_page_url is not None:
            print 'PLAYING REQUESTS: ', scrapy.Request(response.urljoin(next_page_url))
            yield scrapy.Request(response.urljoin(next_page_url), callback=self.parse)

        #literal_eval("'%s'" % self.ans)

        ansi_escape = re.compile(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]')

        #file.write(ansi_escape.sub('', self.ans))
        #file.write(self.ans.decode('string_escape').replace('u\'',''))
        #file.close()
        print 'Written to File ', self.Filename

#TO_CRAWL = [MySpider]

def startProcess(urlLink, Filename=None):
    #process = CrawlerProcess({
    #    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    #})
    #
    #process.crawl(MySpider, urlLink, Filename)
    #process.start() # the script will block here until the crawling is finished
    #print 'completed scraping ', urlLink
    #process.terminate()
    #runner = CrawlerRunner()
    #settings.set("USER_AGENT", "Kiran Koduru (+http://kirankoduru.github.io)")
    #crawler = Crawler(settings)
    #crawler_obj = spider()
    #RUNNING_CRAWLERS.append(crawler_obj)
    configure_logging()
    runner = []
    runner.append(CrawlerRunner())
    i=0
    runner[i].crawl(MySpider, urlLink, Filename)
    d=runner[i].join()
    #d.addBoth(lambda _: reactor.stop())
    ##reactor.callLater()
    ##while 1:
    tries = 3
    #while tries:
    try:
        reactor.run() # the script will block here until the crawling is finished
        #tries-=1
        #break
    except Exception, e:
        print e
        #import sys
        #del sys.modules['twisted.internet.reactor']
        #from twisted.internet import reactor
        #from twisted.internet import default
        #default.install()

    print 'completed scraping ', urlLink
    runner[i].stop()
    runner.pop()
    #i+=1
    ##reactor.removeAll()
    #reactor.iterate()
    ##reactor.stop()

    # start logger
    #log.start(loglevel=log.DEBUG)

    # set up the crawler and start to crawl one spider at a time
    #for spider in TO_CRAWL:
    #    settings = Settings()

    #    # crawl responsibly
    #    settings.set('USER_AGENT', "For competition purpose only..")
    #    crawler = Crawler({
    #   'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    #    })
    #    crawler_obj = spider()
    #    RUNNING_CRAWLERS.append(crawler_obj)

    #    # stop reactor when spider closes
    #    crawler.signals.connect(spider_closing, signal=signals.spider_closed)
    #    crawler.configure()
    #    crawler.crawl(crawler_obj, urlLink, Filename)
    #    crawler.start()

    ## blocks process; so always keep as the last statement
    #reactor.run()

if __name__ == '__main__':
    #startProcess('https://en.wikipedia.org/wiki/Rama') #Not used -- (Ambareesh)
    label=-99
    Name='Sample'
    UrlList=['https://en.wikipedia.org/wiki/Sample_(statistics)','https://www.merriam-webster.com/dictionary/sample',
            'https://en.wikipedia.org/wiki/Sampling_(music)',
            'http://www.dictionary.com/browse/sample',
            'https://en.wiktionary.org/wiki/sample',
            'http://sample.com/',
            'http://www.surveysystem.com/sscalc.htm',
            'https://accuplacer.collegeboard.org/sites/default/files/accuplacer-sample-questions-for-students.pdf',
            'http://www.microchip.com/samples/',
            'http://www.sephora.com/free-beauty-samples',]

    urlLink='https://en.wikipedia.org/wiki/Sample_(statistics)'
    startProcess(urlLink, fileName)
    #ix=1
    #for urlLink in UrlList:
    #    parent_dir_name = os.getcwd()
    #    import runSpider as r
    #    fileName = parent_dir_name + '\data\\train_data\\' + str(label) + ',' + Name + '\\' + str(ix)+'.txt'
    #    r.startProcess(urlLink, fileName)
    #    #del sys.modules['r']
    #    ix=ix+1


#def spider_closing(spider):
#    """
#    Activates on spider closed signal
#    """
#    log.msg("Spider closed: %s" % spider, level=log.INFO)
#    RUNNING_CRAWLERS.remove(spider)
#    if not RUNNING_CRAWLERS:
#        reactor.stop()