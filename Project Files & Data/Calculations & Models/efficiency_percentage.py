# High School Big Data Challenge 2020-2021 - Effieciency Metric Function - Deniz Jasarbasic

import math
import pandas as pd
import csv

# This can be edited based on which metrics and data sets we analyze
fields = ["US Graduation Rates", "Canada Graduation Rates"]

# Loading csv contents into dataframe
df = pd.read_csv('data_file,csv')
metric_name = df.Names
metric_column_a = df["2017_graduation_rates_us"].mean()
metric_column_b = df["2017_graduation_rates_canada"].mean()

# Determine greatest and smallest value
if (metric_column_a > metric_column_b):
    greateast_metric_result = metric_column_a
    smallest_metric_result = metric_column_b

else:
    smallest_metric_result = metric_column_a
    greateast_metric_result = metric_column_b


# Efficiency Percentage Calculations:
def efficiency_percentage():
    
    difference_metric = greateast_metric_result - smallest_metric_result
     
    result = ((difference_metric)/(smallest_metric_result))*100

    return result

# Output result:
print(metric_name, ": ", efficiency_percentage())