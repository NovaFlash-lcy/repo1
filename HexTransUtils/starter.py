import os

t_list = []

for line in open('test.txt'):
    # print(line)
    hex_list = line.split(' ', 4)
    hex_list[3] = hex_list[3][0:-1]
    # print(hex_list)
    num_list = []
    for item in hex_list:
        num_list.append(int(item, 16))
    # print(num_list)
    bin_list = []
    for item in num_list:
        t = bin(item)[2:]
        while len(t) < 8:
            t = ''.join(['0', t])
        t = ''.join([' ', t])
        bin_list.append(t)
    print(bin_list)
    t_list.append(bin_list)

with open('res.txt', 'w') as f:
    for line\
            in t_list:
        f.writelines(line)
        f.write('\n')
