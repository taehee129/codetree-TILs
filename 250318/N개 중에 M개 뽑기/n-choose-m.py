n,m = map(int,input().split())

nums = [i for i in range(1,n+1)]


combination = []

def print_num() :
    answer_list = []
    for i in range(len(combination)):
        if combination[i] !=0 :
            answer_list.append(nums[i])
    
    print(' '.join(map(str,answer_list)))
            

def choose(num,cnt) :
    if cnt == m : 
        print_num()
        return 
    
    if num == n : 
        return 
    
    combination.append(1)
    choose(num+1,cnt+1)
    combination.pop()

    combination.append(0)
    choose(num+1,cnt)
    combination.pop()

choose(0,0)

    
    