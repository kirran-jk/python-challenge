import os
import csv

# Path to collect the data file.
budget_csv = os.path.join('..','PyBank','Resources','budget_data.csv')

# Define empty lists to assign data to.
date = []
profit = []
change = []

# Read in CSV file, splitting the data on commas and storing the header row.
with open(budget_csv, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)

    # Define variables.
    previous = None
    max_profit = 0
    max_month = ""
    min_profit = 0
    min_month = ""
    # Method to loop through rows in the datafile, append columns to the lists previously defined.
    for row in csvreader:
        date.append(row[0])
        profit.append(float(row[1]))
        # Calculate maximum and minimum profit and the respective months where they occur. 
        if(previous != None):
            if ((float(row[1]) - previous) > max_profit):
                max_profit = int(float(row[1]) - previous)
                max_month = row[0]
            if ((float(row[1]) - previous) < min_profit):
                min_profit = int(float(row[1]) - previous)
                min_month = row[0]
            # Calculate the difference in profit between each row and stores in a list.
            change.append(float(row[1]) - previous)
        previous = float(row[1])      

# Count the total months in the data.   
mth_count = len(date)

# Method to sum up values in a given list.
def total_net(profit):
    total = 0.0
    for row in profit:
        total += row
    return int(total)

# Method to calculate average in a given list (formats to 2 d.p.).
def av_change(change):
    total = 0.0
    for row in change:
        total += row
    return '{:.2f}'.format(total/(mth_count - 1))

# Format output to print and write to Text file.
output = f"""Financial Analysis 
----------------------------
Total Months: {mth_count}
Total: ${total_net(profit)}
Average Change: ${av_change(change)}
Greatest Increase in Profits: {max_month} (${max_profit})
Greatest Decrease in Profits: {min_month} (${min_profit})
"""

print(output)

# Path to create text file and write output to file.
results_txt = os.path.join('..','PyBank','Analysis','budget_results.txt')

with open(results_txt, 'w') as txtfile:
    txtwriter = txtfile.writelines(output)
    

        
