f = open('./input.txt')

lines = f.readlines()

grid = []

for line in lines:
    line = line.strip()
    inputArray = []

    for char in line:
        inputArray.append(char)

    grid.append(inputArray)

startIndex = []

for i, line in enumerate(grid):
    for ii, char in enumerate(line):
        if (char == 'S'):
            startIndex.append(i)
            startIndex.append(ii)

path = [startIndex]

while(True):
    currentCords = grid[len(grid) - 1]
    currentLine = grid[0]
    currentColumn = grid[1]
    currentValue = grid[currentLine][currentColumn]

    
    if(currentValue == 'S'):
        if(grid[currentLine - 1][currentColumn] == '|' or grid[currentLine - 1][currentColumn] == '7' or grid[currentLine - 1][currentColumn] == 'F'):
            path.append([currentLine - 1, currentColumn])
            continue
        if(grid[currentLine + 1][currentColumn] == '|' or grid[currentLine + 1][currentColumn] == 'L' or grid[currentLine + 1][currentColumn] == 'J'):
            path.append([currentLine + 1, currentColumn])
            continue
        if(grid[currentLine][currentColumn + 1] == '-' or grid[currentLine][currentColumn + 1] == '7' or grid[currentLine][currentColumn + 1] == 'J'):
            path.append([currentLine, currentColumn + 1])
            continue
        if(grid[currentLine][currentColumn - 1] == '-' or grid[currentLine][currentColumn - 1] == 'L' or grid[currentLine][currentColumn - 1] == 'F'):
            path.append([currentLine, currentColumn - 1])
            continue
    else:
        break
    option1 = None
    option2 = None

    if(currentValue == 'L'):
        option1 = grid[currentLine - 1][currentColumn]
        option2 = grid[currentLine][currentColumn + 1]

    # nextCord = findNextCord(path[len(path) - 1])


# line = startIndex[0]
# column = startIndex[1]

# if(grid[line - 1][column] == '|'):


# def findNextCord(cordArray):
#     line = cordArray[0]
#     column = cordArray[1]

#     if(grid[line - 1] == '|'):
#         return [line - 1, column]
