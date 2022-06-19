import os
import csv

# Path to collect the data file.
election_csv = os.path.join('..','PyPoll','Resources','election_data.csv')

# Method to populate dict keyed on candidate name and value vote count. 
def election_results(election_data):
    candidate = election_data[2]
                   
    if candidate in cand_dict:
        cand_dict[candidate] += 1
    else :
        cand_dict[candidate] = 1
    return cand_dict

# Method to calculate the proportion of votes per candidate.
def per_votes():
    per_votes = (cand_dict[candidate]/total_votes) * 100
    return per_votes

# Read in CSV file, splitting the data on commas and storing the header row.
with open(election_csv, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)

    # Define variables.
    total_votes = 0
    cand_dict = {}

    # Method to loop through rows in datafile, call method election_results() and calculate total votes.
    for row in csvreader:
        cand_dict = election_results(row)
        total_votes += 1
        
    # Define variables.
    max_per = 0
    winner = ''
    cand_lines = ''

    # For each candidate in dict, call method per_votes(). Calculate candidate with the maximum % of votes.
    for candidate in cand_dict:
        cand_per = per_votes()
        if cand_per > max_per:
            max_per = cand_per
            winner = candidate
        cand_lines += f'{candidate}: {cand_per:.3f}% ({cand_dict[candidate]})\n'

# Format output to print and write to Text file.     
output = f"""Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
{cand_lines}\
-------------------------
Winner: {winner}
-------------------------
"""

print(output)

# Path to create text file and write output to file.
results_txt = os.path.join('..','PyPoll','Analysis','election_results.txt')

with open(results_txt, 'w') as txtfile:
    txtwriter = txtfile.writelines(output)

