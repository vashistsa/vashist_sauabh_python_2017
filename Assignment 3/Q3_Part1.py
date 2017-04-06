
# coding: utf-8

# # Tasks
# 1. Calculate Avg. scores for each time those hosted and won match.
# 2. Generate a csv output.

# In[1]:

import os
import pandas as pd


# In[4]:

#Current Directory
currDir = os.getcwd()
#Read CSV
df1 = pd.read_csv(currDir+'/Assignment3/cricket_matches.csv', usecols=[6,7,8,12,13,17,18])
df1.head(5)


# In[14]:

#for Inning 1 and Inning 2 winners and hosts
winIN1 = df[(df['home'] == df['winner']) & (df['winner'] == df['innings1'])]
winIN2 = df[(df['home'] == df['winner']) & (df['winner'] == df['innings2'])]


# In[19]:

#run for teams those hosted and won innings
df1 = pd.DataFrame({'Home': winIN1['home'], 'Runs': winIN1['innings1_runs']})
df2 = pd.DataFrame({'Home': winIN2['home'], 'Runs': winIN2['innings2_runs']})
#Appending 2 data frames in 1
homeRuns = df1.append(df2, ignore_index=True)
homeRuns.head()


# In[24]:

#count the total home 
hG = homeRuns['Runs'].groupby(homeRuns['Home']).count()
#Total Runs
rG = homeRuns['Runs'].groupby(homeRuns['Home']).sum()


# In[32]:

#create new dataframe
col = ['Home', 'Score']
score = pd.DataFrame({'Home' : hG.index, 'Score' : rG / hG})
score.head()


# In[34]:

#Function to check if directory already exists, if not then create one
def checkDir(path):
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    
outPath = currDir + "/Assignment3(Results)/Q3_Part1.csv"
checkDir(outPath)
#create csv file
score.to_csv(outPath, index=False, encoding='utf-8')

