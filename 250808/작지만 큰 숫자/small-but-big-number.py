from sortedcontainers import SortedSet 

n,m = map(int,input().split())

nums = list(map(int,input().split()))

plus= list(map(int,input().split()))
s = SortedSet(nums)

for num in plus : 
    if num <s[0] : 
        print(-1)
        continue 
    x = s.bisect_right(num)-1
    print(s[x])
    s.remove(s[x])
    


    