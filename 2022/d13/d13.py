import json
file = open('d13', 'r')
f = file.readlines()
line_num = 0
pair_num = 1
sum = 0
s1 = ""
s2 = ""
for line in f:
    s = line.strip()
    line_num+=1
    if line_num == 1:
        s1 = json.loads(s)
        print(s1)
    elif line_num == 2:
        s2 = json.loads(s)
        print(s2)  
    else:
        line_num = 0 