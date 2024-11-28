file = open('d8', 'r')
f = file.readlines()
grid = []
sum = 0
high_score = 1
for line in f:
    s = line.strip()   
    row_length = len(s)
    row = []
    for i in range(row_length):
        row.append(s[i])
    grid.append(row)   

for i in range(1, 98):
    for j in range(1, row_length - 1):
        scenic_score = 1
        tree_height = int(grid[i][j])             
        for k in range(j + 1, row_length):           
            if int(grid[i][k]) >= tree_height or k == row_length - 1:

                scenic_score*=(k-j)                         
                break             

        for k in range(j - 1, -1, -1):
            if int(grid[i][k]) >= tree_height or k == 0:               
                scenic_score*=(j-k)
                break 
        
        for k in range(i + 1, 99):
            if int(grid[k][j]) >= tree_height or k == 98:              
                scenic_score*=(k-i)
                break 

        for k in range(i - 1, -1, -1):
            if int(grid[k][j]) >= tree_height or k == 0:
                scenic_score*=(i-k)
                break 
        
        if(scenic_score > high_score):
            high_score = scenic_score     

print(high_score)