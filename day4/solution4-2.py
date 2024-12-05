import csv

path = "2024/day4/inputs4.csv"
grid = []

def read_file(file_in):
    global grid
    with open(file_in, "r") as file:
        reader = csv.reader(file, delimiter="\n")
        for row in reader:
            for char in row:
                grid.append(list(char))


def valid(x, y, rows, columns):
    # Make sure we don't go out of bounds
    return 0 <= x < rows and 0 <= y < columns

def checkDirection(grid, rows, columns, key, index, x, y, dirx, diry):
    if index == len(key):
        return True

    # Recursively check next letter in direction from call until it fails or finds a match
    if valid(x, y, rows, columns) and key[index] == grid[x][y]:
        return checkDirection(grid, rows, columns, key, index + 1, x + dirx, y + diry, dirx, diry)

    return False


def word_search(grid, key):
    locations = []
    rows = len(grid)

    if rows == 0:
        print("Grid is empty.")
        return

    columns = len(grid[0])

    # 8 possible directions
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    for x in range(rows):
        for y in range(columns):
            #check every letter to see if it matches first character in key
            if grid[x][y] == key[0]:
                # check down every cardinal direction to see if it spells out the key word
                for dirx, diry in directions:
                    if checkDirection(grid, rows, columns, key, 0, x, y, dirx, diry):
                        locations.append((x, y))

    # print("Locations:", locations)
    print("Occurrences:", len(locations))

def check_xmas_pattern(grid, rows, columns, x, y):

    # M . S
    # . A .
    # M . S

    if valid(x-1, y-1, rows, columns) and valid(x+1, y+1, rows, columns) and valid(x+1, y-1, rows, columns) and valid(x-1, y+1, rows, columns):
        # Check top-left to bottom-right)
        if grid[x-1][y-1] == 'M' and grid[x][y] == 'A' and grid[x+1][y+1] == 'M':
            if grid[x-1][y+1] == 'S' and grid[x+1][y-1] == 'S':
                return True
        
        # backwards
        if grid[x+1][y-1] == 'M' and grid[x][y] == 'A' and grid[x-1][y+1] == 'M':
            if grid[x+1][y+1] == 'S' and grid[x-1][y-1] == 'S':
                return True

    return False

def count_crosses(grid):
    count = 0
    xmas_locations = []
    rows = len(grid)
    if rows == 0:
        print("We aint got no grid")
        return
    
    columns = len(grid[0])

    for x in range(rows):
        for y in range(columns):
            if grid[x][y] == 'A':
                if check_xmas_pattern(grid, rows, columns, x, y):
                    xmas_locations.append((x, y))
                    count += 1
    print("xmas locations: ", xmas_locations)
    print(f"{count} occurences of xmas")
    
"""
# This is from when I was trying to get it to work for any key
# It kind of works but doesn't catch every occurence of the pattern]\
# If you know how to do sometihng like this pls let me know
def check_crosses(grid, key):
    count = 0
    rows = len(grid)
    columns = len(grid[0])

    if len(key) % 2 == 0:
        print("Gotta be odd to form an X")
        return

    center = len(key) // 2

    for x in range(rows):
        for y in range(columns):
            if grid[x][y] == key[center]:
                positions = [((x - i, y - i), key[center - i]) for i in range(1, center + 1)]\
                          + [((x - i, y + i), key[center - i]) for i in range(1, center + 1)]\
                          + [((x + i, y - i), key[center + i]) for i in range(1, center + 1)]\
                          + [((x + i, y + i), key[center + i]) for i in range(1, center + 1)]
                
                if all(valid(px, py, rows, columns) and grid[px][py] == letter for (px, py), letter in positions):
                    count += 1

    print("Crosses: ", count)
    return
"""

# Read the file and populate the grid
read_file(path)

# Search for the word "XMAS" in the grid
word_search(grid, "XMAS")
count_crosses(grid)