from queue import Queue
queue = Queue()
file = open('adventfile16_2022', 'r')
f = file.readlines()
def pathways(start, end, valves):
    queue.put(start)
    while not queue.empty():

valves = {}
minutes = 30
tot_pres = 0
flow_rate = 0
highest_valves = {}
lowest_valves = {}
for line in f:
    s = line.strip()
    s = s.replace("Valve ", "")
    s = s.replace(" has flow rate=", " ")
    s = s.replace("; tunnels lead to valves", "")
    s = s.replace("; tunnel leads to valve", "")
    s = s.replace(',', "")
    s = s.split()
    valves[s[0]] = [int(s[1]), False, []]
    if int(s[1]) >= 10:
        highest_valves[s[0]] = int(s[1])
    elif int(s[1]) > 0 and int(s[1]) < 10:
        lowest_valves[s[0]] = int(s[0])
    for i in range(2, len(s)):
        valves[s[0]][2].append(s[i])
distance = 0
while minutes > 0:       
    curr_valve = queue.get()
    if len(highest_valves) > 0:
        for i in highest_valves:
            valves_copy = valves
            pathways(curr_valve, i, valves_copy)
    elif len(lowest_valves > 0):
        
    else:
        minutes-=1
        total_pres+=flow_rate
