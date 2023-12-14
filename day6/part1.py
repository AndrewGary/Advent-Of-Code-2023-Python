races = [[40, 233], [82, 1011], [84, 1110], [92, 1487]]

# races = [[7, 9], [15, 40], [30, 200]]

total = 0
# race1 = races[2]
for race1 in races:
    numberOfWaysToWin = 0

    for i in range(race1[0]):
        print('distance: ', str((race1[0] - i) * i))
        distance = (race1[0] - i) * i

        if(distance > race1[1]):
            print('Winner!')
            numberOfWaysToWin = numberOfWaysToWin + 1
    if(total == 0):
        total = numberOfWaysToWin
    else:
        total = total * numberOfWaysToWin

print('total: ', str(total))
print('numberOfWaysToWin: ', str(numberOfWaysToWin))