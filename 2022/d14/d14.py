file = open('d14', 'r')
f = file.readlines()
filled = {}
min_height = 0
curr = [500, 0]
sand_units = 0
def check_repeat(coor, filled):
    if tuple(coor) not in filled:
        filled[tuple(coor)] = 'R'
def check_height(height, min_height):
    if height > min_height:
        return height
    else:
        return min_height
        
for line in f:
    s = line.strip()
    s = s.replace(" ->", "")
    s = s.replace(',', " ")
    s = s.split()
    for i in range(0, len(s) - 3, 2):
        num1 = int(s[i])
        num2 = int(s[i + 1])
        num3 = int(s[i + 2])
        num4 = int(s[i + 3])
        if num4 != num2:
            if num4 > num2:
                for j in range(num2, num4 + 1):
                    check_repeat([num1, j], filled)
                    min_height = check_height(j, min_height)
            elif num4 < num2:
                for j in range(num2, num4 - 1, -1):
                    check_repeat([num1, j], filled)
                    min_height = check_height(j, min_height)
        elif num3 != num1:
            min_height = check_height(num2, min_height)
            if num3 > num1:
                for j in range(num1, num3 + 1):
                    check_repeat([j, num2], filled)
            elif num3 < num1:
                for j in range(num1, num3 - 1, -1):
                    check_repeat([j, num2], filled)
while (500, 0) not in filled.keys():  
    if (curr[0], curr[1] + 1) not in filled.keys() and curr[1] < min_height + 1:    
        move = True  
        curr[1]+=1
    elif (curr[0] - 1, curr[1] + 1) not in filled.keys() and curr[1] < min_height + 1:
        move = True
        curr[0]-=1
        curr[1]+=1
    elif (curr[0] + 1, curr[1] + 1) not in filled.keys() and curr[1] < min_height + 1:
        move = True
        curr[0]+=1
        curr[1]+=1
    else:
        filled[tuple(curr)] = 'S'
        sand_units+=1
        curr = [500, 0]   
print(sand_units)