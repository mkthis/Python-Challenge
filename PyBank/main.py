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

    change = []
    for i in range(len(Profits)-1):
        change.append(Profits[i +1]- Profits[i])

    print(f"Average Change: $ {round(sum(change)/len(change), 2)}")


    maximum = max(change)
    indexing = change.index(maximum)
    increasepr = Dates[indexing + 1]
    print(f'Greatest Increase in Change: {increasepr} (${maximum})')

    minimum = min(change)
    indexing2 = change.index(minimum)
    increasepr2 = Dates[indexing2 + 1]
    print(f'Greatest Decrease in Change: {increasepr} (${minimum})')

    output_path = os.path.join("Analysis", "Financial_Analysis.txt")
    f = open(output_path, "w")
    f.write("Financial Analysis")
    f.write("\n")
    f.write("-----------------------------------")
    f.write("\n")
    f.write((f"Total Months: {num_months}"))
    f.write("\n")
    f.write((f"Total Profits: ${sum(Profits)}"))
    f.write("\n")
    f.write((f"Average Change in Profits: ${round(sum(change)/len(change), 2)}"))
    f.write("\n")
    f.write((f"Greatest Increase in Profits: {increasepr}, (${maximum})"))
    f.write("\n")
    f.write((f"Greatest Decrease in Profits: {increasepr2}, (${minimum})"))
    f.write("\n")
    f.close

     