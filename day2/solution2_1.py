import csv

def is_safe(list):
    inc = True
    dec = True

    for x in range(len(list) - 1):

        diff = abs(list[x + 1] - list[x])

        if (diff < 1) or (diff > 3):
            return False
        
        if list[x] <= list[x+1]:
                dec = False

        elif list[x] >= list[x+1]:
            inc = False
            
    return inc or dec

def removal(list):
    for x in range(len(list)):
        new_list = list[:x] + list[x + 1:]

        if is_safe(new_list):
            return True
          
    return False

safe_count = 0

with open("2024/day2/inputs2.csv", "r") as file:
    reader = csv.reader(file, delimiter = ' ')
    for row in reader:
        list = [int(value) for value in row]
        if is_safe(list):
            safe_count += 1
        else:
            if removal(list):
                safe_count += 1


print (safe_count)