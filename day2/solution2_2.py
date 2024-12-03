import csv

safe_count = 0

with open("2024/day2/inputs2.csv", "r") as file:
    reader = csv.reader(file, delimiter = ' ')
    for row in reader:
        
        safe = True
        inc = True
        dec = True

        diff_violations = 0
        dir_violations = 0

        list = [int(value) for value in row]
        for x in range(len(list) - 1):

            diff = abs(list[x+1] - list[x])
            if (diff < 1) or (diff > 3):
                diff_violations += 1

            if list[x] <= list[x+1]:
                dir_violations += 1
                dec = False

            if list[x] >= list[x+1]:
                dir_violations += 1
                inc = False

        if ((not inc and not dec) and (dir_violations > 1 or diff_violations > 1)):
            safe = False
            
        if safe and (diff_violations <= 1 or inc or dec): 
            safe_count += 1 


print (safe_count)