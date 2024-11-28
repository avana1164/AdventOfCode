file = open('adventfile16_2022', 'r')
f = file.readlines()
valves = {}
nodes = []
nodes_of_interest = []

for line in f:
    line = line.strip().split(" ")
    connections = []
    for i in range(9, len(line)): 
        connections.append(line[i].replace(",", ""))
    
    rate = line[4].replace("rate=", "").replace(";", "")
    nodes.append(line[1])
    if int(rate) > 0:
        nodes_of_interest.append(line[1])
        
    valves[line[1]] = [int(rate), connections]


def floyd_warshall(valves, nodes):
    n = len(nodes)
    dist = [[float('inf')]*n for _ in range(n)]

    for u in nodes:
        for v in valves[u][1]:
            if v in nodes:
                dist[nodes.index(u)][nodes.index(v)] = 1
        dist[nodes.index(u)][nodes.index(u)] = 0
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                
    return dist

dist = floyd_warshall(valves, nodes)  

cache = {}
def max_pressure(current, time, visited):
    if (current, time, visited) in cache:
        return cache[(current, time, visited)]
        
    max_val = 0
    
    if time <= 0:
        return 0
    
    for next in nodes_of_interest:
        distance = dist[nodes.index(current)][nodes.index(next)] + 1
        if not (visited & (1 << nodes.index(next))) and time - distance >= 0:
            pressure = valves[next][0]*(time - distance)
            max_val = max(max_val, pressure + max_pressure(next, time - distance, visited | (1 << nodes.index(next))))
            cache[(current, time, visited)] = max_val
    
    return max_val

mask = (1 << len(nodes_of_interest)) - 1
max_val = 0

for i in range((mask + 1)//2):
    max_val = max(max_val, max_pressure("AA", 26, i) + max_pressure("AA", 26, i^mask))
    
print(max_val)