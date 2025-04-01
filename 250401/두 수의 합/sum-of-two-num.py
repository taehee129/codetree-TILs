n,k = map(int,input().split())


nums = list(map(int,input().split()))

com = []
end = len(nums)
cnt = 0
def combination(idx) :
    global cnt
    if len(com) == 2 :
        if com[0] + com[1] == k:
            cnt+=1
    
    for i in range(idx,end) : 
        com.append(nums[i])
        combination(i+1)
        com.pop()
     
combination(0)
print(cnt)