# In this challenge, you are tasked with creating a Python script to analyze the financial records of your company. 
# You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is 
# composed of two columns: "Date" and # "Profit/Losses". (Thankfully, your company has rather lax standards for 
# accounting, so the records are simple.)

# Your task is to create a Python script that analyzes the records to calculate each of the following:

# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in profits (date and amount) over the entire period

import os
import csv

from csv import DictReader

# Declare Variables
Months = []
Profit = []
ProfitChange = []

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csv_dict_reader = DictReader(csvfile)
    
    # Loop through CSV file
    for row in csv_dict_reader:
       Months.append(row['Date'])
       Profit.append(int(row['Profit/Losses']))

# Loop through Profit/Losses to deteremine change in profit
for i in range(len(Profit) - 1):
   ProfitChange.append(Profit[i+1] - Profit[i])
   
# Find Max Increase/Decrease Month Index.  Index will be +1 from ProfitChange
maxIncreaseMonthIndex = ProfitChange.index(max(ProfitChange)) + 1
maxDecreaseMonthIndex = ProfitChange.index(min(ProfitChange)) + 1

# Display Financial Analysis Summary Information
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(Months)}")
print(f"Total: ${sum(Profit)}")
print(f"Average Change: {round(sum(ProfitChange) / len(ProfitChange),2)}")
print(f"Greatest Increase in Profits: {Months[maxIncreaseMonthIndex]} (${max(ProfitChange)})")
print(f"Greatest Decrease in Profits: {Months[maxDecreaseMonthIndex]} (${min(ProfitChange)})")

# Output files
outputFile = os.path.join("Analysis","Financial_Analysis_Summary.txt")

with open(outputFile,"w") as file:
    
# Write methods to print to Financial_Analysis_Summary 
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(Months)}")
    file.write("\n")
    file.write(f"Total: ${sum(Profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(ProfitChange) / len(ProfitChange),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {Months[maxIncreaseMonthIndex]} (${max(ProfitChange)})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {Months[maxDecreaseMonthIndex]} (${min(ProfitChange)})")