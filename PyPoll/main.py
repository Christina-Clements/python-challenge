import os
import csv

PyPoll_csv = os.path.join('..', 'PyPoll', '03-Python_Instructions_PyPoll_Resources_election_data.csv')

with open(PyPoll_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f'CSV Header: {csv_header}')
    data = list(csvreader)
    input = 'PyPoll_csv'
    row_count = (len(data)-1)
print(f'Election Results')
print(f'----------------')    
print(f'Total Votes = {row_count} ')


    

