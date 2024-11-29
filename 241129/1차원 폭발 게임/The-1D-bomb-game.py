# 위의 예에서 

n,m = tuple(map(int,input().split()))

lst = [
    int(input())
    for _ in range(n)
]


bombs = lst[::-1]
totalCnt = 0
while True :
    cnt = 0 
    sameCnt=1
    newBombs =bombs[:]
    for i in range(1,len(bombs)) :
        if bombs[i] == bombs[i-1]  :
            sameCnt +=1 
            
            if i == len(bombs)-1 and sameCnt >=m :
                cnt += sameCnt 
                break
        else :
           
            if sameCnt >=m:
                #폰탄 떠드리고, 
                cnt+=sameCnt
              
            sameCnt =1 
  
        newBombs[i-cnt] = bombs[i]

    
    newBombs = newBombs[0:len(bombs)-cnt]
    bombs =list(newBombs)
    if cnt == 0 :
        break

if m == 1 :
    bombs = []    


bombs = bombs[::-1]

print(len(bombs))
for i in bombs :
    print(i)
