# Forex Insights
This repository contains my solution to the FX problem
This tool scrapes the top popular websites of a company and analyses the data. This data is then converted into dataset after which a machine learning model is trained. Easy intuitive UI is also provided. More Details can be found in design document at STAGE 1 Documents/FX Problem.pdf

#### Stage 1 Design Document:
This can be found in /STAGE 1 Documents/FX problem.pdf. 
It contains:  
* Algorithm
* Techonologies used
* System Architecture
* Mathematical reasoning behind ML models
* Insights generation

This document explains logic behind web-scraping, web-searching, training ML model, using trained model, generating insights, code snippet analysis, folder structure and NLP algorithm behind creating a dataset.

#### Stage 2 Prototype Implementation:
The following diagram depicts, an running instance of the tool. More of such instances are shown in /STAGE 1 Documents/screenshots.  

![This image shows tool generating insights for a company](https://github.com/revanurambareesh/forexInsights/blob/master/STAGE%201%20documents/screenshots/Insights/generating%20insights.png)


## Overview of this approach
This project aims to support forex business using data available on public web domain using NLP, web-scraping and ML. A set of most frequently appearing keywords in what defines the term 'Forex' are used as feature set. The dataset is generated for each of the entry given in excel sheet (mentioned in problem statement) using web search APIs, and each of the obtained links is scraped for data within specified HTML tags. The presence of the keyword in the data after processing for its presence in majority of the links crawled by search engine (see design document) is considered as y = 1 or positive case. Once the dataset is ready, Naïve Bayes model is trained. This model is used to predict the probability to determine a potential FX customer. An intuitive GUI is also provided for this project. 

Insights like probability that a company will opt for Forex, its similarity with known companies (from training set) and also how popular this company is on web. Complete project is developed in Python 2.7. Both Stage1 and Stage2 submissions are made available at github.com/revanurambareesh/forexInsights. Stage 1 design document elaborates on the algorithm, technologies used, UI, scraper, and NLP model.

### Running the tool
From command line run,
> python main.py

## Data Scraped
Data scraped from web is about **450MB**. Since Data is uploaded here, the repository is large and is downloadable as [zip file](https://github.com/revanurambareesh/forexInsights/archive/master.zip) of about 90MB.
All the data has been collected from public domain websites after *obeying* ROBOTS.TXT.

##### Author: **Ambareesh Revanur**  ([more](https://in.linkedin.com/in/ambareeshr))
For any errata, bugs, typos, .. etc, please raise an issue in Issues tab! Thanks.