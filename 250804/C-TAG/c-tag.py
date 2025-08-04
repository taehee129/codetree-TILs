n,m = map(int,input().split())

a_alphas = [input() for _ in range(n)]

b_alphas = [input() for _ in range(n)]

cnt = 0
for i in range(m) : 
    for j in range(i+1,m) : 
        for k in range(j+1,m) : 
            
            flag = True
            s = set()
            for a in a_alphas :
                s.add(a[i]+a[j]+a[k])
            
            for b in b_alphas : 
                b_alpha = b[i] + b[j] + b[k]
              
                if b_alpha in s : 
                    flag = False
                    break 
            
            if flag : 
                cnt +=1 

print(cnt)

            