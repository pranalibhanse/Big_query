# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

import os

# Python package for bigquery.
import bq_helper

#Create helper object for bigquery
hacker_news = bq_helper.BigQueryHelper(active_project= "bigquery-public-data",
                                        dataset_name = "hacker_news")

#list all the tables in the hacker_news dataset
hacker_news.list_tables()

#Search for indivaidual table
hacker_news.table_schema("full")

#To check first couple of lines in "full" table
hacker_news.head("full")

#to see first 10 enries in the column ("by")
hacker_news.head("full",selected_columns="by",num_rows=10)

#to check size of the query, first me wwite query
query = """SELECT score
            FROM `bigquery-public-data.hacker_news.full`
            WHERE type = "job" """
hacker_news.estimate_query_size(query)

# only run this query if it's less than 100 MB
hacker_news.query_to_pandas_safe(query, max_gb_scanned=0.1)
hacker_news.score_counts().head()

#checking
job_scores = hacker_news.query_to_pandas_safe(query)

# average score for job posts
job_scores.score.mean()

# save our dataframe as a .csv
job_scores.to_csv("job_scores.csv")

# What five score have the most measurements taken there
job_scores.score.value_counts().head()





















