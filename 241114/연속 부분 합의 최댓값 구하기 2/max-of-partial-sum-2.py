n= int(input())

lst = list(map(int,input().split()))


maxSum = -1000
sumVal =0
for val in lst :
    sumVal += val
    maxSum = max(maxSum, sumVal)
    if sumVal < 0 :
        sumVal=0



print(maxSum)