file = open('adventfile13_2022', 'r')
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
        s1 = s[1:len(s) - 1]
        print(s1)
    elif line_num == 2:
        s2 = s[1:len(s) - 1]
        print(s2)
    elif s == "":
        line_num = 0
        bracket_num = 0
        for i in s1:
            if i == '[':
                line_num
            

        #for i in range(len())           
       