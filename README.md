# Sentiment-Mining-for-Product-Comparison
This analysis was performed to understand the wider public opinion for Alexa and Google Home and finally conclude the most preferred ones by Twitterati.  

## Twitter Sentiment Analysis: Alexa vs Google Home
Built Python MapReduce job on Hadoop cluster & performed sentiment analysis on tweets of voice-assistants.  
Used Knowledge-based approach & calculated a total sentiment score for each product to find which product has stronger positive presence.


## Methodology
A. Data Extraction:
1. Extracted tweets using the open source twitter API in RStudio
2. Utilized packages such as rtweet, ROAuth, stringr, tm
3. Programmed to code such that the tweets contained “alexa”, “vs” and “google”  
A dataset was thus obtained that contained tweets and relevant parameters like ID of the tweet, time, date, favorited, etc.

B. Data Preprocessing:
Cleaned the tweets by performing the following preprocessing steps:
1. Converted the tweets to ASCII to avoid reading strange characters
2. Removed graphic characters
3. Removed junk values and replacement words like fffd which appear because of encoding differences
4. Removed the retweet, punctuations, links, tabs, blank spaces at beginning, usernames
5. Took a subset of Tweet ID and text for further operations
6. Converted the dataset into txt file by tab delimited feature  
After all these steps, the cleaned dataset was obtained which contained approximately 7500 tweets for both ‘alexa’ and ‘google’. Further narrowed it down as needed and found the tweets which contained the term ‘vs’ also.

C. Sentiment Analysis:
1. Loaded this data into Hadoop Distributed File System so that MapReduce could be utilized for conducting sentiment analysis. Fed a dictionary of positive and negative words to our program so that a Knowledge based approach could be used for sentiment analysis.

2. Mapper Program - 
The words in each tweet is compared with the bag of positive and negative words. The count of the classified words help to determine the polarity (a count of 0 indicated neutral sentiment while a value greater or lesser indicated positive and negative sentiment, respectively.) For each user, a score is obtained for the two keywords from his tweets.

3. Reducer Program - 
Combined the score for our keywords ‘alexa’ and ‘google’ in the reducer.

4. Finally, calculated a total sentiment score for each product to conclude the overall sentiment and thus compared which product has a stronger positive presence among the masses.

## File Description
bigdata.R, mapper.py and reducer.py files contain the code for data preprocessing and mapreduce jobs.

negative-words.txt and positive-words.txt contain the bag of words.

steps-to-execute.txt outline the steps to execute the Python MapReduce program.




