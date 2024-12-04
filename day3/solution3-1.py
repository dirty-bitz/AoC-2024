import csv
import re

pattern = r"mul\((\d+),(\d+)\)"
matches = []
total = 0

with open("2024/day3/inputs3.csv", "r") as file:
    reader = csv.reader(file, delimiter=" ")
    for row in reader:
        print ("Row:", row)
        for cell in row:
            print ("Cell:", cell)
            cell_matches = re.findall(pattern, cell)
            matches.extend(cell_matches)

for x in matches:
    int1, int2 = map(int, x)
    total += int1 * int2

print("Total:", total)