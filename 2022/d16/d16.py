file = open('d16', 'r')
f = file.readlines()
paths = {}
valves = {}
visited = {}
dist = {}
nonzero = []

for line in f:
    line = line.strip().split(" ")
    connections = []
    for i in range(9, len(line)): 
        connections.append(line[i].replace(",", ""))
    
    rate = line[4].replace("rate=", "").replace(";", "")
    if int(rate) > 0:
        nonzero.append(line[1])
        valves[line[1]] = int(rate)
        dist[line[1]] = {}
        
    paths[line[1]] = connections
    visited[line[1]] = [0, False]

dist["AA"] = {}

for node in dist:
    visited = {k: [0, False] for k in visited}
    queue = []
    queue.append(node)
    visited[node][1] = True
    while len(queue) > 0:
        u = queue[0]
        for v in paths[u]:
            if not visited[v][1]:
                visited[v][1] = True
                visited[v][0] = visited[u][0] + 1
                queue.append(v)
                if v in dist and v != "AA":
                    dist[node][v] = visited[v][0]
        queue.pop(0)

indices = {}
for i in range(len(nonzero)):
    indices[nonzero[i]] = i
 
cache = {}

# Try to use dictionaries instead of arrays to make lookup times faster
def max_pressure(current, time, opened):
    if (current, time, opened) in cache:
        return cache[(current, time, opened)]
        
    max_val = 0

    for next in dist[current]:
        remtime = time - dist[current][next] - 1
        #adding continues instead of one if statement makes code slightly faster
        if remtime < 0:
            continue
        bit = 1 << indices[next]
        if opened & bit:
            continue
        pressure = valves[next]*(remtime)
        max_val = max(max_val, pressure + max_pressure(next, remtime, opened | bit))    
    
    cache[(current, time, opened)] = max_val
    
    return max_val 
    
# part 1 
# print(max_pressure("AA", 30, 0)) 

# part 2 (don't add AA to non zero, an extra bit means twice the number of iterations)
mask = (1 << len(nonzero)) - 1
max_val = 0

for i in range((mask + 1)//2):
    max_val = max(max_val, max_pressure("AA", 26, i) + max_pressure("AA", 26, i^mask))
    
print(max_val)