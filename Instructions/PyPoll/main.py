# Dependencies
import pandas as pd
import numpy as np
import os


file = 'Resources\election_data.csv'

# Read our Data file with the pandas library
# Not every CSV requires an encoding, but be aware this can come up
df = pd.read_csv(file, encoding="ISO-8859-1")

# Preview of the DataFrame
#
# Note that FIELD8 is likely a meaningless column
df.head()

Total_votes=df['Voter ID'].count()
print("Election Results")
print("-------------------------")
print ("Total Votes:    :"  + str(Total_votes))
print("-------------------------")

#-------------------------------------------
#- Eliminate Candidates who did not recieve any vote
#---------------------------------------------
#df.groupby('Candidate').count()[['Voter ID']]
df = df.dropna(how='any')
#df [ 'Candidate'].head()

df_voteSum = df.groupby('Candidate').count()[['Voter ID']]
df_percent = df_voteSum.copy()
#df_percent = df_voteSum['VotePercent'] = [ x * 100 / Total_votes for x in df_voteSum['Voter ID']]
df_percent['VotePercent'] = [ x * 100 / Total_votes for x in df_percent['Voter ID']]
df_voteSum
df_wnr = df_voteSum[ df_voteSum['Voter ID']==df_voteSum['Voter ID'].max()]
print ("winner:")
df_wnr.iloc[:,0]

