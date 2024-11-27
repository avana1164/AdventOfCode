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
        
    options = []
    
    if time <= 0:
        return 0
    
    for next in nodes_of_interest:
        distance = dist[nodes.index(current)][nodes.index(next)] + 1
        if not (visited & (1 << nodes.index(next))) and time - distance >= 0:
            pressure = valves[next][0]*(time - distance)
            cache[(current, time, visited)] = pressure + max_pressure(next, time - distance, visited | (1 << nodes.index(next)))
            options.append(cache[(current, time, visited)])

    if not options:
        return 0
    
    return max(options) 
          
print(max_pressure("AA", 30, 0))