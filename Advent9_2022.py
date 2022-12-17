file = open('adventfile9_2022', 'r')
f = file.readlines()
v = []
coor = {0: [0, 0], 1: [0, 0], 2: [0, 0], 3: [0, 0], 4: [0, 0], 5: [0, 0], 6: [0, 0], 7: [0, 0], 8: [0, 0], 9: [0, 0]}
for line in f:
    s = line.split()
    dir = s[0]
    moves = int(s[1])
    for _ in range(moves):                    
        if dir == 'R':              
            coor[0][0]+=1 
        elif dir == 'L':  
            coor[0][0]-=1           
        elif dir == 'U':          
            coor[0][1]+=1                      
        elif dir == 'D':  
            coor[0][1]-=1 

       
        for i in range(9):                     
            y = coor[i][1] - coor[i + 1][1]
            x = coor[i][0] - coor[i + 1][0]
            
            if abs(x) > 1 or abs(y) > 1:
                if abs(x) > 1 or abs(y) > 1:
                #     if x > 0 and y > 0:
                #         coor[i + 1][0] += 1
                #         coor[i + 1][1] += 1
                #     elif x < 0 and y > 0:
                #         coor[i + 1][0] -= 1
                #         coor[i + 1][1] += 1
                #     elif x > 0 and y < 0:
                #         coor[i + 1][0] += 1
                #         coor[i + 1][1] -= 1
                #     elif x < 0 and y < 0:
                #         coor[i + 1][0] -= 1
                #         coor[i + 1][1] -= 1
                #     elif x > 1:
                #         coor[i + 1][0] += 1
                #     elif x < -1:
                #         coor[i + 1][0] -= 1
                #     elif y > 1:
                #         coor[i + 1][1] += 1
                #     elif y < -1:
                #         coor[i + 1][1] -= 1
                if x > 1:
                    coor[i + 1] = [coor[i + 1][0] + 1, coor[i + 1][1] + y]                  
                elif x < -1:
                    coor[i + 1] = [coor[i + 1][0] - 1, coor[i + 1][1] + y] 
                elif y > 1:
                    coor[i + 1] = [coor[i + 1][0] + x, coor[i + 1][1] + 1]  
                elif y < -1:
                    coor[i + 1] = [coor[i + 1][0] + x, coor[i + 1][1] - 1]   
            print
            if coor[9] not in v:
                v.append(coor[9])                                  
print(len(v))      
