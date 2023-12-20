

# convert instructions to a array of indexes to choose R = 1 and L = 0 so RL would be convereted to [1, 0]

# startString will always be the left value of the top row in the case above it would be 'AAA'

# con

file = open('./input.txt')

lines = file.readlines()

fileInstructions = lines[0].strip()

print(fileInstructions)


convertedInstructionSet = []
for char in fileInstructions:
    print(char)
    if(char == 'R'):
        convertedInstructionSet.append(1)
    if(char == 'L'):
        convertedInstructionSet.append(0)

linesplaceholder = []
for i, line in enumerate(lines):
    if(i > 1):
        linesplaceholder.append(line.strip().replace('(', '').replace(')', '').replace(' =', '').replace(',', ''))

structuredLines = {}
for i, line in enumerate(linesplaceholder):
    values = line.split(' ')
    structuredLines[values[0]] = [values[1], values[2]]

# print(structuredLines)

currentValue = 'AAA'
steps = 0

while(True):
    if(currentValue == 'ZZZ'):
        print('Answer: ', steps)
        break

    for value in convertedInstructionSet:
        currentValue = structuredLines[currentValue][value]
        steps += 1
        if(currentValue == 'ZZZ'):
            print(steps)
            break;


print(steps)
    
# # for line in lines:
# #     line = line.strip()
# #     print(line)