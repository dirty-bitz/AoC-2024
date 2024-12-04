import csv
import re
import time

start_time = time.time()

pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
matches = []
total = 0
do = True

with open("2024/day3/inputs3.csv", "r") as file:
    reader = csv.reader(file, delimiter=" ")
    for row in reader:
        # print ("Row:", row)
        for cell in row:
            # print ("Cell:", cell)
            cell_matches = re.findall(pattern, cell)
            matches.extend(cell_matches)

for x in matches:
    if x == "don't()":
        do = False
    if x == "do()":
        do = True
    if do and x != "do()":
        x = x.strip("mul()").split(",")
        int1, int2 = map(int, x)
        total += int1 * int2

end_time = time.time()
print("Total:", total)
print(f"Time Elapsed: {(end_time - start_time) * 1000} ms")