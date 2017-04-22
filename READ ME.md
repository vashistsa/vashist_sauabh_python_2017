# Final Project 

## Synopsis: 
As a part of Final Project, I have analyzed the impact of war like situations around the world. I am comparing the stocks of 
US Military arm manufacturer "General Dynamics" to those of who were not the part of Afghan War 2002. As this event took place in 2002 when
the social media was not at boom and still in its early phase, people relied on news internet portals or the newspapers. In this project,
I have analyzed the what was the ratio of articles on war to the other articles. Data Gather:
- Yahoo Stock Finance for 4 major Arms Manufacturers during 2002.
- NYT articles in JSON format for that period.
- NYT stocks data then and now.

# 1- Analysis on Arms Manufacturers
- More Information About General Dynamics role in Afghan War 2002-(https://en.wikipedia.org/wiki/General_Dynamics_F-16_Fighting_Falcon_operational_history)
- There are 2 analysis involved, comparing General Dynamics stocks to other arms manufacturers stocks.
- In order to fetch data from Yahoo! Finance following steps have been taken.
  - $ pip install yahoo-finance
  - $ pip install ystockquote
  - import ystockquote
  - from yahoo_finance import Share

## Analysis 1 
The Aim of Analysis 1 is to find the impact of war like situations on the stock market of Arm Manufacturers proving US govt arms. Basis of this analysis is the information gathered from knowledge that General Dynamics was the primary provider of TOMAHAWK Missiles to US and UK Govt. Total of 109 Tomahawk missiles were used during Afghan War 2002 with total cost of $150 Million. Other Arms providers used in the Analysis are Raytheon, Lockheed Martins and Boeing.


### Steps Taken

#### Data Preparation
Packages Used -:
- Yahoo_Finance
- OS
- time
- CSV
- Pandas
- Numpy
- Plotly
- ystockquote

#### Data Extraction
- Import Yahoo_Finance python package.
- Store the stock data in CSV.
- Dataframes were created for each dataset.

#### Data Transformation
- Normalized the data to plot "Bell-Curve".

#### Output
- Plots at 'final\Analysis\ana_[1-3]'
- CSV File at 'final\extra'

## Plot 1


## Inference
The plot encapsulates the steep rise in the value of the mentioned organizations due to the utilization of weapons in the Afghanistan war inflating the demand vs supply ratio.

## Plot 2


## Inference
- As the first plot describes the rise in value of stocks, high volumes of shares are traded on the New York Stock Exchange. 
- The normal distribution of the mentioned companies shows a right skewed shift. 
- It indicates a trend of buying a stock at a cheaper price to sell later at a projected surge price due to the ongoing war. 

#### Final Conclusion based on Analysis.
- A proof of concept is established over the problem statement. 
- After studying the plots over the timeline, a conclusion can be drawn marking a direct relation between the utlization of weapons in war zones and the simultaneous upswing in the stock value of the top four defense contractors of the United States of America.

## Analysis 2 
#### Data access - Enron Mail Dir.
#### Result Folder - [midterm/que[1-2]/ana_[1-3]/Top Employee/]
#### File Name (Midterm_Question 1 (Analysis 2 - Top Email Analysis).ipynb) stored in midterm/que[1-2]/ana_[1-3].ipynb/]
> In this Analysis-:
- I wil find TOP employee who recieved & sent most emails from directory of Half of Millions emails.
- Then will predict result on those TOP employees.
- Then will Analyse their emails on year basis.

### Step 1 (Data Preperation)
Packages Used -:
- GLOB
- OS
- Email Parser

I have read "ALL" folder of all Employees from the data provided by professor.
```
1- Initially the data was in MIME type format.
2- Lopped through each email and sent to Email Parser (get_payload()) in order to get the "To" & "FROM".
3- Stored TO & FROM of all emails in two different List.
```

### Step 2 (Cleaning & Preprocessing)
Packages Used -:
- RE

In this step I have replaced all the tab's, newlines and spaces.
```
1- Looped through the List to remove all stab's, newlines and spaces.
```

### Step 3 (Finding Top 10 from LIST & thier Count)
Packages Used -:
- Counter
- Collections

In this step I have Found the TOP to & from emp emails.
```
1- Looped through the List to find top 10 using Counter Counter(to_email_list).most_common(10).
```
See attached Pic.
<img src ="que[1-2]/ana_[1-3]/Top Employee/result/count.PNG" />
```
After Seeing above result.
- We can Predict -: (To Email)
    - The top person is Richard Shapiro.
    - He was the Vice President and lobbyist (“bribery guy”) for Enron.
    - A lot of his emails are about handing dollars to politicians, and getting favourable laws passed.
    - The fact that he received the most emails shows he was in touch with everything that was happening.
    
- (From Email)
    - Kay Mann, He is the head of legal for Enron.
    - The fact that she sent so many emails is ironical, seeing as how Enron was breaking every law in the book 
      keep in mind that most employees, including Kay Mann, were innocent.
    - Only the top executives were guilty, and most went to prison.
    
    
- Funny Fact:
   - A company with such a active legal department, and yet the executives ignored (or didn’t care) about the law at all. 
```

### Step 4 (Analysis on above result)
Packages Used -:
- CSV

In this step, I am going to analyse all emails of employee in each category w.r.t year.
```
1- Created List of emp name empList = ['shapiro-r', 'mann-k'].
2- I looped thorugh each employee all folder and saved date in two different list.
3- Date was in word format but I formatted and collected year with count of emails of each employee.
4- I stored Year and Count in CSV format that can be find here [midterm/que[1-2]/ana_[1-3]/Top Employee/emp/*.csv]
```

### Step 5 (Reading CSV file and Plotting on Pie Chart)
Packages Used -:
- Matplotlib

In this step, I read csv data from csv file and plotted on pie chart.
```
1- Used Matplotlib library to conert number in to % to plot % of emails in particulat year.
2- These files are stored in [midterm/que[1-2]/ana_[1-3]/Top Employee/emp/result/*.png]
```
 see attached pic
<img src ="que[1-2]/ana_[1-3]/Top Employee/result/shapiro-r.png" /> 
<img src ="que[1-2]/ana_[1-3]/Top Employee/result/mann-k.png" />
 
### Conclusion from Above Analysis & Pictures
- As we know, The company went bankrupt in year 2001. So, it was obvious that the whole email transaction was occur in same year.
- Richard Shapiro, The company Vice President. We can see 94 % of email traffic in year 2001.
- Kay Mann, Legal Head. We can see 50% of email traffic, which shows he was not actual the part of Enron. But he was actively involved.

## Analysis 3 (This Analysis is based on Above Analysis.)
#### Data access - Enron Mail Dir.
#### Result Folder - [/midterm/que[1-2]/ana_[1-3]/Top Conversation/result/]
#### File Name (Midterm_Question 1 (Analysis 3 - Top Communication).ipynb) stored in midterm/que[1-2]/ana_[1-3].ipynb/]
```diff
+ NOTE-:
+ In this Analysis I also analysed all conversation of "146" employee w.r.t to half of million emails, 
+ which took "7 Hours" to run one loop. Means each employee is looping half of million emails which is (146*500,000 iterations).
+ I am attaching that pynb and csv file inside midterm folder. [midterm /que[1-2] / top conversation enron all emp.ipynb ]
+ CSV file [midterm / que[1-2] / conversation.csv]
+ I request you to please have a look. But the same is done for only 4 employee below.
+ CSV file explain sender 1 sent number of emails to sender 2.
+ Example - Lay sent 508 emails to Shapiro.
```
> In this Analysis-:
- This is based on above analysis in this I have taken TOP 2 (TO & From) employees and target is find who did the 
 most communication with whom.
- Then will plot the number on bar graph in order to show top communication.
- Then will Analyse about them.

### Step 1 (Data Preperation)
Packages Used -:
- GLOB
- OS
- Email Parser

I have read "ALL" folder of all Employees where the condition meet (Give me 'TO' where from is ['shapiro', 'dasovich', 'mann', 'kaminski'] these 4 is predicted on above analysis.).
```
1- Initially the data was in MIME type format.
2- Lopped through each email and sent to Email Parser (get_payload()) in order to get the "To" & "FROM".
3- Stored TO & FROM of all emails in two different List.
```
### Step 2 (Cleaning & Preprocessing)
Packages Used -:
- RE

In this step I have replaced all the tab's, newlines and spaces.
```
1- Looped through the List to remove all tab's, newlines and spaces.
```
### Step 3 (Finding Top 1 from LIST of all 4 & thier Count)
Packages Used -:
- Counter
- Collections

In this step I have Found the TOP person with related to 4 given names and thier count.
```
1- Looped through the List to find top 1 using Counter Counter(to_email_list).most_common(1).
```
See attached Pic.
<img src ="que[1-2]/ana_[1-3]/Top Conversation/result/conver.PNG" />
<img src="que[1-2]/ana_[1-3]/Top Conversation/result/percent.png" />
After Seeing above result.
- We can Predict -: 
  - From above Bar Graph & Pie Chart We can say.
  - Shapiro sent Steven around 477 emails which is 4.8%
  - Dasovich sent Shapiro around 3000 emails which is 29.6%
  - Mann sent Suzanne around 1600 emails which is 16.2
  - kaminski sent vkaminski around 4500 emails which is 49.4%
  
 #### Final Conclusion 
- As we know Shapiro recieved most number of emails in organization which was around 17000 from above 
  we can see around 20% was sent from   Dasovich.
- Mann recieved most emails but she was actively sending to other person and she was in TOP communication with Suzanne.
    
    
## Note-: In this Analysis I also did Solo Word Analysis on Enron CEO (Kennath Lay)
- Word Analysis is basically finding out the top words used by that person.
- I read all the emails of Kennath Lay in order to find word frequency.
- I gone through Data prepration til Data cleaning.

See attached Image-:
<img src="que[1-2]/ana_[1-3]/Top Conversation/result/kennathLay.PNG" />
#### Conclusion on Kennath Lay Analysis-:
- The Above result showing Top 50 words that was used in Kenneth Lay emails.
- After seeing this we can predict:
    - Words like "Energy and Communication" are expected, as thats what Ernon did.
    - Words like "Million, Millions, Stocks, and Bankruptcy" are occured which shows Kenneth was aware was this.
    - The word "California" is used more than 3000 times means Company had some bad history there.
    - The word "Meeting" is used more than 2000 times which shows Kenneth was the busy man.


# 2- Analysis on NYT API(Archive & User Comments)
- This Analysis is related to Articles & User Comments
- API key is save in Environment Variable.
- Note -: I have Done 2 Analysis on Archive & 1 Analysis on User Comments.

## Analysis 1 (This Analysis is based on Categories & based on Categories (Donal Trump(sub-categories Articles))
#### Data access folder - [/midterm/data/Archive/jsonData/]
#### Result Folder - [/midterm/que[1-2]/ana_[1-3]/Articles/]
#### File Name (Midterm_Question 2 (Analysis 1 - Articles & SubArticles).ipynb) stored in midterm/que[1-2]/ana_[1-3].ipynb/]

### Step 1 (Data Preperation)
Packages Used -:
- JSON
- OS
- Requests

I made an API call to NYT Archive website with month and year parameters.
I stored a data for Jan17.
```
1- Initially, I made an API call to NYT website to store data in JSON file in my local Directory.
2- I looped through that JSON file in order to find useful information related to articles.
3- Data I found through JSON is all stored in text files in directory. [midterm/data/Articles/*.txt].
4- Read that Text file and stored in one list.
```
### Step 2 (Preprocessing of Text Files)
Packges Used -:
- GLOB
- RE

In this step I have read text file and find all the useful information.
```
1- We Know Jan 17 was the presidential month, So I looped the text file in order to find all Politics Articles.
2- Removed all Punctuation from the List.
3- Found top 10 articles with their count.
```
### Step 3 (Preparing CSV File & Plots)
Packages Used-:
- Matplotlib
- CSV

In this, I have stored the Ranked list in CSV file and Read that file to plot top Articles on BAR Chart. 

```
1- Created a CSV file that contains top 10 articles with Rank w.r.t count.
2- Read CSV file in order to plot bar graph using Matplotlib.
```
see picture attached. 
<img src="que[1-2]/ana_[1-3]/Articles/result/percentTopic.png" />
- Result is stored in [que[1-2]/ana_[1-3]/Articles/result/percentTopic.png]

### Step 4 (Data Collection for Sub Articles w.r.t to President Donald Trump)
Packages Used-:
- Same as above.

In this, I have access the JSON file Headline and found all values that contains Donald Trump in it. 

```
1- Created a Text file and stored all keywords relate to sub category Donald.
```

### Step 5 (Cleanind & Preprocessing & sorting on the basis of Count)
Packages Used-:
- RE

In this, I have Read the Text file line by line. 

```
1- Read the text file line by line and removed all punctuation and tab's.
2- created a loop in order to find unique keywords.
3- used lambda function in order to find count and sort from top to bottom.
4- Looped through the sorted data to assign Rank from 1st to last and stored that in csv file.
```

### Step 6 (Reading CSV & Plotting Bar chart using Matplotlib)
Packages Used-:
- CSV
- Matplotlib

In this, I have Plotted a Bar chart showing "Number of Articles w.r.t Donald Trump. 

```
1- Read the CSV file and created base for Matplotlib BAr chart.
2- Plotted bar chart showing count on x-axis & sub category on y-axis.
```
see picture attached. 
<img src="que[1-2]/ana_[1-3]/Articles/result/keyWordsPercent.png" />
- Result is stored in [que[1-2]/ana_[1-3]/Articles/result/keyWordsPercent.png]

### Conclusion from Above Analysis
- NYT Posted total of 5206 Articles in JAN'17 out which.
- NYT Posted majority of articles related to Politics in Jan'17.
- Out of which major was related to Donald Trump.
- The Top most sub category was "UNited states and Politics" & Second Top was Presidential Election.

## Analysis 2 (Analysis to find the Top 10 Part of Speech in Article Lead Paragraph)
#### Data access folder - [/midterm/data/Archive/jsonData/]
#### Result Folder - [/midterm/que[1-2]/ana_[1-3]/Part of Speech/]
#### File Name (Midterm_Question 2 (Analysis 2 - Part of Speech).ipynb) stored in midterm/que[1-2]/ana_[1-3].ipynb/]
> In this Analysis-:
- I wil find Access json file in order to find all lead paragraphs.
- Will use NLTK wordnet(POS TAGS) in order to find top 10 Part of speech.
- Will Plot all part of speech on pie chart for distribution.

### Step 1 (Data Collection & Storing)
Packages Used -:
- Request
- JSON
- OS

I have read JSON file that I have dumped in above Analysis in order to find all Lead Paragraphs of Jan' 17 Articles..
```
1- I looped through that JSON file in order to find all 5206 Lead Paraghaph of articles.
2- Data I found through JSON is all stored in text files in directory. [midterm/data/Part of Speech/*.txt].
3- Read that Text file and stored in one list.
```

### Step 2 (Pre Processing & Cleaning)
Packages Used -:
- RE
- NLTK word_tokenization
- WORNET
- Collection

I have read Text file line by line in order to clean & store in list.
```
1- Looped through the text file in order to remove all Punctuations.
2- Used NLTK work Tokenize in order to divides a string into substrings by splitting on the specified string (defined in subclasses).
using word_tokenize(data).
3- Used NLTK POS TAG in order to processes a sequence of words, and attaches a part of speech tag to each word using nltk.pos_tag(words).
4- Used Counter in order to find the count of individual Part of Speech.
5- USed Collection in order to find TOP 10.
```


### Step 3 (CSV & Plotting Pie Chart)
Packages Used -:
- CSV
- MATPLOTLIB

I have Stored the data in csv in order to make base for pie chart.
```
1- Stored the data in csv file with label, count and explode factor.
2- Looped through csv file to create base for pie chart.
```
see attched image
<img src="que[1-2]/ana_[1-3]/Part of Speech/result/percentSpeech.png" />
- Result is stored in [que[1-2]/ana_[1-3]/Part of speech/result/percentSpeech.png]

### Conclusion from Above Analysis (we can predict)
- NYT use majority of NOUN words in all of thier articles.
- Second top majority is Proper Noun & Singular.
- Third majority is Preposition & Subordinating Conjunction.

## Analysis 3 (Count of +ve & -ve Words in User Comment API)
#### Data access folder - [/midterm/data/community/Json Data/] & [/midterm/data/AIFNN.txt]
#### Result Folder - [/midterm/que[1-2]/ana_[1-3]/wordAnalysis/]
#### File Name (Midterm_Question 2 (Analysis 3 - Count of +ve & -ve Words).ipynb) stored in midterm/que[1-2]/ana_[1-3].ipynb/]
> In this Analysis-:
- I will use Another NYT API related to USER Comments.
- Will use Word Tokenization & Sent Tokenization.
- Will use AIFNN file in order to find +ve & -ve Words Used.
- AIFNN file contains +ve & -ve Words on score of -5 to +5.
- Will plot -ve & +ve score on Scatter Plot.
- Will Display Pie chart showing % of +ve & -ve words used in User Comments.

### Step 1 (Data Collection & Storing)
Packages Used -:
- Request
- JSON
- OS

Requested DATA from NYT User Comment API.
```
1- I made an API call to NYT User Comment section.
2- I stored my key in Enviornment Variable of system.
3- This API gives data only for 1 day at a time but I looped through 31 days in order to get response for Jan' 17.
4- Data I found through JSON is all stored in JSON FILES in directory. [midterm/data/WordAnalysis/*.json].
```

### Step 2 (Data Preprocessing & Cleaning)
Packages Used -:
- RE
- JSON
- OS

Looped through each JSON files in order to find Comments.
```
1- I looped thorugh all JSON files in order to get Comment Body of all users.
2- Initailly, I stored all that list of comments in a list.
3- I looped through list to store all that comments in text file. [\midterm\que[1-2]\ana_[1-3]\wordAnalysis\userComments/listOfComments.txt]
```

### Step 2 (+ve & -ve Score building for each sentence)
Packages Used -:
- NLTK
- Word Tokenize
- Sent Tokenize
File Used-
- AIFNN.txt

Looped through stored text file in order to find score of sentences.
```
What is AIFNN.txt?
- AFINN is a list of English words rated for valence with an integer between minus five (negative) and plus five (positive). 
The words have been manually labeled by Finn Årup Nielsen in 2009-2011. The file is tab-separated. stored in [midterm/aifnn.txt]
1- I looped Aifnn.txt and created on Dictionary in order to store word with his value.
2- I read the text file and splitted each sentence using sen_tokenize.
3- Then i Splitted all words from that sentence.
4- Using that dictionary I found the score of each word in that sentence. This I have doen for all more than 750 Comments.
5- I store the count of +ve & -ve in words in form of tuple.
```
See attched image.
<img src="que[1-2]/ana_[1-3]/wordAnalysis/result/score.PNG" />
- Result is stored in [que[1-2]/ana_[1-3]/wordAnalysis/result/score.png]
- Above picture is showing count of +ve & -ve Score in each sentence. (Cumulative)
- Means in one sentence the score of +ve word is x and -ve word is y.


### Step 3 (Data writting to CSV & Plotting)
Packages Used -:
- CSV
- Matplotlib

Stored the list in csv in order to process for plots.
```
1- I Stored each tuple of +ve & -ve words in CSV file.
2- Read that csv file ir order to create base for scatter plot.
```
See attched image.
<img src="que[1-2]/ana_[1-3]/wordAnalysis/result/posNegGraph.png" />
- Result is stored in [que[1-2]/ana_[1-3]/wordAnalysis/result/posNegGraph.png]
- The above scatter is showing sentences w.r.t +ve & -ve words.
- Now, In next step I have plotted over all count of +ve & -ve Words on pie chart.
See attched image.
<img src="que[1-2]/ana_[1-3]/wordAnalysis/result/percentWord.png" />

### Conclusion from Above Analysis (we can predict)
- In january User use more -ve words w.r.t +ve words.
- The count of -ve word is more may be is vary month to month.
- After seeing scatter plot I can say for every sentence count of -ve words is more than +ve words.
