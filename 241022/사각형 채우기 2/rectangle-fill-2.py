n = int(input())

lst = [0 for _ in range((n if n>=2 else 2))]


lst[0]=1
lst[1]= 3 


for i in range(2,n) :

    lst[i] = lst[i-1]+lst[i-2]*2


print(lst[n-1]%10007)