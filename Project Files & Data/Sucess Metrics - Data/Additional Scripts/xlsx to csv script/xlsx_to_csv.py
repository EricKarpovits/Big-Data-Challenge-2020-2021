#importing pandas as pd 
import pandas as pd 
  
# Read and store content of an excel file  
read_file = pd.read_excel ("xlsx/academic_performance_US.xlsx") 
  
# Write the dataframe object into csv file format 
read_file.to_csv ("csv/academic_performance_data_US.csv", index = None, header=True) 
    
# read csv file and convert into a dataframe object 
df = pd.DataFrame(pd.read_csv("csv/academic_performance_data_US.csv")) 
  
# show the dataframe 
df