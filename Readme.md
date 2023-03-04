# <p  style="color:blue;text-align:center;" > Walmart-sales forescast </p>

## promblem statment : In this recruiting competition, job-seekers are provided with historical sales data for 45 Walmart stores located in different regions. Each store contains many departments, and participants must project the sales for each department in each store. To add to the challenge, selected holiday markdown events are included in the dataset. These markdowns are known to affect sales, but it is challenging to predict which departments are affected and the extent of the impact.

## Dataset Description
Data Link: https://www.kaggle.com/competitions/walmart-recruiting-store-sales-forecasting/data

stores.csv

This file contains anonymized information about the 45 stores, indicating the type and size of store.

train.csv

This is the historical training data, which covers to 2010-02-05 to 2012-11-01. Within this file you will find the following fields:

* Store - the store number
* Dept - the department number
* Date - the week
* Weekly_Sales -  sales for the given department in the given store
* IsHoliday - whether the week is a special holiday week
test.csv

This file is identical to train.csv, except we have withheld the weekly sales. You must predict the sales for each triplet of store, department, and date in this file.

features.csv

This file contains additional data related to the store, department, and regional activity for the given dates. It contains the following fields:

* Store - the store number
* Date - the week
* Temperature - average temperature in the region
* Fuel_Price - cost of fuel in the region
* MarkDown1-5 - anonymized data related to promotional markdowns that Walmart is running. MarkDown data is only available after Nov 2011, and is not available for all stores all the time. Any missing value is marked with an NA.
* CPI - the consumer price index
* Unemployment - the unemployment rate
* IsHoliday - whether the week is a special holiday week

**train and test data after merging**
![image](https://user-images.githubusercontent.com/59472284/222876954-c4dd5b5b-9ece-4c2b-9c27-5565f99fb688.png)
![image](https://user-images.githubusercontent.com/59472284/222877026-e139a848-7c70-4287-aad3-b86ec235b168.png)

**From EDA we select following questions**
![image](https://user-images.githubusercontent.com/59472284/222877091-ace01a76-6333-47fd-be11-110bdd705334.png)

## summary of data
**1.Sales heavlly depend on Deptartment** \
**2.Size of store also play major role in sales big store usually have more weekly_sales**\
**3.A type store did more sales than b and c**\
**4.weekly sales also depend on week of the year holidays weeks are good for sales**\
**5.final submission is with RandomForest model with tunned hyperparameters**

Training pipeline
![image](https://user-images.githubusercontent.com/59472284/222877287-271779c5-1136-4764-9f5b-bf90ddd016af.png)

**Streamlit app**
![image](https://user-images.githubusercontent.com/59472284/222886472-ab261ad7-f960-454e-8473-6690ffe2f29d.png)

![image](https://user-images.githubusercontent.com/59472284/222886787-4df8b914-21cd-4e01-a6af-74ad53f83bc3.png)


