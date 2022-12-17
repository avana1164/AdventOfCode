file = open('adventfile7_2022.txt', 'r')
f = file.readlines()
directories = {}
sum = 0
curr_dir = ""
duplicate_values = 1
for line in f:
    s = line 
    s = s.split()  
    if s[1] == "cd" and s[2] == "..":
        curr_dir = directories[curr_dir][1]
    elif s[1] == "cd" and s[2] != "..": 
        if len(directories) > 0:
            for i in directories[curr_dir][2]:
                if s[2] in i:                    
                    curr_dir = i
                    break 
        else:
            curr_dir = s[2]          
        if curr_dir not in directories.keys():
            directories[curr_dir] = [0, "", []]        
    elif s[0] == "dir":  
        dir_name = s[1]
        if dir_name in directories.keys(): 
            dir_name = s[1] + str(duplicate_values)
            duplicate_values+=1

        directories[curr_dir][2].append(dir_name)        
        directories[dir_name] = [0, curr_dir, []] 
    elif s[0] != '$' and s[0] != "dir":  
        num = int(s[0])    
        directories[curr_dir][0] += num 
        if curr_dir != '/':
            back_track = directories[curr_dir][1]
            directories[back_track][0] += num  
            while(back_track != '/'):
                back_track = directories[back_track][1]
                directories[back_track][0] += num
space_unused = 70000000 - directories['/'][0]
min_delete = directories['/'][0]

for i in directories:   
    if space_unused + directories[i][0] >= 30000000 and directories[i][0] < min_delete:
        min_delete = directories[i][0]
print(min_delete)