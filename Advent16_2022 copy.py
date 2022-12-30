import copy
from queue import Queue
queue = Queue()
queue2 = Queue()
file = open('adventfile16_2022', 'r')
f = file.readlines()
valves = {}
flow = {}
compressed = {}
def bfs(curr_node, valves):   
    v = copy.deepcopy(valves)   
    v[curr_node][0]=0
    queue.put(curr_node)   
    while not queue.empty():
        u = queue.get()
        for i in v[u][1]:
            if v[i][0] == -1: 
                v[i][0] = v[u][0] + 1 
                queue.put(i)
    return v
for line in f:
    s = line.strip()
    s = s.replace("Valve ", "").replace(" has flow rate=", " ").replace("; tunnels lead to valves", "").replace("; tunnel leads to valve", "").replace(',', "").split()
    valves[s[0]] = [-1, []]
    if int(s[1]) > 0:
        flow[s[0]] = int(s[1])
    for i in range(2, len(s)):
        valves[s[0]][1].append(s[i])
for i in flow:
    v = bfs(i, valves)
    compressed[i] = [[],[]]
    for j in flow:
        if j != i:
            compressed[i][0].append(j)
            compressed[i][1].append(v[j][0]+1)
v = bfs('AA', valves)
compressed['AA'] = [[],[]]
for j in flow:
    compressed['AA'][0].append(j)
    compressed['AA'][1].append(v[j][0]+1)
max_pressure = 0
queue.put(['AA', 0, 0, 30, flow]) #don't include both player and elephant, keep them separate
num_players = 2

print(max_pressure)