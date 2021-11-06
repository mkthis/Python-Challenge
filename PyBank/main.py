import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    num_months = 0
    Dates = []
    Profits = []
    for row in csvreader: 
        num_months = num_months + 1
        Profits.append(int(row[1]))
        Dates.append(row[0])

    print("Financial Analysis:")
    print("-----------------------------------------------------")
    print("Total Months:", num_months)

    Total = sum(Profits)

    print(f'Total: ${Total}')
    
    change = round((Profits[-1] - Profits[0])/len(Profits), 2)
    print(f"Average Change: ${change}")

    maximum = max(Profits)
    indexing = Profits.index(maximum)
    increasepr = Dates[indexing]
    print(f'Greatest Increase in Profits: {increasepr} (${maximum})')

    minimum = min(Profits)
    indexing = Profits.index(minimum)
    increasepr = Dates[indexing]
    print(f'Greatest Decrease in Profits: {increasepr} (${minimum})')

     