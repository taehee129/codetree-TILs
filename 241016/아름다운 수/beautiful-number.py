N= int(input())


def isBeauty(n) :
    n = str(n)
    
    before=n[0]
    cnt=0
    for s in n:
        if s ==before :
            cnt+=1
        else :
            flag = cnt%(int(before))
            if flag != 0 :
                return False 
            cnt=1
        before=s  

    flag = cnt%(int(before))
    if flag != 0 :
        return False 
    
    return True


answer=0
def permutaion(s,n) :
    global answer
    if n==N  :
        if isBeauty(s) :
            answer+=1
        
        return


    

    for i in range(1,5):
        permutaion(s+str(i),n+1)

        
permutaion('',0)
print(answer)