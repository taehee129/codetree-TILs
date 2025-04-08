n,m = map(int,input().split())

lst = list(input() for _ in range(n*2))

cnt =0
for i in range(m) : 
    for j in range(i+1,m) :
        for k in range(j+1,m) : 
            l1 = []
            l2 = []
            s1 = set()
            s2 = set()
            flag = True
            for idx in range(n) :
                combi = lst[idx][i]+lst[idx][j]+lst[idx][k]
                combi2 = lst[idx+n][i]+lst[idx+n][j]+lst[idx+n][k]
                s1.add(combi)
                l1.append(combi)
                l2.append(combi2)
                s2.add(combi2)

            
            for s in l1 :
                if s in s2 :
                    flag = False
                    break
            
            for s in l2 :
                if s in s1 :
                    flag= False 
                    break 
            
            if flag : 
                # print('-'*50)
                # print(i,j,k)
                # print(s1)
                # print(s2)
                cnt +=1


print(cnt)                  


                 

                


