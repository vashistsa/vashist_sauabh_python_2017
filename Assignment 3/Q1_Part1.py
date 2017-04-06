
# coding: utf-8

# # Tasks
# 1. Find % of collisions in Manhattan out of all collisions in NYC.
# 2. Generate CSV.

# In[47]:

#Import libraries
import os
import pandas as pd
from pandas import DataFrame


# In[28]:

#Current Directory
currDir = os.getcwd()
#Read CSV
df = pd.read_csv(currDir+'/Assignment3/vehicle_collisions.csv', usecols=[0,1,3], parse_dates=['DATE'])
df.head(5)


# In[11]:

#fETCHING data for yeae 2016
df = df[df.DATE.dt.year == 2016]
df.head(5)


# In[13]:

# Offsetting the warning
pd.options.mode.chained_assignment = None

#Fetching month from Date Column
df['MONTH'] = df['DATE'].dt.strftime('%b')
df.head(5)


# In[18]:

#Groupby on Month and count total accidents
NYC = df['UNIQUE KEY'].groupby(df['MONTH'], sort=True).count()
#Month Sort
NYC.index = pd.CategoricalIndex(NYC.index, 
                               categories=['Jan', 'Feb', 'Mar', 'Apr','May','Jun', 'Jul', 'Aug','Sep', 'Oct', 'Nov', 'Dec'], 
                               sorted=True)
NYC = NYC.sort_index()
NYC


# In[21]:

#Groupby on Month and count total accidents
MANHATTAN = df['UNIQUE KEY'][df['BOROUGH'] == "MANHATTAN"].groupby(df['MONTH'], sort=True).count()
#Month Sort
MANHATTAN.index = pd.CategoricalIndex(MANHATTAN.index, 
                               categories=['Jan', 'Feb', 'Mar', 'Apr','May','Jun', 'Jul', 'Aug','Sep', 'Oct', 'Nov', 'Dec'], 
                               sorted=True)
MANHATTAN = MANHATTAN.sort_index()
MANHATTAN


# In[29]:

Col = ["MONTH", "MANHATTAN", "NYC", "PERCENTAGE"]
#creating new data frame
dataFrame = pd.DataFrame({'MONTH' : NYC.index, 'MANHATTAN' : MANHATTAN, 'NYC' : NYC, 'PERCENTAGE' : MANHATTAN/NYC})
output = dataFrame[Col]
output.head(20)


# In[67]:

#Function to check if directory already exists, if not then create one
def checkDir(path):
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    
outPath = currDir + "/Assignment3(Results)/Q1_Part1.csv"
checkDir(outPath)
#create csv file
output.to_csv(outPath, index=False, encoding='utf-8')


# In[ ]:



