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

    print("Locations:", locations)
    print("Occurrences:", len(locations))


# Read the file and populate the grid
read_file(path)

# Search for the word "XMAS" in the grid
word_search(grid, "XMAS")