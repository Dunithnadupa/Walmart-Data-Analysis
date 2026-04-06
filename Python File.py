# Step1 - Data Exploration & Loading 

# importing Dependencies

import pandas as pd 

# mySql toolkit 

import pymysql  #this will work as a adapter 
from sqlalchemy import create_engine

#psql

import psycopg2 

df=pd.read_csv('Walmart.csv',encoding_errors='ignore')
print(df.shape) #chech the total rowns and total elemnets 

print(df.head())

print(df.describe()) #to find some statistics 

print(df.info()) #to find the data Type 

df.drop_duplicates(inplace=True) #Remove Duplicate Values 
df.duplicated().sum() #to find any duplicate values and find how many of them 

print(df.shape) #to cheack the total data after removing the duplicate values 

print(df.isnull().sum()) #to find missing values 

# Dropping all records with missing values

df.dropna(inplace=True)
print(df.isnull().sum())  # to verify if the missing values are dropped 
print(df.shape)

df['unit_price']=df['unit_price'].str.replace('$',' ').astype(float)   #Remove the $ sign in Unit_price and change the data type str--->float
print(df.head())
print(df.info())  #cheack new data type of unit_price 

print(df.columns)  #to view the all the columns in the dataset 

df['total'] = df['unit_price'] * df['quantity']   # Create a new Column called "total"
print(df.head())

# Making a connection with SQL ;

# ---> mysql <-----
# host = localhost
# port = 3306
# user = root 
# password = 'your_Password'

# ---> psql <-----
# host = localhost
# port = 5432
# user = postgres
# password = 'your_Password'

print(df.shape)

# Cleaned Data File 

df.to_csv('walmart_clean_data.csv', index=False)    

# mySQL Connection 
# mysql+pymysql://user:password@localhost:3306/db_name

engine_mysql =create_engine("mysql+pymysql://root@localhost:3306/walmart_db")

try:
    engine_mysql
    print("Connection Scucess to mysql")

except:
    print("Unable to Connect")

df.to_sql(name='walmart',con=engine_mysql,index=False)

print(df.shape)

df.columns = df.columns .str.lower()
print(df.columns)

















