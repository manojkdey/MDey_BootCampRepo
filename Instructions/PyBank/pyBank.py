# Import Dependencies
import pandas as pd
# File to Load
budget_d = "Resources/budget_data.csv"

# Read the modified GoodReads csv and store into Pandas DataFrame
bd_df = pd.read_csv(budget_d, encoding="utf-8")
bd_df.head(2)

#- FInd the total number of months in the df_df
totalMonths = bd_df["Date"].count()

#- FInd net total amount of "Profit/Losses" over the entire period
totalProfit = bd_df["Profit/Losses"].sum()

#- Calculate aaverage of changes over entire period
bd_df ["change"] = bd_df["Profit/Losses"].diff()
bd_df.head()

avgChange = bd_df["Profit/Losses"].mean()



#- Calculate greatest increase in profit over entire period
maxProfit = bd_df["change"].max()
maxProfitRow = bd_df[bd_df['change'] == maxProfit]
maxProfitDate = maxProfitRow['Date']
#maxProfitDate

#- Calculate greatest decrease loss over entire period
minProfit = bd_df["change"].min()
minProfitRow = bd_df[bd_df['change'] == minProfit]
minProfitDate = minProfitRow['Date']
#minProfit

#- PRint report
print('Financial Analysis')
print('----------------------------')
print('Total Months: ' + str(totalMonths))
print('Average  Change: ' + str(avgChange))
print('Greatest Increase in Profits: ' + maxProfitDate + " " + str(maxProfit))
print('Greatest Decrease in Losses: ' + minProfitDate + " " + str(minProfit))