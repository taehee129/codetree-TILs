n = int(input())

b = [input() for _ in range(n)]

def hsp(a,b) :

    if a == 'H' : 
        if b == 'S' : 
            return 1 

    if a =='S' :
        if b =='P' :
            return 1 
    
    if a =='P' :
        if b == 'H' : 
            return 1 
    
    return 0 

hl = [0]*n
hr = [0]*n

sl = [0]*n
sr = [0]*n 

pl = [0]*n
pr = [0]*n 

hl[0] = hsp('H',b[0])
sl[0] = hsp('S',b[0])
pl[0] = hsp('P',b[0])

for i in range(1,n) : 
    hl[i] = hl[i-1] + hsp('H',b[i])
    sl[i] = sl[i-1] + hsp('S',b[i])
    pl[i] = pl[i-1] + hsp('P',b[i])


hr[n-1] = hsp('H',b[n-1])
sr[n-1] = hsp('S',b[n-1])
pr[n-1] = hsp('P',b[n-1])

for i in range(n-2,-1,-1) : 
    hr[i] = hr[i+1] + hsp('H',b[i])
    sr[i] = sr[i+1] + hsp('S',b[i])
    pr[i] = pr[i+1] + hsp('P',b[i])


ans = 0 

ans = max(hl[n-1],sl[i],pl[i])
for i in range(n-1) : 
    lst = [
    hl[i] + sr[i+1],
    hl[i] + pr[i+1],
    sl[i] + hr[i+1],
    sl[i] + pr[i+1],
    pl[i] + sr[i+1],
    pl[i] + sr[i+1]
    ] 

    maxval = max(lst) 

    ans = max(ans,maxval)

print(ans)