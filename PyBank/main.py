import os
import csv

PyBank_csv = os.path.join('..', 'PyBank', '03-Python_Instructions_PyBank_Resources_budget_data.csv')
f = open('bank.txt', 'w+')
with open(PyBank_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    input = 'PyBank_csv'
with open(PyBank_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    data = list(csvreader)
    row_count = (len(data)-1)
    print(f'Total months = {row_count} ')
    f.write(f'Total months = {row_count} \n')
Total_ProfitLosses=0
for i in (range(1, (row_count + 1))):
    
    Total_ProfitLosses = (Total_ProfitLosses + int(data[i][1]))

print(f'Total Profit/ Losses = ${Total_ProfitLosses}')
f.write(f'Total Profit/ Losses = ${Total_ProfitLosses}\n')
Differences = []
Previous_Value = int(data[1][1])

for i in range(2, len(data)):
    Current_Value = int(data[i][1])
    Differences.append(int(Current_Value)-int(Previous_Value))
    Previous_Value = Current_Value

Sum_Differences = sum(Differences)
Total_Differences = len(Differences)
Average_Change=round((int(Sum_Differences)/int(Total_Differences)),2)
print(f'Average Change: ${Average_Change}')
f.write(f'Average Change: ${Average_Change}\n')
pValue = 0
for value in Differences:
    if value > pValue:
        Greatest_Increase = value
    pValue = value
print(f'Greatest increase in profits = $({Greatest_Increase})')
f.write(f'Greatest increase in profits = $({Greatest_Increase})\n')
pValue = 0
for value in Differences:
    if value < pValue:
        Greatest_Decrease = value
    pValue = value
print(f'Greatest decrease in profits = $({Greatest_Decrease})')
f.write(f'Greatest decrease in profits = $({Greatest_Decrease})')
f.close()