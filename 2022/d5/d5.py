file = open('d5', 'r')
f = file.readlines()
cargo = [[], [], [], [], [], [], [], [], []]
init_pos = 1
counter = 1
for line in f:
    s = line   
    if counter < 9:
        s = s.split()
        for i in range(0, 9):
            if s[i] != "[1]":              
                cargo[i].append(s[i]) 
    elif counter >= 10:
        s = s.replace("move ", "")
        s = s.replace("from ", "")
        s = s.replace("to ", "")
        s = s.split()
        num = int(s[0]) 
        start = int(s[1])
        end = int(s[2])               
        for i in range(num - 1, -1, -1):            
            cargo[end - 1].insert(0, cargo[start - 1][i]) #to keep the same order, use i instead of 0
            cargo[start - 1].pop(i) #to keep the same order, use i instead of 0      
    counter+=1
file.close()
for i in range(9):
    print(cargo[i][0]) 