
# coding: utf-8

# # Task
# 1.Extract data from Awards column and split it into multiple columns
# 2. Create nominated and won column for different awards and fill the data
# 3. Generate csv file
# 

# In[13]:

import os
import numpy as np
import pandas as pd
import warnings


# In[29]:

#Import libraries
currDir = os.getcwd()

# Read CSV file
df = pd.read_csv(currDir+'/Assignment3/movies_awards.csv', usecols=[5,15])
#drop null values
df = df.dropna()
df.head()


# In[30]:

#create various columns based on string extracted from Awards column
df['Awards_Won'] = df['Awards'].str.extract('(\d+ win)', expand=True)
df['Awards_Nominated'] = df['Awards'].str.extract('(\d+ nomination)', expand=True)
df['Prime_Awards_Nominted'] = df['Awards'].str.extract('(Nominated for \d+ Primetime Emmy)', expand=True)
df['Oscar_Awards_Nominated'] = df['Awards'].str.extract('(Nominated for \d+ Oscar)', expand=True)
df['Golden_Awards_Nominated'] = df['Awards'].str.extract('(Nominated for \d+ Golden Globe)', expand=True)
df['BAFTA_Awards_Nominated'] = df['Awards'].str.extract('(Nominated for \d+ BAFTA)', expand=True)
df['Prime_Awards_Won'] = df['Awards'].str.extract('(Won \d+ Primetime Emmy)', expand=True)
df['Oscar_Awards_Won'] = df['Awards'].str.extract('(Won \d+ Oscar)', expand=True)
df['Golden_Awards_Won'] = df['Awards'].str.extract('(Won \d+ Golden Globe)', expand=True)
df['BAFTA_Awards_Won'] = df['Awards'].str.extract('(Won \d+ BAFTA)', expand=True)
df.head(5)


# In[31]:

warnings.filterwarnings('ignore')
#Fetch string and storing
df['Awards_Won'] = df['Awards_Won'].str.extract('(\d+)')
df['Awards_Nominated'] = df['Awards_Nominated'].str.extract('(\d+)')
df['Prime_Awards_Nominted'] = df['Prime_Awards_Nominted'].str.extract('(\d+)')
df['Oscar_Awards_Nominated'] = df['Oscar_Awards_Nominated'].str.extract('(\d+)')
df['Golden_Awards_Nominated'] = df['Golden_Awards_Nominated'].str.extract('(\d+)')
df['BAFTA_Awards_Nominated'] = df['BAFTA_Awards_Nominated'].str.extract('(\d+)')
df['Prime_Awards_Won'] = df['Prime_Awards_Won'].str.extract('(\d+)')
df['Oscar_Awards_Won'] = df['Oscar_Awards_Won'].str.extract('(\d+)')
df['Golden_Awards_Won'] = df['Golden_Awards_Won'].str.extract('(\d+)')
df['BAFTA_Awards_Won'] = df['BAFTA_Awards_Won'].str.extract('(\d+)')
df.head(5)


# In[32]:

#remove NaN
df['Awards_Won'] = df['Awards_Won'].fillna(0)
df['Awards_Nominated'] = df['Awards_Nominated'].fillna(0)
df['Prime_Awards_Nominted'] = df['Prime_Awards_Nominted'].fillna(0)
df['Oscar_Awards_Nominated'] = df['Oscar_Awards_Nominated'].fillna(0)
df['Golden_Awards_Nominated'] = df['Golden_Awards_Nominated'].fillna(0)
df['BAFTA_Awards_Nominated'] = df['BAFTA_Awards_Nominated'].fillna(0)
df['Prime_Awards_Won'] = df['Prime_Awards_Won'].fillna(0)
df['Oscar_Awards_Won'] = df['Oscar_Awards_Won'].fillna(0)
df['Golden_Awards_Won'] = df['Golden_Awards_Won'].fillna(0)
df['BAFTA_Awards_Won'] = df['BAFTA_Awards_Won'].fillna(0)
df.head(1000)


# In[33]:

warnings.filterwarnings('ignore')
#convert string to integer
df['Awards_Won'] = df['Awards_Won'].astype(int)
df['Awards_Nominated'] = df['Awards_Nominated'].astype(int)
df['Prime_Awards_Nominted'] = df['Prime_Awards_Nominted'].astype(int)
df['Oscar_Awards_Nominated'] = df['Oscar_Awards_Nominated'].astype(int)
df['Golden_Awards_Nominated'] = df['Golden_Awards_Nominated'].astype(int)
df['BAFTA_Awards_Nominated'] = df['BAFTA_Awards_Nominated'].astype(int)
df['Prime_Awards_Won'] = df['Prime_Awards_Won'].astype(int)
df['Oscar_Awards_Won'] = df['Oscar_Awards_Won'].astype(int)
df['Golden_Awards_Won'] = df['Golden_Awards_Won'].astype(int)
df['BAFTA_Awards_Won'] = df['BAFTA_Awards_Won'].astype(int)
df.head(5)


# In[43]:

#total awards nominated
df['Awards_Nominated'] = df['Awards_Nominated'] + df['Prime_Awards_Nominted'] + df['Oscar_Awards_Nominated'] + df['BAFTA_Awards_Nominated']+df['Golden_Awards_Nominated']
#total awards won
df['Awards_Won'] = df['Awards_Won'] + df['Prime_Awards_Won'] + df['Oscar_Awards_Won'] + df['BAFTA_Awards_Won']+df['Golden_Awards_Won']
col = ['Awards_Won', 'Awards_Nominated', 'Prime_Awards_Nominted', 'Oscar_Awards_Nominated', 'Golden_Awards_Nominated', 'Oscar_Awards_Nominated', 'BAFTA_Awards_Nominated', 'Prime_Awards_Won', 'Oscar_Awards_Won', 'Golden_Awards_Won', 'BAFTA_Awards_Won']
df[col].head().to_string(index=True)


# In[41]:

#Function to check if directory already exists, if not then create one
def checkDir(path):
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    
outPath = currDir + "/Assignment3(Results)/Q4_Part1.csv"
checkDir(outPath)
#create csv file
df[col].to_csv(outPath, index=False, encoding='utf-8')


# In[ ]:



