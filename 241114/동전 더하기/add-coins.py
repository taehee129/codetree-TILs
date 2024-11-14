n,k = tuple(map(int, input().split()))

lst =[
    int(input())
    for _ in range(n)
]
lst.sort(reverse=True)

cnt =0
while k >0 :
    
    for val in lst :
        if k >= val:
            k -= val 
            cnt+=1
            break

print(cnt)
            
    