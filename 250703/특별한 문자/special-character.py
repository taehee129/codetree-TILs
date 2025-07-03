string = input()

d= {}
for s in string : 
    if s in d :
        d[s] +=1
    else : 
        d[s] =1 



flag = ''
for s in string : 
    if d[s] == 1 :
        print(s)
        flag = True 
        break

if not flag :
    print('None')
