import csv

safe_count = 0

with open("2024/day2/inputs2.csv", "r") as file:
    reader = csv.reader(file, delimiter = ' ')
    for row in reader:
        
        safe = True
        inc = True
        dec = True

        list = [int(value) for value in row]
        for x in range(len(list) - 1):

            diff = abs(list[x+1] - list[x])
            if (diff < 1) or (diff > 3):
                safe = False
                break
            if list[x] <= list[x+1]:
                dec = False

            if list[x] >= list[x+1]:
                inc = False
            
        if safe and (inc or dec): 
            safe_count += 1 
print (safe_count)