# forexInsights
Scraping and providing *insights* for your business using NLP

**(WORK IN PROGRESS!! This project is by no means complete or error free just as yet.)**

Author: **Ambareesh Revanur**  ([more](https://in.linkedin.com/in/ambareeshr))
Originally written for Innovation hack! :)

## STAGE 1: 
Design Document available at /STAGE 1 documents/

## Idea Description


## Introduction
#### Why forexInsights?
#### NLP and web-scraping
#### 

Python 2.7
* Scrapy
* Google-Search API for Python(with custom keys)
* Scikit
* PyQt4

Some of the tools considered for this project includes [Pattern](http://www.clips.ua.ac.be/pattern).
This link https://github.com/lorien/awesome-web-scraping/blob/master/python.md desbribes different web scraping techniques.
https://in.mathworks.com/help/stats/naivebayes-class.html

## Steps:  
**Feature Extraction**  
- Web Scrape for Forex wikis from Google/Bing Search. 
- Get list of words (considering vocabulary?) that are present in each of the websites.
- Select n=100 words that are often defined apart from (article, an, the, ... using NLP)

**Scrape Forex websites**
- Web Scrape for Forex Websites from Excel sheet and for each of the entry Google/Bing Search of top 10.
- For each website, check if the word is present in the <p> tags. If yes increment the value
- After 10 websites, if the incremented value is above 6, normalise it to 1. Otherwise, make it 0. (or go ahead with multinomial naive bayes)

**Scrape Non-Forex websites**
- Web Scrape for Non-Forex Websites from Excel sheet and for each of the entry Google/Bing Search of top 10.
- For each website, check if the word is absent in the <p> tags. If yes increment the value.
- After 10 websites, if the incremented value is above 6, normalise it to 0. Otherwise, make it 1. (or go ahead with multinomial naive bayes)

**Generate Model**
- Using the data from Forex and Non-Forex site, Create a Naive Bayes Model.

**Testing**
- During test time, use the model and test it accordingly. Use the probablity generated as propensity score.
- Insights generated includes the similarity of the website to the other website based on L1 norm, L2 norm, which words indicated potential for the website. Mail is also generated automatically.


## Scraping
- Use <p> tag from HTML tag. (Learn & Do more with XPath)

PATH to Scrapy project Root >> scrapy startproject tutorial
PATH to Scrapy project Root >> scrapy crawl quotes
PATH to Scrapy project Root >> scrapy crawl quotes -o quotes.json  //or quotes.csv


Also note (from official source) 
Win + R: scrapy shell "http://quotes.toscrape.com/page/1/"

## Google Search API
(xGoogle: http://www.catonmat.net/blog/python-library-for-google-search/): Deprecated?
--(Set it up using the setup.py)--

-- my custom search engine key: 030550212650xxxxxxxx04:rbsuxqik2xyk (obfuscated)
-- my API key: A3IzaSyBf3JuAb7zOEOelexxxxxxxxmHo5LL3iRYk (obfuscated)

Go to -> scraper/google-api-python-client-master/main.py

## NLP Keyword Extraction
RAKE algorithm has been used.

Go to -> scraper/rake/keywordExtraction.py

## UI
Built in QtDesigner and saved as *.ui file

PATH to UI file >> Path..\Anaconda2\Lib\site-packages\PyQt4\pyuic4.bat -x FXfrontend.ui -o FXfront.py

