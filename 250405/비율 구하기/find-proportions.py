n = int(input())

from sortedcontainers import SortedDict 


sd = SortedDict()


for _ in range(n) : 
    s = input()

    if s in sd :
        sd[s] +=1 
    else :
        sd[s] =1 

for k,v in sd.items() : 
    print(k, '{:.4f}'.format(round((v/n)*100,4) ))