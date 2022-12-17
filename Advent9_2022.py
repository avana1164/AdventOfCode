file = open('adventfile9_2022', 'r')
f = file.readlines()
v = []
coor = {0: [0, 0], 1: [0, 0], 2: [0, 0], 3: [0, 0], 4: [0, 0], 5: [0, 0], 6: [0, 0], 7: [0, 0], 8: [0, 0], 9: [0, 0]}
dir = {'R': [1, 0], 'L': [-1, 0], 'U': [0, 1], 'D': [0, -1]}
for line in f:
    s = line.split()
    m = s[0]
    moves = int(s[1])
    for _ in range(moves):                    
        coor[0][0]+=dir[m][0]
        coor[0][1]+=dir[m][1]
        for i in range(9):                     
            y = coor[i][1] - coor[i + 1][1]
            x = coor[i][0] - coor[i + 1][0]
            if abs(x) > 1 or abs(y) > 1:
                if x > 0 and y > 0:
                    coor[i + 1][0] += 1
                    coor[i + 1][1] += 1
                elif x < 0 and y > 0:
                    coor[i + 1][0] -= 1
                    coor[i + 1][1] += 1
                elif x > 0 and y < 0:
                    coor[i + 1][0] += 1
                    coor[i + 1][1] -= 1
                elif x < 0 and y < 0:
                    coor[i + 1][0] -= 1
                    coor[i + 1][1] -= 1
                elif x > 0:
                    coor[i + 1][0] += 1
                elif x < 0:
                    coor[i + 1][0] -= 1
                elif y > 0:
                    coor[i + 1][1] += 1
                elif y < 0:
                    coor[i + 1][1] -= 1

            if tuple(coor[9]) not in v:
                v.append(tuple(coor[9]))                                  
print(len(v))      