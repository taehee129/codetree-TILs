n = int(input())

nums = list(map(int,input().split()))
hs = set()


for num in nums :
    hs.add(num)

print(len(hs))