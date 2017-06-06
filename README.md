# Forex Insights
 
[Deployment: Click here!](https://business-forex-insights.herokuapp.com/)

![New Model](https://github.com/revanurambareesh/forexInsights/blob/master/Stage%201%20documents/diagrams/twoDplot.png)

The figure above shows the demonstration of generative model generated. The plot is drawn for some random set of training and test samples after the application of dimension reduction to the graph (using Principle component analysis) and is then scaled for clarity.

About 90% Accuracy on training set and about 80% Accuracy on test set.

## New Features added

* Web application has been built.
* Ensured right web links are scraped.
* To reduce over-fitting number of features are reduced.
* Using Scrapy and Beautiful Soup for scraping, Django for web server.
* Changed ML algorithm from supervised to unsupervised
* Training set consists of about 6000 companies, Cross Validation set consists of about 1000 companies and test set consists of about 1000 companies. Out of 50000 companies, info relevant to the project are considered.
* No hard bound value for predicting if the company is likely to opt for forex. (Previously there was a value 0.5). Now the value is determined by the algorithm based on the statistics of the training data.
* Tested on Linux Platforms as well. The app is deployed on to the cloud which is aware of linux environment and hence linux.


*Old code is archived [here](https://github.com/revanurambareesh/forexInsightsQtUI)*

-----

### Design Document:

It contains:  
* Algorithm
* Techonologies used
* System Architecture
* Mathematical reasoning behind ML models
* Insights generation

This document explains logic behind web-scraping, web-searching, training ML model, using trained model, generating insights, code snippet analysis, folder structure and NLP algorithm behind creating a dataset.

#### Implementation:
![HTML UI](https://github.com/revanurambareesh/forexInsights/blob/master/Stage%201%20documents/demo/demo.png)

[Click here to visit](https://business-forex-insights.herokuapp.com/)

### Running the server on local machine
To run the server on the localhost, it is recommended to use virtual environment in python.
Django and scrapy framework is needed to be installed.

> pip install -r requirements.txt

> python manager.py runserver 128.0.0.1:8000

## Data Scraped

Kindly check out *.gitignore* file for more details.
All the data has been collected from public domain websites after *obeying* ROBOTS.TXT.

##### Author: **Ambareesh Revanur**  ([more](https://in.linkedin.com/in/ambareeshr))
For any errata, bugs, typos, .. etc, please raise an issue in Issues tab! Thanks.
