from queue import Queue
queue = Queue()
file = open('adventfile25_2018', 'r')
f = file.readlines()
coordinates = {}
sum = 0
for line in f:
    s = line
    s = s.replace(',', " ")
    s = s.split()
    connectable = []
    if len(coordinates) >= 1:
        for (w, x, y, z), i in coordinates.items():
            w2 = int(s[0])
            x2 = int(s[1])
            y2 = int(s[2])
            z2 = int(s[3])
            if abs(w - w2) + abs(x - x2) + abs(y - y2) + abs(z - z2) <= 3:
                i.append((w2, x2, y2, z2))  
                connectable.append((w, x, y, z))             
    coordinates[(int(s[0]), int(s[1]), int(s[2]), int(s[3]))] = connectable
while len(coordinates) > 0:
    for k in coordinates.keys():
        queue.put(k)
        break
    
    while not queue.empty():
        u = queue.get()
        if u in coordinates.keys():
            for v in coordinates[u]:                           
                queue.put(v)                   
            try:
                del coordinates[u]
            except KeyError:
                pass
    sum+=1
print(sum)         