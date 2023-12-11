file = open('./input.txt')

lines = file.readlines()

total = 0

for i, line in enumerate(lines):

    l = line
    score = 0
    semi = l.find(':')

    semi = semi + 1
    l = l[semi:].strip().split(' | ')

    # print(l)

    winners = l[0].replace('  ', ' ').split(' ')
    nums = l[1].replace('  ', ' ').split(' ')

    # print(winners)
    # print(nums)
    # print(type(nums))

    for win in winners:
        if win in nums:
            if(score == 0):
                score = score + 1
            else:
                score = score * 2

    print('Line: ' + str(i) + ' --- Score: ' + str(score) )
    total = total + score

print('Total: ' + str(total))    

# for line in lines:
#     l = line

#     semi = l.find(':')

#     semi = semi + 1
#     l = l[semi:].strip().split(' | ')

#     winners = l[0].replace('  ', ' ').split(' ')
#     nums = l[1]

#     print(winners)
#     print(nums)

#     for win in winners:
#         find = nums.find(win)
#         print(find)

#     score = 0
#     1111        
#     for num in nums:
#         for wnum in win:
#             if(num == wnum):
#                 if(score == 0):
#                     score = score + 1
#                 else:
#                     score = score * 2

#     print('adding ' + str(score) + ' to total')
#     total = total + score
#     print('new Total: ' + str(total))

# print(total)
# print(len(lines))