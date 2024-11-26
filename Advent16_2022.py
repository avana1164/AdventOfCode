import copy
from queue import Queue
queue = Queue()
file = open('adventfile16_2022', 'r')
f = file.readlines()
valves = {}


for line in f:
    line = line.strip()
    line = line.split(" ")
    connections = []
    for i in range(9, len(line)):
        connection = line[i].replace(",", "")
        connections.append(connection)
    
    rate = line[4].replace("rate=", "")
    rate = rate.replace(";", "")
    
    valves[line[1]] = [int(rate), connections]


