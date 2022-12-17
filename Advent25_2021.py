file = open('adventfile25_2021', 'r')
f = file.readlines()
cu1 = {}
sum = 0
width = 139
height = 137
movement = True
y_coor = 0
for line in f:   
    s = line
    for i in range(width):           
        if s[i] == '>':
            cu1[(i, y_coor)] = '>'
        elif s[i] == 'v':            
            cu1[(i, y_coor)] = 'v'
    y_coor+=1

while movement:
    movement = False
    sum+=1
    cu2 = {}  
    for (x, y), c in cu1.items():
        if c == '>':
            nc = (x + 1) % width, y      
            if nc not in cu1:
                cu2[nc] = c 
                movement = True
            else:
                cu2[(x, y)] = c
        else:
            cu2[(x, y)] = c
    cu3 = {}  
    for (x, y), c in cu2.items():
        if c == 'v':
            nc = x, (y + 1) % height
            if nc not in cu2:
                cu3[nc] = c 
                movement = True
            else:
                cu3[(x, y)] = c
        else:
            cu3[(x, y)] = c 
    cu1 = cu3   
print(sum)