file = open('./input.txt')

lines = file.readlines()

# print(lines)

# siteExampleInpute = 'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53\r\nCard 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19\r\nCard 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1\r\nCard 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83\r\nCard 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36\r\nCard 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'

siteExampleInpute = 'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1'


idk = siteExampleInpute.split('\r\n')
answer = 0

for line in [line[10:].strip().split(' | ') for line in idk]:
# for line in [line[10:].strip().split(' | ') for line in lines]:

    lineScore = 0
    winningNumbers = line[0].split()
    # losingNumber = line[1].split()
    
    for wNum in winningNumbers:
        print('************')
        if(wNum == 1):
            print('winNum: ' + str(wNum))
            
        continue
        if(line[1].find(wNum) != -1):
            print(wNum)
            if(lineScore == 0):
                print('adding 1 to linescore')
                lineScore = lineScore + 1
            else:
                print('multiplying linescore by 2')
                lineScore = lineScore + lineScore

    answer = answer + lineScore

    # print(lineScore)

print('answer: ' + str(answer))



    # print(line)
    # print(winningNumbers)

# for line in lines:
#     line = line[10:]
#     print(line)