import os
import csv

election_csv = os.path.join('..','PyPoll','Resources','election_data.csv')

def election_results(election_data):
    candidate = str(election_data[2])
                   
    if candidate in cand_list:
        cand_list[candidate] += 1
    else :
        cand_list[candidate] = 1
    return cand_list

def per_votes():
    per_votes = (cand_list[candidate]/total_votes) * 100
    return per_votes


with open(election_csv, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)
    
    total_votes = 0
    cand_list = {}
    
    for row in csvreader:
        cand_list = election_results(row)
        total_votes += 1

    max_per = 0
    winner = ''
    cand_lines = ''

    for candidate in cand_list:
        cand_per = per_votes()
        if cand_per > max_per:
            max_per = cand_per
            winner = candidate
        cand_lines += '%s: %s%% (%s) \n'%(candidate, '{:.3f}'.format(cand_per), cand_list[candidate])
        
output = """
Election Results
-------------------------
Total Votes: %s
-------------------------
%s
-------------------------
Winner: %s
-------------------------
"""%(total_votes, cand_lines.strip('\n'), winner)

print(output)

results_txt = os.path.join('..','PyPoll','Analysis','election_results.txt')

with open(results_txt, 'w') as txtfile:
    txtwriter = txtfile.writelines(output)

