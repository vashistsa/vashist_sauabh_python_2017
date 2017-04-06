
# coding: utf-8

# # Task
# 1. filter data by calender year and find average salary for every employee
# 2. find people wha have overtime salary greater than 5%
# 3. calculate percentage of total benefits wrt total compensation
# 4. generate csv

# In[1]:

import os
import pandas as pd


# In[8]:

currDir = os.getcwd()
currDir = os.getcwd()
df = pd.read_csv(currDir+'/Assignment3/employee_compensation.csv')
df.head(5)


# In[9]:

dfCalen = df[(df['Year Type'] == 'Calendar')]
dfCalen.head(5)


# In[11]:

dfReq = dfCalen[['Job Family','Employee Identifier','Salaries','Overtime','Other Salaries','Total Salary','Retirement','Health/Dental','Other Benefits','Total Benefits','Total Compensation']]
#calculate average on each column
dfReq = dfReq.groupby(['Employee Identifier','Job Family']).mean()
dfReq.head(5)                                                  


# In[16]:

# Expression for overtime salary > 5% 
dfsal = dfReq[dfReq['Overtime'] > 0.05*dfReq['Salaries']]        
dfsal = dfsal.reset_index(drop=False)
df1= dfsal[['Job Family','Total Benefits','Total Compensation']]
df1.head()


# In[18]:

output = df1.groupby(['Job Family']).mean()
#Adding Percentage column to output
output['Percent_Total_Benefit'] = output['Total Compensation'] / output['Total Benefits']

output.head()


# In[19]:

#Function to check if directory already exists, if not then create one
def checkDir(path):
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    
outPath = currDir + "/Assignment3(Results)/Q2_Part2.csv"
checkDir(outPath)
#create csv file
output.to_csv(outPath, index=False, encoding='utf-8')


# In[ ]:



