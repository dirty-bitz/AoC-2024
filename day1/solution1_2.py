import csv

column1 = []
column2 = []
score = 0

with open("2024/day1/inputs1_1.csv", "r") as file:
    reader = csv.reader(file, delimiter = ' ')
    for row in reader:
        row = [value for value in row if value]
        column1.append(int(row[0]))
        column2.append(int(row[1]))

sorted1 = sorted(column1)
sorted2 = sorted(column2)

entry = len(column1)

for x in range(entry):
    count = sorted2.count(sorted1[x])
    score += sorted1[x] * count
    
print(score)