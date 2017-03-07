# Midterm

> There were analysis done on 2 types of dataset
  - Enron Dataset
  - NYT Dataset
    - Archive API
    - Article Search API

# Analysis on Enron Dataset

## About
The Enron scandal, publicized in October 2001, eventually led to the bankruptcy of the Enron Corporation, an American energy company based in Houston, Texas, and the de facto dissolution of Arthur Andersen, which was one of the five largest audit and accountancy partnerships in the world.

## Analysis 1

### Purpose
Purpose of this analysis is to access the Enron's email and find useful information. It is to find the total count of emails sent from enron's employee for each month. This gives us a subset of emails to parse through and set the priorities to emails.

### Steps
  
#### Data Preparation
- GLOB
- OS
- Email Parser

#### Extraction and Transformation
- extract the users list in mail directory.
- use email parser to parse through dates emails were sent.
- clean the dates and store in dates list.
- Setting the priority to each month as per their frequency

#### Output
- count the frequency of dates in list.
- The output represents the total mails sent during particular month.
- CSV file at location: 'C:\Users\DELL PC\midterm\que[1-2]\ana_[1-3]'
- plot showing total mails sent during particular month.
- saved plot at location: 'C:\Users\DELL PC\midterm\que[1-2]\ana_[1-3]'

#### Conclusion
- Based on the analysis done on sent items, it tells that the entities related to the company sent most of the emails on Jan2002, Mar2001, Feb2001, Nov2000 etc.
- This clearly raises the flag that the company was going through alot of suspecious activities during these months as compared to other months.
- It is important to go through the emails of respective first because this is the duration when the company was going through chaos.

## Analysis 2

### Purpose
The purpose of this analysis is to find the useful information company was trying to hide by deleting emails. During this analysis we will find the months during which fraudulent activities were going through. Later during this analysis we will be looking at the keywords which showed up frequently to gain more knowledge on the issue.

### Steps
  
#### Data Preparation
- GLOB
- OS
- Email Parser

#### Extraction and Transformation
- extract the users list in mail directory.
- use email parser to parse through dates emails were deleted.
- clean the dates and store in dates list.

- extract the users list in mail directory.
- use email parser to parse through contents of the emails were deleted.
- clean the data and store in data list, word by word and store them in text file.

#### Output
- count the frequency of words in list.
- The output represents the frequency of words in those emails mails deleted during particular month.
- count the frequency of dates in list.
- The output represents the total mails deleted during particular month.
- Plot showing total count of emails deleted every month
- csv file at location: 'C:\Users\DELL PC\midterm\que[1-2]\ana_[1-3]'
- Saved plot at location: 'C:\Users\DELL PC\midterm\que[1-2]\ana_[1-3]'



#### Conclusion
- Based on the analysis done on deleted items, it tells that the entities related to the company deleted most of the emails    on Jan2002 and Nov2001.
- This clearly raises the flag that the company was trying to hide some important information during these months.
- It is important to go through the deleted emails of Jan2002 and Nov2001 first because this is the duration when the            company proved to be fraud.
- The second analysis provides the top 500 words from the deleted emails. Words like:
    - TD: 107176(oronto-Dominion Bank paid $130-million (U.S.) to settle claims relating to the demise of Enron Corp
    - gas: 27689
    - yahoo: 5698
    - debt: 5698
    - aol: 5887 etc.
- Analyzing these words can help in finding information company didnt want anybody to know.


## Analysis 3

### Purpose
The purpose of this analysis is to go through all the folder os CEO Lay-K and find useful information. During this analysis we will find the employees who sent mail to the CEO and the recipient's of CEO's mails. This way we can connect the dots and find possible people involved in this fraud.

### Steps
  
#### Data Preparation
- GLOB
- OS
- Email Parser
- re
- stopwords
- nltk

#### Extraction and Transformation
- Set the userPath to Lay-k's directory.
- Go through each folder for his directory and using email parser, extract the senders.  
- Loop in all the folders in mail directory of Lay-k.
- use email parser to parse through contents of the emails were sent or deleted or inboxed(all possible data).
- clean the data and store in data list, word by word and store them in text file.

#### Output
- Count the top 20 senders.
- Count the top 20 receivers.
- count the frequency of words in deleted emails.
- The output represents the frequency of words in those deleted emails mails.

#### Conclusion
1. It is important to analyze Enron's CEO's profile as a part of this project.
2. The top sender's list provides the list of people who were in direct frequent contact during the scam.
3. The top receiver's list provides the list of people with whom the CEO was in direct frequent contact during the scam.
4. The pupose of last activity was to find the top used words used by the CEO during this period.
5. Words like energy and company tells that enron was an energy company.
6. Frequent use of california tells about the shortage of electricity supply caused by market manipulations, illegal[5] shutdowns of pipelines by the Texas(Houston word used frequently) energy consortium Enron.
7. declared and bankruptcy has been used frequently as well.
