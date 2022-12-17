from queue import Queue 
queue = Queue()
file = open('adventfile12_2022')
f = file.readlines()
curr_node = ()
targ_node = ()
grid = {}
line_num = 1
for line in f:
    s = line.strip()
    for i in range(len(s)):
        if s[i] == 'S' or s[i] == 'a':
            curr_node = (i + 1, line_num)
            queue.put(curr_node)
            grid[(i + 1, line_num)] = [0, 'a']
        elif s[i] == 'E':
            targ_node = (i + 1, line_num)
            grid[(i + 1, line_num)] = [-1, 'z']
        else:
            grid[(i + 1, line_num)] = [-1, s[i]]
    line_num+=1
while curr_node != targ_node:
    u = queue.get()
    up = (u[0], u[1] - 1)
    down = (u[0], u[1] + 1) 
    right = (u[0] + 1, u[1])
    left = (u[0] - 1, u[1])
    if u == targ_node:
        curr_node = targ_node
        continue

    if up in grid:
        if (ord(grid[u][1]) + 1 == ord(grid[up][1]) or ord(grid[u][1]) >= ord(grid[up][1])) and grid[up][0] == -1:
            grid[up][0] = grid[u][0] + 1 
            queue.put(up)        
    
    if down in grid:
        if (ord(grid[u][1]) + 1 == ord(grid[down][1]) or ord(grid[u][1]) >= ord(grid[down][1])) and grid[down][0] == -1:
            grid[down][0] = grid[u][0] + 1
            queue.put(down)
    
    if left in grid:
        if (ord(grid[u][1]) + 1 == ord(grid[left][1]) or ord(grid[u][1]) >= ord(grid[left][1])) and grid[left][0] == -1:
            grid[left][0] = grid[u][0] + 1
            queue.put(left)
    
    if right in grid:
        if (ord(grid[u][1]) + 1 == ord(grid[right][1]) or ord(grid[u][1]) >= ord(grid[right][1])) and grid[right][0] == -1:
            grid[right][0] = grid[u][0] + 1
            queue.put(right)
print(grid[targ_node][0])     