import os
import csv

PyPoll_csv = os.path.join('..', 'PyPoll', '03-Python_Instructions_PyPoll_Resources_election_data.csv')

with open(PyPoll_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    data = list(csvreader)
    input = 'PyPoll_csv'
    row_count = (len(data)-1)
print(f'Election Results')
print(f'----------------')    
print(f'Total Votes = {row_count} ')

with open(PyPoll_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    candidate_name= []
    for row in csvreader:
        candidate_name.append(row[2])
    used = []
    for candidate in candidate_name:
        if candidate in used:
            pass
        else:
            used.append(candidate)
    candidate_name= used
    print(f'----------------')
    votes = {}
    for candidate in candidate_name:
        Total_Votes=0
        for row in data:
            if row[2] == candidate:
                Total_Votes += 1
        votes[candidate] = Total_Votes
        print(f'{candidate} : {round((Total_Votes/row_count)*100, 3)}%  ({Total_Votes})')
    print(f'----------------')
    pValue = 0
    for election, value in votes.items():
        if value > pValue:
            winner = election
        pValue = value
    print(f'Winner: {winner}')
    print(f'----------------')






    

