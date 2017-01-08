# Forex Insights
This repository contains my solution to the FX problem
This tool scrapes the top popular websites of a company and analyses the data. This data is then converted into dataset after which a machine learning model is trained. Easy intuitive UI is also provided. More Details can be found in design document at STAGE 1 Documents/FX Problem.pdf

### Overview of this approach


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
[This image shows tool generating insights for a company](STAGE 1 Documents/screenshots/Insights/generating insights.png)

## Running the tool
From command line run,
>> python main.py

## Data Scraped
Data scraped from web is about **450MB**. Since Data is uploaded here, the repository is large and is downloadable as zip file of about 90MB.
All the data has been colleted from public domain websites after *obeying* ROBOTS.TXT.

##### Author: **Ambareesh Revanur**  ([more](https://in.linkedin.com/in/ambareeshr))