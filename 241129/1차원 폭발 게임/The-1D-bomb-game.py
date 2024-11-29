# 위의 예에서 

n,m = tuple(map(int,input().split()))

lst = [
    int(input())
    for _ in range(n)
]

# 경계값을 항상 조심 1,처음,끝  마지막 값
bombs = lst[::-1]
totalCnt = 0
while True :
    cnt = 0 
    sameCnt=1
    newBombs =bombs[:]

    for i in range(len(bombs)) :
        newBombs[i-cnt] = bombs[i]

        if i>0 and bombs[i] == bombs[i-1] :
            sameCnt +=1 
        else :
            sameCnt = 1

        if sameCnt ==m :
            cnt+=sameCnt
        elif sameCnt >m :
            cnt +=1 
        
    newBombs = newBombs[0:len(bombs)-cnt] 
    bombs = list(newBombs)
    if cnt == 0 or len(newBombs)==0 :
        break
    
    
                  


bombs = bombs[::-1]

print(len(bombs))
for i in bombs :
    print(i)
