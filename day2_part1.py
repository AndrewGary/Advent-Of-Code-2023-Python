file = open('./day2_input.txt')

lines = file.readlines()

gamesCanWork = []

for line in lines:
    splitLine = line.split(':')

    leftHalf = splitLine[0]
    rightHalf = splitLine[1]

    splitLeft = leftHalf.split()

    #Grab the game number
    gameNumber = splitLeft[1]

    bagGrabs = rightHalf.split(';')

    goodGame = True

    for grab in bagGrabs:
        dice = grab.split(',')
        print(dice)
        for die in dice:
            countSplit = die.split()
            print(countSplit)

            if(countSplit[1] == 'red'):
                numberOfDie = int(countSplit[0])
                if(numberOfDie > 12):
                    goodGame = False
                    continue
            if(countSplit[1] == 'green'):
                numberOfDie = int(countSplit[0])
                if(numberOfDie > 13):
                    goodGame = False
                    continue
            if(countSplit[1] == 'blue'):
                numberOfDie = int(countSplit[0])
                if(numberOfDie > 14):
                    goodGame = False
                    continue

    if(goodGame == True):
        gamesCanWork.append(gameNumber)

total = 0

for value in gamesCanWork:
    digit = int(value)

    total = total + digit

print(total)