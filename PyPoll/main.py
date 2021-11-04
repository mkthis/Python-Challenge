import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    num_rows = 0

    for row in open(csvpath):
        num_rows = num_rows + 1

    print("Total Votes:", num_rows - 1)    

    candidates = []


    i = ["Voter ID", "County", "Candidate"]
    for row in csvreader:
        candidates.append(row[2])

    print(list(set(candidates)))

count_ot = 0
for candidate in candidates:
        if candidate == "O'Tooley":
            count_ot = count_ot + 1

print(count_ot)

count_k = 0
for candidate in candidates:
        if candidate == "Khan":
            count_k = count_k + 1

print(count_k)

count_l = 0
for candidate in candidates:
        if candidate == "Li":
            count_l = count_l + 1

print(count_l)

count_c = 0
for candidate in candidates:
        if candidate == "Correy":
            count_c = count_c + 1

print(count_c)


Percent_K = round(((count_k / num_rows) * 100), 2)
print(Percent_K, "%")

Percent_C = round(((count_c / num_rows) * 100), 2)
print(Percent_C, "%")

Percent_L = round(((count_l / num_rows) * 100), 2)
print(Percent_L, "%")

Percent_OT = round(((count_ot / num_rows) * 100), 2)
print(Percent_OT, "%")

dictionary = {"Khan": 63, "Correy": 20, "Li": 14, "O'Tooley": 3}
max_key = max(dictionary, key = dictionary.get)
print(max_key)

print("-------------------------------------------------------------------------------------")

print("Election Results:")
print("-------------------------------------------------------------------------------------")
print("Total Votes:", num_rows - 1)
print("-------------------------------------------------------------------------------------")
print("Khan:", Percent_K, "%", "(",count_k,")")
print("Cooley:", Percent_C, "%", "(",count_c,")")
print("Li:", Percent_L, "%", "(",count_l,")")
print("O'Tooley:", Percent_OT, "%", "(",count_ot,")")
print("-------------------------------------------------------------------------------------")
print("Winner:", max_key)