n,g = map(int,input().split())

hs = set()
hs.add(1)

def check(lst) : 
    
    idx = False
    cnt = 0
    lst_len = len(lst)
    for i in range(lst_len) :
        if lst[i] in hs : 
            cnt+=1
        else : 
            idx = i 
        
    if cnt == lst_len-1 :
        return lst[idx]
    else : 
        return -1



glst = [list(map(int,input().split())) for _ in range(g)]


while True : 
    flag =False
    for lst in glst : 
        ret = check(lst[1:])
        if ret != -1 :
            hs.add(ret)
            flag = True
    if not flag : 
        break

print(len(hs))

        