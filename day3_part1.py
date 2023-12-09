file = open('./day3_input.txt')

lines = file.readlines()

def check_character(char):
    if len(char) != 1:
        raise ValueError("Input must be a single character")

    return not char.isdigit() and char != '.'

symbolCords = []

# for i, line in enumerate(lines):
#     line = line.strip()
#     for ii, char in enumerate(line):
#         if(check_character(char)):
#             symbolCords.append([i, ii])

for i, line in enumerate(lines):
    line = line.strip()

    for ii, char in enumerate(line):
        foundDigit = False
        numberString = ''
        if(char.isdigit()):
            symbolCords.append([i, ii])

print(symbolCords)

nums = []

for syCord in symbolCords:
    row = syCord[0]
    column = syCord[1]

    
