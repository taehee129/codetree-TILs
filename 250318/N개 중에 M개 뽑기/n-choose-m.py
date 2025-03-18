n,m = map(int,input().split())

nums = [i for i in range(1,n+1)]


answer_list =[]

def choose(idx) : 
    if len(answer_list) == m :
        print(' '.join(map(str,answer_list)))

    for i in range(idx,n):
        answer_list.append(nums[i])
        choose(i+1)
        answer_list.pop()


choose(0)
    