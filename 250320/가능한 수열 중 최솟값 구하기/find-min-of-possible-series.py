n = int(input())

nums = [4,5,6]

answer = [] 

def in_range(x) : 
    if x<0 or x>= len(answer) : 
        return False
    return True

def check() :
    l = len(answer)
    for i in range(1,l) : 
        flag = False
        start_idx = l -i 
        start_idx2 = start_idx -i
        for j in range(i) : 
    
            if not (in_range(start_idx+j) and in_range(start_idx2+j)) :
                return True 
            if answer[start_idx+j] != answer[start_idx2+j] :
                flag = True         
                break 
        if not flag : 
            return False
    return True
            
    
def choose(idx) :
    #print(answer)
    if idx == n : 
        print(''.join(map(str,answer)))
        return True 
    
    for i in range(3) : 
        answer.append(nums[i])
        if not check() :
            answer.pop()
            continue         
        if choose(idx+1) :
            return True
        answer.pop()

choose(0)