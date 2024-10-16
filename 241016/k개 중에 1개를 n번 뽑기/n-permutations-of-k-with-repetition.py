K,N =  tuple(map(int,input().split()))

lst=[]

def choose(n, s) :
    global K
    global N
    if n==N :
        lst.append(s)
        return

    for i in range(1,K+1) :
        choose(n+1, s+" "+str(i))

choose(0,'')

for s in lst :
    print(s[1:])