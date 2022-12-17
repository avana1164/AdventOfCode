file = open('adventfile24_2018', 'r')
f = file.readlines()
infections = []
immune_system = []
line_num = 1
group_num = 1
for line in f:
    s = line.split()
    if line_num > 10:
        group_num = 1 
    if line_num > 10:   
        infections.append([int(s[0]), int(s[1]), s[2], s[3], s[4], int(s[5])])
        group_num+=1     
    else:       
        immune_system.append([int(s[0]), int(s[1]), s[2], s[3], s[4], int(s[5])])
        group_num+=1
    line_num+=1
       