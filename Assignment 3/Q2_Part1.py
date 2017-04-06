
# coding: utf-8

# # Tasks
# 1. Find out highest paid department in each organization.
# 2. Generate csv output

# In[1]:

#Import libraries
import os
import pandas as pd


# In[2]:

#Current Directory
currDir = os.getcwd()
#Read CSV
df = pd.read_csv(currDir+'/Assignment3/employee_compensation.csv', usecols=[3,5,21])
df.head(5)


# In[25]:

#Groupby on Organization Group and Department and finding the average compensation
compensation = df.groupby(['Organization Group', 'Department']).mean()
compensation = compensation.reset_index()
compensation.head()


# In[23]:

#Sort the output
output = compensation.sort_values(['Organization Group','Total Compensation'],ascending = [True, False])
output.head()


# In[22]:

#Function to check if directory already exists, if not then create one
def checkDir(path):
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    
#Generate csv
outPath = currDir + "/Assignment3(Results)/Q2_Part1.csv"
checkDir(outPath)
output.to_csv(outPath, index=False, encoding='utf-8')

