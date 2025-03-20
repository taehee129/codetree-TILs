k,n = map(int,input().split())



nums = [i for i in range(1,k+1)]

answer = []



def choose() : 
    if len(answer)== n :
        print(' '.join(map(str,answer)))
        return 
    
    for i in range(1,k+1) : 
        answer_len = len(answer)
        if answer_len >=2 and answer[answer_len-1] == i and answer[answer_len-2] == i :
            continue
        answer.append(i)
        choose()
        answer.pop()

choose()
    
    
