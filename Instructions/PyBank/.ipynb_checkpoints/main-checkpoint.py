{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [],
   "source": [
    "#-main script to run for Pypoll analysis\n",
    "# Modules\n",
    "import os\n",
    "import pandas as pd\n",
    "import csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 137,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Store filepath in a variable\n",
    "PyBankPath = \"../02-Homework/03-Python/Instructions/PyBank/Resources/Budget_data.csv\"\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 138,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Read our Data file with the pandas library\n",
    "# Not every CSV requires an encoding, but be aware this can come up\n",
    "PyBankPath_df = pd.read_csv(PyBankPath, encoding=\"ISO-8859-1\")\n",
    "df = PyBankPath_df.copy()\n",
    "df['change'] = df['Profit/Losses'].diff()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 139,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total_Month    :86\n"
     ]
    }
   ],
   "source": [
    "#- The total number of months included in the dataset\n",
    "Total_months=df['Date'].count()\n",
    "print (\"Total_Month    :\"  + str(Total_months))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 140,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total          : $38382578\n"
     ]
    }
   ],
   "source": [
    "#- The net total amount of \"Profit/Losses\" over the entire period\n",
    "Total = df['Profit/Losses'].sum()\n",
    "#print (\"Total       : \"  + str(Total))\n",
    "print (\"Total          : \"  + '${:.0f}'.format(Total))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 141,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Average  Change: $-2315.12\n"
     ]
    }
   ],
   "source": [
    "#- The average of the changes in \"Profit/Losses\" over the entire period\n",
    "avgChange = df['change'].mean()\n",
    "avgChange = (\"%.2f\" % avgChange)\n",
    "print (\"Average  Change: \" + '${:.2f}'.format(float(avgChange)))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 142,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "25    Greatest Increase in Profits: Feb-2012 ($19261...\n",
      "Name: Date, dtype: object\n"
     ]
    }
   ],
   "source": [
    "#-  The greatest increase in profits (date and amount) over the entire period\n",
    "mxChange = df['change'].max()\n",
    "mxChangeRow = df.loc[df['change'] == maxChange]\n",
    "maxChangeDate = mxChangeRow [ 'Date' ]\n",
    "maxChangeAmt = mxChangeRow [ 'change' ]\n",
    "print (\"Greatest Increase in Profits: \" + maxChangeDate + \" (\" + '${:.2f}'.format(float(maxChangeAmt)) + \")\" )\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
