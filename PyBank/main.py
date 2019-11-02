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

Total_ProfitLosses=0
for i in (range(1, row_count)):
    
    Total_ProfitLosses = (Total_ProfitLosses + int(data[i][1]))

print(f'Total Profit/ Losses = ${Total_ProfitLosses}')

Average_Change = round((Total_ProfitLosses/row_count), 2)

print(f'Average Change = ${Average_Change}')



        



    


    