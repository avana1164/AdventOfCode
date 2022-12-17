import math
file = open('adventfile11_2022', 'r')
f = file.readlines()
monkeys = []
for line in f:    
    if "Starting" in line:
        line_type = 1
        monkey = []
        start_items = []
    s = line.split()
    if line_type == 1:
        for i in range(len(s)):
            if i >= 2:
                start_items.append(int(s[i]))
        monkey.append(start_items)
    elif line_type == 2:
        monkey.append(s[len(s) - 1])
        monkey.append(s[len(s) - 2])
        monkey.append(s[len(s) - 3])
    elif line_type == 3 or line_type == 4 or line_type == 5:
        monkey.append(int(s[len(s) - 1]))        
    if line_type == 5:
        monkey.append(0)
        monkeys.append(monkey)
    line_type+=1
for k in range(20):
    for i in range(len(monkeys)):
        monkeys[i][7]+=len(monkeys[i][0])
        for j in monkeys[i][0]:
            if monkeys[i][1] == 'old':
                num1 = j
            else:
                num1 = int(monkeys[i][1])
            
            if monkeys[i][3] == 'old':
                num2 = j
            else:
                num2 = int(monkeys[i][3])

            if monkeys[i][2] == '+':
                total_num = int(num1 + num2)
            elif monkeys[i][2] == '*':
                total_num = int(num1*num2)
            #total_num = math.floor(total_num/3)
            if total_num % monkeys[i][4] == 0:
                monkeys[monkeys[i][5]][0].append(total_num)  
            else:
                monkeys[monkeys[i][6]][0].append(total_num) 
        monkeys[i][0] = []
print(monkeys)
inspection = []
for i in range(len(monkeys)):
    inspection.append(monkeys[i][7])
inspection.sort()
print(inspection[len(inspection) - 1]*inspection[len(inspection) - 2])