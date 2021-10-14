name = str(input())
temp = []
temp.append(name[0])

for i in range(1,len(name)):
    
    check = 0
    for j in temp:
        if name[i] == j:
            check = 1
            
            break
    if check == 0:
        temp.append(name[i])
        
    
        

if len(temp) % 2 == 0:
    print('CHAT WITH HER!')
    
else:
    print('IGNORE HIM!')
    
