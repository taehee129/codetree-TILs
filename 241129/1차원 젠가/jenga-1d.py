def zenga(x,y,lst) :
    return lst[0:x] + lst[y+1:]

n= int(input())

lst= [
    int(input())
    for _ in range(n)
]


for _ in range(2) :
    x,y = tuple(map(int, input().split()))
    lst= zenga(x-1,y-1,lst)

print(len(lst))

for i in lst :
    print(i)