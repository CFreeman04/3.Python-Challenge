#import modules
import os
import csv

#set path for file
csvpath = os.path.join('Resources', 'budget-data.csv')

#set the output of the text file
text_path = os.path.join("Analysis", "Final_Analysis.txt")

#Set variables
totalmonths = []
profits = []
pc = []

# Method 2 using CVS Module
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile) #, delimiter=',')
    #print(csvreader)

    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    for row in csvreader:
        totalmonths.append(row[0])
        profits.append(int(row[1]))

for i in range(len(profits) - 1):
        pc.append(profits[i+1] - profits[i])


print("Financial Analysis")
print("---------------------")
print(f"Total Months: {len(totalmonths)}")
print(f"Total Profit: {sum(profits)}")
print(f"Average Revenue Change: ${sum(pc) / len(pc):.2f}")
print(f"Greatest Increase in Profits: {totalmonths[pc.index(max(pc))+1]} (${max(pc)})")
print(f"Greatest Decrease in Profits: {totalmonths[pc.index(min(pc))+1]} (${min(pc)})")
  
#print(totalmonths.index("Jan-10"))
#write changes to csv
with open(text_path, 'w') as file:
        file.write("Financial Analysis\n")
        file.write("---------------------\n")
        file.write(f"Total Months:  {len(totalmonths)}\n")
        file.write(f"Total Profits: $ {sum(profits)}\n")
        file.write(f"Average Revenue Change ${sum(pc) / len(pc):.2f}\n")
        file.write(f"Greatest Increase in Profits: {(totalmonths[pc.index(max(pc))+1])} (${max(pc)})\n")
        file.write(f"Greatest Decrease in Profits: {(totalmonths[pc.index(min(pc))+1])} (${min(pc)})\n")
