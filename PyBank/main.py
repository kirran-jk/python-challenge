import os
import csv

budget_csv = os.path.join('..','Pybank','Resources','budget_data.csv')

date = []
profit = []

with open(budget_csv, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)
    for row in csvreader:
        date.append(row[0])
        profit.append(float(row[1]))
        
mth_count = len(date)

def total_net(profit):
    total = 0.0
    for row in profit:
        total += row
    return total

changes = (profit[mth_count-1] - profit[0]) / mth_count

largest = max(profit)

smallest = min(profit)        

print (mth_count)
print (total_net(profit))
print (changes)
print(largest)
print(smallest)


        
