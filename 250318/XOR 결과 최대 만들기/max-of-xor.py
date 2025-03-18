n,m = map(int,input().split())

nums = list(map(int,input().split()))
max_num=0 

lst = []
def choose(idx) :
    global max_num 
    if len(lst) == m :
        val = lst[0]
        for k in range(1,len(lst)) :
            val ^= lst[k]   
        
        max_num = max(max_num, val)

    for i in range(idx,n) : 
        lst.append(nums[i])
        choose(i+1)
        lst.pop()


choose(0)
print(max_num)
