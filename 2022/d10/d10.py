file = open('d10', 'r')
f = file.readlines()
X = 1
cycle = 0
sig_str = 0
CRT_row = ""
def check_cycle(cycle, X):
    return cycle*X

for line in f:
    s = line.strip()
    if s == "noop":
        cycle += 1 
        if cycle - 1 >= X - 1 and cycle - 1 <= X + 1:
            CRT_row+='#'
        else:
            CRT_row+='.'

        if cycle == 40:
            print(CRT_row)
            cycle = 0
            CRT_row = ""    

        """if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
            sig_str+=check_cycle(cycle, X) for part 1"""           
    elif "addx" in s:
        s = s.split()
        for _ in range(2):
            cycle += 1
            if cycle - 1 >= X - 1 and cycle - 1 <= X + 1:
                CRT_row+='#'
            else:
                CRT_row+='.'
            
            if cycle == 40:
                print(CRT_row)
                CRT_row = ""
                cycle = 0

            """if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
                sig_str+=check_cycle(cycle, X) for part 1"""                           
        X+=int(s[1]) 
#print(sig_str) for part 1