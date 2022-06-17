import os
import csv

budget_csv = os.path.join('..','Pybank','Resources','budget_data.csv')

date = []
profit = []
change = []

with open(budget_csv, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)
    previous = None
    max_profit = 0
    max_month = ""
    min_profit = 0
    min_month = ""
    for row in csvreader:
        date.append(row[0])
        profit.append(float(row[1]))
        if(previous != None):
            if ((float(row[1]) - previous) > max_profit):
                max_profit = int(float(row[1]) - previous)
                max_month = row[0]
            if ((float(row[1]) - previous) < min_profit):
                min_profit = int(float(row[1]) - previous)
                min_month = row[0]
            change.append(float(row[1]) - previous)
        previous = float(row[1])      
       
mth_count = len(date)

def total_net(profit):
    total = 0.0
    for row in profit:
        total += row
    return int(total)

def av_change(change):
    total = 0.0
    for row in change:
        total += row
    return '{:.2f}'.format(total/(mth_count - 1))

lines = """
Financial Analysis
----------------------------
Total Months: %s
Total: $%s
Average Change: $%s
Greatest Increase in Profits: %s ($%s)
Greatest Decrease in Profits: %s ($%s)
"""%(mth_count, total_net(profit), av_change(change), max_month, max_profit, min_month, min_profit)

print(lines)

results_txt = os.path.join('..','Pybank','Analysis','budget_results.txt')

with open(results_txt, 'w+') as txtfile:
    txtwriter = txtfile.writelines(lines)
    

        
