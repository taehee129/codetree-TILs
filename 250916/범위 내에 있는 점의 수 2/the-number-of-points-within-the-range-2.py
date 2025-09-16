n,q = map(int,input().split())

dots = list(map(int,input().split()))

ranges = [tuple(map(int,input().split())) for _ in range(q)]

prefix_sum = [0]*(10**6)

for dot in dots : 
    prefix_sum[dot-1] = 1 

for i in range(1,10**6) : 
    prefix_sum[i] = prefix_sum[i-1] + prefix_sum[i]

for i in range(q) : 
    x,y = ranges[i]
    #print(prefix_sum[y-1],prefix_sum[x-2])
    print(prefix_sum[y-1]-prefix_sum[x-2])
