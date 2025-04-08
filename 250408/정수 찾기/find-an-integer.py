n = int(input())
lst1 = list(map(int,input().split()))
m = int(input())
lst2 = list(map(int,input().split()))

set1 = set(lst1)
for num in lst2 :
    if num in set1 :
        print(1)
    else :
        print(0)