import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader: 
        print(row)

    file = open(csvpath)   
    csvreader = csvreader

    num_months = 0

    for row in open(csvpath):
        num_months = num_months + 1

    print("Total Months:", num_months - 1) 

    profit = []
    total_profit = 0
    profit.append(row[1])
    total_profit = total_profit + int(row[1])


_   
   



