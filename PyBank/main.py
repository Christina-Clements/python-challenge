import os
import csv

PyBank_csv = os.path.join('..', 'PyBank', '03-Python_Instructions_PyBank_Resources_budget_data.csv')


with open(PyBank_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    print(csvreader)

    csv_header = next(csvreader)
    print(f'CSV Header: {csv_header}')

    for row in csvreader:
        print(row)

    input = 'PyBank_csv'
with open(PyBank_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    data = list(csvreader)
    row_count = len(data)
    print(f'Total months = {row_count}. ')


        



    


    