file = open('./input.txt')

lines = file.readlines()

answer = 0

numMap = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'zero': '0'}

def replaceWordsWithNums(inputString):
    keys = []

    for key in numMap:
        keys.append(key)

    for key in keys:
        start = 0
        while True:
            start = inputString.find(key, start)
            if(start == -1):
                break
            
            newValue = numMap[key]

            
            inputString[start] = numMap[key]
    
    return inputString
        


testing = 'onetwothreefour'

testing = replaceWordsWithNums(testing)

print('testing')
print(testing)


            



# for line in lines:
#     yeah = line.replace('\n', '')
#     replaceWordsWithNums(line)

#     break

#     index = 0
#     leftvalue = ''
#     rightvalue = ''

#     while(leftvalue == '' or rightvalue == ''):
#         if(leftvalue == '' and line[index].isdigit()):
#             leftvalue = line[index]
        
#         if(rightvalue == '' and line[(-1 * index) - 1].isdigit()):
#             rightvalue = line[(-1 * index) - 1]

#         index = index + 1

    
    
#     combinedValues = leftvalue + rightvalue

#     print(combinedValues)
#     numToAddToTotal = int(combinedValues)

#     answer = answer + numToAddToTotal

# print(answer)



#     # for char in yeah:
#     #     print(char)
