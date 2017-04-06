
# coding: utf-8

# # Tasks
# 1. For each Borough find out distribution of each collision scale
# 2. Generate CSV.

# In[1]:

import os
import pandas as pd
from pandas import DataFrame


# In[3]:

#Import libraries
currDir = os.getcwd()

#Import libraries
df = pd.read_csv(currDir+'/Assignment3/vehicle_collisions.csv', usecols=[0,3,19,20,21,22,23])
df.head(5)


# In[26]:

#DF to have all vehicle columns
df_vehicles = df[['VEHICLE 1 TYPE','VEHICLE 2 TYPE','VEHICLE 3 TYPE','VEHICLE 4 TYPE','VEHICLE 5 TYPE']]
#DF to have all locations in BOROUGH
df_locations = df[['UNIQUE KEY','BOROUGH']]
#Take only not Null Values from vehicles
df_case = df_vehicles.notnull()
#Assign 0 and 1 to NaN values
df_case = df_case.applymap(lambda x:1 if x else 0)
#concatenate 2 DFs
df_case = pd.concat([df_locations, df_case], axis=1)
df_case.head(5)


# In[27]:

#Groupby on Borough to total the vehicles invloved
output = df_case.groupby(df_case['BOROUGH']).sum()
output


# In[30]:

#New DF for the output
Col = ['Borough', 'One_Vehicle_Involved', 'Two_Vehicle_Involved', 'Three_Vehicle_Involved', 'more_Vehicle_Involved']
result = pd.DataFrame({'Borough' : output.index, 'One_Vehicle_Involved' : output['VEHICLE 1 TYPE']-output['VEHICLE 2 TYPE'], 
                           'Two_Vehicle_Involved' : output['VEHICLE 2 TYPE']-output['VEHICLE 3 TYPE'], 'Three_Vehicle_Involved' : output['VEHICLE 3 TYPE']-output['VEHICLE 4 TYPE'],
                           'more_Vehicle_Involved' : output['VEHICLE 4 TYPE'] })
result[Col].head()


# In[31]:

#Function to check if directory already exists, if not then create one
def checkDir(path):
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    
outPath = currDir + "/Assignment3(Results)/Q1_Part2.csv"
checkDir(outPath)
#create csv file
output.to_csv(outPath, index=False, encoding='utf-8')


# In[ ]:



