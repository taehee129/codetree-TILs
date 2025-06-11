n,m = map(int,input().split())

nums = list(map(int,input().split()))

def upper_bound(target) :
    left = 0
    right=n-1 
    min_idx = n 

    while left <= right :
        mid = (left + right) //2 

        if nums[mid] >= target : 
            min_idx = min(mid,min_idx) 
            right = mid -1 
        else : 
            left = mid +1 
    
    return min_idx 

questions = list(map(int,input().split()))


for num in questions : 
    ans = upper_bound(num) 

    if ans==n or num != nums[ans]:
        print(-1) 
    else : 
        print(ans+1)