# Forex Insights

Status: Lot of code movement is taking place..

##### Modifications are being made.... Kindly keep in touch with me...
[Deployment Link: UI](https://business-forex-insights.herokuapp.com/)

*Old code is archived [here](https://github.com/revanurambareesh/forexInsightsQtUI)*

## Mentoring

* Ensured right web links are scraped.
* Dataset does not assume 0 for non-forex anymore. Hence, *unsupervised learning*
* Using Scrapy and Beautiful Soup for scraping, Django for web server.
* Changed ML algorithm from supervised to unsupervised
* UI is now Web-based
* Training set consists of about 6000 companies, Cross Validation set consists of about 1000 companies and test set consists of about 1000 companies. Out of 50000 companies, info relevant to the project are considered.

As discussed, I am located in Bangalore and I can demonstrate it physically as well.

-----

#### Stage 1 Design Document:
(Old document) This can be found in **/STAGE 1 Documents/FX_problem.pdf**.
It contains:  
* Algorithm
* Techonologies used
* System Architecture
* Mathematical reasoning behind ML models
* Insights generation

This document explains logic behind web-scraping, web-searching, training ML model, using trained model, generating insights, code snippet analysis, folder structure and NLP algorithm behind creating a dataset.

#### Mentoring phase Implementation:
This is being updated shortly...

https://business-forex-insights.herokuapp.com/

### Running the tool
To run the server on the localhost, it is recommended to use virtual environment in python.
Django and scrapy framework is needed to be installed.

> pip install -r requirements.txt

> python manager.py runserver 128.0.0.1:8000

## Data Scraped

Data scraped from web is more than **1GB**. To save upload time scraped data is **not** uploaded here.
Kindly check out *.gitignore* file more details.
All the data has been collected from public domain websites after *obeying* ROBOTS.TXT.

##### Author: **Ambareesh Revanur**  ([more](https://in.linkedin.com/in/ambareeshr))
For any errata, bugs, typos, .. etc, please raise an issue in Issues tab! Thanks.
