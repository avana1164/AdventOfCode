file = open('d6', 'r')
f = file.readlines()
s = f[0]
for j in range(len(s) - 13):
    duplicate = False
    smallstr = s[j:j+14]
    for i in range(14):
        if smallstr.count(smallstr[i]) > 1:          
            duplicate = True
    
    if duplicate == False:
        print(j + 14)
        break   