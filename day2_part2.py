file = open('./day2_input.txt')

lines = file.readlines()

gamesCanWork = []

answer = 0

for line in lines:
    splitLine = line.split(':')

    leftHalf = splitLine[0]
    rightHalf = splitLine[1]

    splitLeft = leftHalf.split()

    #Grab the game number
    gameNumber = splitLeft[1]

    bagGrabs = rightHalf.split(';')

    minRed = 0
    minGreen = 0
    minBlue = 0

    for grab in bagGrabs:
        dice = grab.split(',')
        print(dice)
        for die in dice:
            countSplit = die.split()
            print(countSplit)

            if(countSplit[1] == 'red'):
                numberOfDie = int(countSplit[0])
                if(numberOfDie > minRed):
                    # goodGame = False
                    minRed = numberOfDie
                    
            if(countSplit[1] == 'green'):
                numberOfDie = int(countSplit[0])
                if(numberOfDie > minGreen):
                    # goodGame = False
                    minGreen = numberOfDie
                    
            if(countSplit[1] == 'blue'):
                numberOfDie = int(countSplit[0])
                if(numberOfDie > minBlue):
                    # goodGame = False
                    minBlue = numberOfDie
    power = minRed * minGreen * minBlue

    answer = answer + power               

    

print(answer)