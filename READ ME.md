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
- ystockquote

#### Data Extraction
- Import Yahoo_Finance python package.
- Store the stock data in CSV.
- Dataframes were created for each dataset.

#### Data Transformation
- Normalized the data to plot "Bell-Curve" using numpy Random function.

#### Plotting
- Offline Plotting done.
- Plotly library used.
- Scatter Plot 
- Displot (Normal Distribution)

#### Output
- StockData at 'final\Analysis\ana_[1-3]\StockData.png'
- VolumeTraded at 'final\Analysis\ana_[1-3]\VolumeTraded.png'
- SharesBA File at 'final\extra\SharesBA.csv'
- SharesGD File at 'final\extra\SharesGD.csv'
- SharesLMT File at 'final\extra\SharesLMT.csv'
- SharesRTN File at 'final\extra\SharesRTN.csv'

#### Plot 1


#### Inference
The plot encapsulates the steep rise in the value of the mentioned organizations due to the utilization of weapons in the Afghanistan war inflating the demand vs supply ratio.

#### Plot 2


#### Inference
- As the first plot describes the rise in value of stocks, high volumes of shares are traded on the New York Stock Exchange. 
- The normal distribution of the mentioned companies shows a right skewed shift. 
- It indicates a trend of buying a stock at a cheaper price to sell later at a projected surge price due to the ongoing war. 

### Final Conclusion based on Analysis.
- A proof of concept is established over the problem statement. 
- After studying the plots over the timeline, a conclusion can be drawn marking a direct relation between the utlization of weapons in war zones and the simultaneous upswing in the stock value of the top four defense contractors of the United States of America.

## Analysis 2 
Continuing the theme of 'war-profiteering', the focus of study shifts to the interest generated in media during the Afghanistan war. Popular events provoke vivid reflections among the citizens ensuing staunch attraction from media. The latter pursues the events in detail and concentrates efforts to encapsulate and express the buzz thereby distributing information. The increase in the demand of information reflects in the stock value of the media outlet.

During the initial months of the war, in a world devoid of social media, newpapers and television were the main source of updates. The following analyses attempts to visualize the interest in media about the activities surrounding the Afghanistan war. It targets a major newspaper, the New York Times, and its stock value on the New York Stock Exchange.


### Steps Taken

#### Data Preparation
Packages Used -:
- Yahoo_Finance
- OS
- time
- CSV
- Pandas
- Json
- time
- Numpy
- Plotly
- ystockquote
- NYT Archive API


#### Data Extraction
- Import Yahoo_Finance python package to fetch NYT 2002 as well as current data.
- Extract NYT acticles using archive API.
- Dataframes were created for each dataset from stocks.

#### Data Transformation
- From Stocks dataframe, years were removed in order to plot the stocks(2002 and current) on same graph.
- Mean of the stocks were plotted.
- Count of Articles in each section was calculated for json files extracted.
- Result stored in CSV.

#### Plotting
- Offline Plotting done.
- Plotly library used.
- Bar Graph 
- Pie Chart percentage distribution

#### Output
- NYTstocks at 'final\Analysis\ana_[1-3]\NYTstocks.png'
- SectionArticleCount at 'final\Analysis\ana_[1-3]\SectionArticleCount.png'
- SharesNYTWarTime File at 'final\extra\SharesNYTWarTime.csv'
- SharesNYTNow File at 'final\extra\SharesNYTNow.csv'
- TT1 File at 'final\extra\TT1.csv'


#### Plot 1


#### Inference
- Since the event was broadcasted live over the globe, and is potentially marked as a new divide in the political environment, minute details were significantly covered by the media to relay as much information to the aghast citizen. 
- A huge surge in the stock value is clearly visible when we compare one of the most apalling events of all time to the recent timeline.


#### Plot 2


#### Inference
- Majority of articles focused on the stories revolving around 9/11 and the rising politcal tensions while all other information eschewed. 
- It is clearly visualized in the pie chart, majority of articles are centered around the topics including World, New York, Washington, Front Page and Opinion.

### Final Conclusion based on Analysis.
- The consequtive plots validate thes problem statement displaying relative congruence in a direct impact of interest generated in information surrounding the political environment in the aftermath of 9/11 demonstrated in the first plot and the rise in the stock value of New York Times, the major source of information, as compared to its current standing demonstrated in the second plot.

## Analysis 3 
The Aim of Analysis 1 is to find the impact of war like situations on the stock market of Arm Manufacturers proving US govt arms. Basis of this analysis is the information gathered from knowledge that General Dynamics was the primary provider of TOMAHAWK Missiles to US and UK Govt. Total of 109 Tomahawk missiles were used during Afghan War 2002 with total cost of $150 Million. Other Arms providers used in the Analysis are Raytheon, Lockheed Martins and Boeing.


### Steps Taken

#### Data Preparation
Packages Used -:
- Yahoo_Finance
- OS
- time
- CSV
- Pandas
- Json
- time
- Numpy
- Plotly
- ystockquote


#### Data Extraction
- Import Yahoo_Finance python package to fetch NYT 2002 as well as current data.
- Extract NYT acticles using archive API.
- Dataframes were created for each dataset from stocks.

#### Data Transformation
- Mean of the stocks were plotted.
- Count of Articles in each section was calculated for json files extracted.
- Result stored in CSV.

#### Plotting
- Offline Plotting done.
- Plotly library used.
- Bar Graph 
- Box Plot

#### Output
- WordTotalArticle at 'final\Analysis\ana_[1-3]\WordTotalArticle.png'
- NYT at 'final\Analysis\ana_[1-3]\NYT.png'
- TT2 File at 'final\extra\TT2.csv'


#### Plot 1


#### Inference
The plot encapsulates the steep rise in the value of the mentioned organizations due to the utilization of weapons in the Afghanistan war inflating the demand vs supply ratio.

#### Plot 2


#### Inference
- As the first plot describes the rise in value of stocks, high volumes of shares are traded on the New York Stock Exchange. 
- The normal distribution of the mentioned companies shows a right skewed shift. 
- It indicates a trend of buying a stock at a cheaper price to sell later at a projected surge price due to the ongoing war. 

### Final Conclusion based on Analysis.
- A proof of concept is established over the problem statement. 
- After studying the plots over the timeline, a conclusion can be drawn marking a direct relation between the utlization of weapons in war zones and the simultaneous upswing in the stock value of the top four defense contractors of the United States of America.
