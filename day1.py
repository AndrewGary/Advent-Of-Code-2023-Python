file = open('./input.txt')

lines = file.readlines()

answer = 0

for line in lines:
    yeah = line.replace('\n', '')

    index = 0
    leftvalue = ''
    rightvalue = ''

    while(leftvalue == '' or rightvalue == ''):
        if(leftvalue == '' and line[index].isdigit()):
            leftvalue = line[index]
        
        if(rightvalue == '' and line[(-1 * index) - 1].isdigit()):
            rightvalue = line[(-1 * index) - 1]

        index = index + 1

    
    
    combinedValues = leftvalue + rightvalue

    print(combinedValues)
    numToAddToTotal = int(combinedValues)

    answer = answer + numToAddToTotal

print(answer)



    # for char in yeah:
    #     print(char)
