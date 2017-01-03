import scrapy
from twisted.internet import reactor, defer
from scrapy.utils.log import configure_logging
from scrapy.crawler import CrawlerRunner

'''
SAMPLE data for __main__
'''
# following were the results obtained as per Google Custom Search

UrlL=[
		 'https://en.wikipedia.org/wiki/Sample_(statistics)','https://www.merriam-webster.com/dictionary/sample',
         'https://en.wikipedia.org/wiki/Sampling_(music)',
         'http://www.dictionary.com/browse/sample',
         'https://en.wiktionary.org/wiki/sample',
         'http://sample.com/',
         'http://www.surveysystem.com/sscalc.htm',
         'https://accuplacer.collegeboard.org/sites/default/files/accuplacer-sample-questions-for-students.pdf',
         'http://www.microchip.com/samples/',
         'http://www.sephora.com/free-beauty-samples',
]

FileL=[]

class MySpider(scrapy.Spider):
    name = "RunFXspider"
    start_urls = []
    ans=''

    def __init__(self, url = None, Filename=None):
        self.url = url
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

@defer.inlineCallbacks
def crawl(univList, runner):
    for link2D in univList: 
        print 'link getting scraped is: ', link2D[0][0]
        print 'Filename is: ', link2D[1]
        yield runner.crawl(MySpider, link2D[0][0], link2D[1])
    reactor.stop()

def startReactor(univList):
    configure_logging()
    runner = CrawlerRunner()
    crawl(univList, runner)
    reactor.run()

@defer.inlineCallbacks
def crawl_dep(urlList, FileList, runner):
	i=0
	for urlLink in urlList:
		print 'VALUE OF i IS: ', str(i)		
		print 'Filename is: ', FileList[i]
		yield runner.crawl(MySpider, urlLink, FileList[i])
		i=i+1
	reactor.stop()

def startReactor_dep(UrlL, FileL):
	configure_logging()
	runner = CrawlerRunner()
	crawl_dep(UrlL, FileL, runner)
	reactor.run()

if __name__ == '__main__':
	j=0
	for urlLink in UrlL:
		FileL.append('data\sample.info.old\\'+str(j)+'.txt')
		j=j+1
	startReactor_dep(UrlL, FileL)

