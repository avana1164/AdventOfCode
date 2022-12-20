file = open('adventfile15_2022', 'r')
f = file.readlines()
min_x = 0
max_x = 0
sensors = {}
pos = []
neg = []
pos_rep = set()
neg_rep = set()
for line in f:
    s = line.strip()
    s = s.replace("Sensor ", "")
    s = s.replace("at x=", "")
    s = s.replace(", y=", " ")
    s = s.replace(": closest beacon is", "")
    s = s.split()
    x1 = int(s[0])
    y1 = int(s[1])
    x2 = int(s[2])
    y2 = int(s[3])
    manhattan = abs(x1 - x2) + abs(y1 - y2)
    a = x1 + manhattan + 1
    b = x1 - (manhattan + 1)
    sum1 = y1 + a 
    sum2 = y1 - a
    sum3 = y1 + b
    sum4 = y1 - b
    if sum2 not in pos:
        pos.append(sum2)
    else:
        pos_rep.add(sum2)
    
    if sum4 not in pos:
        pos.append(sum4)
    else:
        pos_rep.add(sum4)

    if sum1 not in neg:
        neg.append(sum1)
    else:
        neg_rep.add(sum1)

    if sum3 not in neg:
        neg.append(sum3)
    else:
        neg_rep.add(sum3)
    sensors[(x1, y1)] = manhattan
    """row_num = 10
        if (y1 + manhattan >= row_num and y1 <= row_num) or (y1 - manhattan <= row_num and y1 >= row_num):
        row_range = abs(manhattan - abs(row_num - y1))
        if x1 - row_range < min_x:
            min_x = x1 - row_range
        elif x1 + row_range > max_x:
            max_x = x1 + row_range"""
beacon_length = 4000000
for i in neg_rep:
    for j in pos_rep:
        x = int((i - j)/2)
        y = x + j
        num_sensors = 22
        if x >= 0 and x <= beacon_length and y >= 0 and y <= beacon_length:
            for (x1, y1),k in sensors.items():
                manhattan = abs(x - x1) + abs(y - y1)
                if manhattan <= k:               
                    break
                else:
                    num_sensors-=1 
                if num_sensors == 0:
                    print(x*4000000+y)