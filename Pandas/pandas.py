# Why need Pandas?
# Efficient and optimized Data structures
# Faster and efficient data handling
# Built on top of NumPy, making it much faster
# Descriptive Statistics and Analytics
# Excel, CSV, Json, SQL, Text, XML file handling

# CSV File: Comma Separated Values (Used in Research fields extensivey)
        # (Opens directly in Excel)
        # e.g.: name,age,city
        #       John Doe,20,New York
        #       Jane Smith,22,Los Angeles


# TSV File: Tab Separated Values (Doesn't open in excel but can be used in Python)
          # e.g:  name	age	city
          #       John Doe	20	New York
          #       Smith	22	Los Angeles


# JSON : JavaScript Object Notation 
# {
#   "name": "John Doe",
#   "age": 20,
#   "enrolled": true,
#   "subjects": ["Math", "Physics"]
# }

# Accessing File
# pd.read_csv('file.csv')
# pd.read_csv('file.tsv', sep='\t')
# pd.read_csv('file.txt', sep=':')
# pd.read_csv('file.txt', sep=';')

import pandas as pd
# to read csv files:
pd.read_csv('name.csv')

# To read TSV files:
pd.read_csv('name.tsv', sep="\t") 
# read_csv use korte hobe tsv er khettreo

# To Access Json file:
pd.read_json('name.json')


# To Access Json file:
pd.read_json('name.json')

# Series
# • one-dimensional
# • array-like structure;
# • can hold elements of any data type
# • similar to a column in an Excel sheet
# pd.Series([list values])
# pd.Series([list of values], index=[list of indexes])

li= [1,2,3,4,5]
# Series:
pd.Series(li)
# indexing in series:
# a,b,c...
pd.Series([1,2,3,4,5],['a','b','c','d','e'])

# DataFrameL
# 1. Two-dimensional (2D)
# 2. Tabular data structure with labeled axes (rows and
# columns).
# 3. Like an Excel spreadsheet 

# Creating DataFrame:  
# By accessing files:
  # df = pd.read_csv('file.csv')


df= pd.read_csv('name.csv')
df

# Dictionary to dataframe:
data={
    'Name' : ['Mahtab','Haque','Angkon'],
    'Age' : ['20','21','22'],
    'City' : ['Dhaka','Chittagong','Dhaka']
}
df=pd.DataFrame(data)
df
#2D List to DataFrame:
data = [
    ['Alice',25,'New York'],
    ['Bob',30,'Los Angeles'],
    ['Charlie',35,'Chicago']
]
df=pd.DataFrame(data,columns=['Name','Age','City'])
df


# Numpy array to Df
import numpy as np
data = np.array(
    [
        [2108008,21,8],
        [2208008,22,8],
        [2308008,23,8]
    ]
)
df = pd.DataFrame(data,columns=['ID','Batch','ID in Short'])
df



# Dataset Preview

# • df.columns()
# returns all the column names of that dataset as a list

# • df.head(n)
# returns first n rows of dataframe

# • df.tail(n)
# returns last n rows of dataframe

# • df[columns_name].value_counts()
# returns the frequency of each values in that column

# IPL Dataset
df = pd.read_csv('IPL_Ball_by_Ball_2008_2022.csv')
df


df.columns

df.head(4)

df.head() 
# n=5 (first 5)

df.tail()
# n=5 (last 5)


# Value Counts:
# Suppose, which batsman has played the most deliveries from 2008-2012?
df['batter'].value_counts()

# kon type er wicket beshi hoise?
df['kind'].value_counts()



# If there's any missing values:
# isnull and notnull
# • df.isnull()
# • df.isnull().sum()
# • df.isnull().sum().sum()
# • df.notnull()
# • df.notnull().sum()
# • df.notnull().sum().sum()


df.isnull()

# Total Null Values in each catagories:
df.isnull().sum()

# Total Null values:
df.isnull().sum().sum()

# Which values are not null:
print(df.notnull())
# total: 
print(df.notnull().sum())
print(df.notnull().sum().sum())




# dropna : To drop null values
# • df.dropna()
# • df.dropna(axis=1)
# • df.dropna(subset=[column_names])
# • df.dropna(inplace = True)

df1= df.dropna()
# it will drop a whole row that contains null values
df1 


# to drop columnwise:
df2=df.dropna(axis=1)
print(df2)
# to drop rowwise: Default
df3=df.dropna(axis=0)
print(df3)


# <!-- to remove columns with null values by specifying names:-->

df.dropna(subset=['extra_type','kind'])
df


# to make the drop parmanant:
df.dropna(inplace=True)
df


# fillna
# • df.fillna(value)
# • df.fillna({column1: value1, column2: value2})
# • df.fillna(method='ffill')
# • df.fillna(inplace=True)

# To replace all the null values with anything:
df.fillna(0)

df.fillna({"player_out": "None","Kind":"No Wicket"})

# To fillup a null value with the previous value of the same column:
df.fillna(method="ffill")

# To fillup a null value with the next value of the same column:
df.fillna(method="bfill")



# replace
# • df.replace(to_replace= 'value' , value = 'new_value' )
# • df.replace('value', 'new_value')


df.replace(to_replace= 'I SHarma' , value = 'Ishant Sharma' )
# in shortcut:
df.replace('A Kumble' , 'Mahtab Haque' )

