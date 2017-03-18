# Forex Insights
 
[Deployment: Click here!](https://business-forex-insights.herokuapp.com/)

![New Model](https://github.com/revanurambareesh/forexInsights/blob/master/Stage%201%20documents/diagrams/twoDplot.png)

The figure above shows the demonstration of *new* model generated. The plot is drawn for some random set of training and test samples after the application of dimension reduction to the graph (using Principle component analysis) and is then scaled for clarity.
About 90% Accuracy on training set and about 70% Accuracy on test set.

## Mentoring

* Ensured right web links are scraped.
* Dataset does not assume 0 for non-forex anymore. Hence, *unsupervised learning*
* Using Scrapy and Beautiful Soup for scraping, Django for web server.
* Changed ML algorithm from supervised to unsupervised
* UI is now Web-based
* Training set consists of about 6000 companies, Cross Validation set consists of about 1000 companies and test set consists of about 1000 companies. Out of 50000 companies, info relevant to the project are considered.

As discussed, I am located in Bangalore and I can demonstrate it physically as well.

*Old code is archived [here](https://github.com/revanurambareesh/forexInsightsQtUI)*

-----

#### Stage 1 Design Document:
(Old document) This can be found in /STAGE 1 Documents/FX_problem.pdf.
It contains:  
* Algorithm
* Techonologies used
* System Architecture
* Mathematical reasoning behind ML models
* Insights generation

This document explains logic behind web-scraping, web-searching, training ML model, using trained model, generating insights, code snippet analysis, folder structure and NLP algorithm behind creating a dataset.

#### Mentoring phase Implementation:
![HTML UI](https://github.com/revanurambareesh/forexInsights/blob/master/Stage%201%20documents/demo/demo.png)

Runs best on the latest version on Mozilla Firefox. The company name should be entered into the above textbox and return key (Enter key) must be hit.
Batch of companies can be upload in a .csv format with the company name in each line. However the number of searches are limited to 100 per day.

[Click here to visit](https://business-forex-insights.herokuapp.com/)

### Running the tool
To run the server on the localhost, it is recommended to use virtual environment in python.
Django and scrapy framework is needed to be installed.

> pip install -r requirements.txt

> python manager.py runserver 128.0.0.1:8000

## Data Scraped

Data scraped from web is more than **1GB**. To save upload time scraped data is **not** uploaded here.
Kindly check out *.gitignore* for file more details.
All the data has been collected from public domain websites after *obeying* ROBOTS.TXT.

##### Author: **Ambareesh Revanur**  ([more](https://in.linkedin.com/in/ambareeshr))
For any errata, bugs, typos, .. etc, please raise an issue in Issues tab! Thanks.
