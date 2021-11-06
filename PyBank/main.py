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

     #profit_loss = []
    # for row in file:
        # profit_loss.append(int(row[1]))
        # Total_Profit = (profit_loss.append(int(row[1])))
       #  print(Total_Profit)


# with open(csvpath, 'r') as infile:
    # columns = list(map(float,next(infile).split(',')))
    # for how_many_entries, line in enumerate(infile,start=2):
        # for (idx,running_avg), new_data in zip(enumerate(columns), line.split(',')):
            # columns[idx] += (float(new_data) - running_avg)/how_many_entries

   
    # total_profit = 0
    # for row in open(csvpath):
       # total_profit.append(row[1])
        #total_profit = total_profit + int(row[1])

# def AverageColumn (c):
  #  f=open(csv,"r")
   # average=0
    #Sum=0
    # column=len(f)
   # for i in range(0,column):
        #for n in i.split(','):
           # n=float(n)
            #Sum += n
        #average = Sum / len(column)
    #return 'The average is:', average

# f.close()

# csv_file = csv. reader(open("your_file_name.csv"))
# dist = 0.
# for row in csv_file:
# _dist = row[2]
# try:
# _dist = float(_dist)        _   
   



