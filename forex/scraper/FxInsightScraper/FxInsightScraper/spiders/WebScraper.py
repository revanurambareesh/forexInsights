import urllib2
import os
import bs4 as BeautifulSoup

__author__ = 'Ambareesh Revanur (@revanurambareesh)'

def crawl(univList):
    i = 0
    init_prog_val = 15

    for link2D in univList:
        stat = 'scraping ' + link2D[0][0]
        print 'link getting scraped is: ', link2D[0][0]
        print 'Filename is: ', link2D[1]

        count = 3
        while count > 0:
            try:
                ans= urllib2.urlopen(link2D[0][0], timeout=8).read()#HTML response
                soup=BeautifulSoup.BeautifulSoup(ans)
                ans=soup.get_text()
                #sleep(3)
                ans=ans.encode('ascii', 'ignore')
                ans=os.linesep.join([s for s in ans.splitlines() if s])

                file = open(link2D[1], "w")
                print ans
                file.write(ans)
                file.close()
                break

            except: 
                print 'Retrying as an unexpected error occured'
                count=-1
        if count == -1: print 'tried and failed to obtain the HTML... Check your network connectivity'

        i += 1

    stat = 'Completed Scraping from Web'

    #reactor.stop()


def startReactor(univList):
    crawl(univList)

