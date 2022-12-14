import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
#csvpath = os.path.join('..','Resources', 'budget_data.csv')

totalmonths = []
profits = []
pc = []

# Method 2 using CVS Module
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile) #, delimiter=',')
    print(csvreader)

    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    for row in csvreader:
        totalmonths.append(row[0])
        profits.append(int(row[1]))

for i in range(len(profits) - 1):
    pc.append(profits[i+1] - profits[i])


print(len(totalmonths))
print(sum(profits))
print(sum(pc) / len(pc))
print(totalmonths[pc.index(max(pc))+1])
print(totalmonths[pc.index(min(pc))+1])
print(min(pc))

#print(totalmonths.index("Jan-10"))




        