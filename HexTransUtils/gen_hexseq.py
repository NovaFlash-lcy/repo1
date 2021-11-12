t = 0
i = 0
list = []
while i <= 33:
    list.append(''.join([hex(t)[2:].replace('c', 'C'), 'H']))
    i = i + 1
    t = t + 4
# print(list)
with open('res1.txt', 'w') as f:
    for i in list:
        f.write(''.join([' ', i]))
        f.write('\n')
