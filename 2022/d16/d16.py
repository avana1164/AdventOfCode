file = open('d16', 'r')
f = file.readlines()
paths = {}
valves = {}
visited = {}
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
        
    paths[line[1]] = connections
    visited[line[1]] = [0, False]

nonzero.insert(0, "AA")

dist = [[float('inf')]* len(nonzero) for _ in range(len(nonzero))]
for node in nonzero:
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
                if v in nonzero:
                    dist[nonzero.index(node)][nonzero.index(v)] = visited[v][0]
        queue.pop(0)
        
cache = {}
    
def max_pressure(current, time, opened):
    if (current, time, opened) in cache:
        return cache[(current, time, opened)]
        
    max_val = 0

    for next in nonzero:
        remtime = time - dist[nonzero.index(current)][nonzero.index(next)] - 1
        bit = 1 << nonzero.index(next)
        if not (opened & bit) and remtime >= 0 and next != "AA":
            pressure = valves[next]*(remtime)
            max_val = max(max_val, pressure + max_pressure(next, remtime, opened | bit))    
    
    cache[(current, time, opened)] = max_val
    
    return max_val 
    
# part 1 
# print(max_pressure("AA", 30, 0)) 

mask = (1 << len(nonzero)) - 1
max_val = 0

for i in range((mask + 1)//2):
    max_val = max(max_val, max_pressure("AA", 26, i) + max_pressure("AA", 26, i^mask))
    
print(max_val)