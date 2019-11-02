import os
import csv
import math

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
    row_count = (len(data)-1)
    print(f'Total months = {row_count}. ')

Total_ProfitLosses=0
for i in (range(1, (row_count + 1))):
    
    Total_ProfitLosses = (Total_ProfitLosses + int(data[i][1]))

print(f'Total Profit/ Losses = ${Total_ProfitLosses}')

Differences = []
Previous_Value = int(data[1][1])

for i in range(2, len(data)):
    Current_Value = int(data[i][1])
    Differences.append(abs(int(Current_Value)-int(Previous_Value)))
    Previous_Value = Current_Value

Sum_Differences = sum(Differences)
Total_Differences = len(Differences)
Average_Change=round((int(Sum_Differences)/int(Total_Differences)),2)
print(f'Average Change: ${Average_Change}')



    


    