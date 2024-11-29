# 

# 111 
#
# 왼쪽 오른쪽 
# 어떤 것을 


#
# 212
# 시계 반대 방향 

# 323 212 시계 반대 방향으로 가던지 
# 323 423 333  324 에서 시계 방향으로 간다.

# 111


#   dp[n][m][k] = dp[n-1][m][k]  
    #
#    251  왼쪽으로 9 번 회존했을 때 51 왼쪽으로 9 회전하고 n 번째로 오른쪽으로 x 번  
#     1~9 10~99                 

n = int(input())

orgin = input()

goal = input()

n2=n

n =10**(n-1)
dp = [[10000000 for _ in range(10)] for _ in range(n)]

def right(orgin, goal) :
    lst = [0,1,2,3,4,5,6,7,8,9]
    x= 0

    for k in range(10) : 
        if lst[orgin-x] == goal :
            break
        x+=1 

    return x
# o  j   left i  
# dp[0][0] 처음 '1' 에서 왼쪽으로 j 번 돌렸을 때 i 가 되기 위해 회전해야 하는 최솟값

for i in range(10) :
    for j in range(10) : 
        val = int(orgin[n2-1]) #첫 번째 값
        leftValue = (val+j)%10 # 왼쪽으로 회전한 후의 값
        dp[i][j] = right(leftValue,i)+j
        # print(x,j)
# for i in range(10)  :
#     print(dp[i])   



# 1  0   1    0   1  0+1 1 
# 1  1   2    0   2  1+2 3
# 1  2   3    0   3  2+3 5 
# 1  3   4    0   4  3+4 7

#  왼쪽 회전(다같이 회전되는 것)은 커지고 오른쪽 회전은 작아진다
#  11 -> 10 
#  11 -> 한 번 회전후(00) -> 10 ->

# 11 0  11  10  0+0+1 = 1
# 11 1  22  10  1+1+2 = 4  
# 11 2  33  10  2+2+3 = 7
# 11 3  88  10  


for i in range(10,n) :
    for j in range(10) :
            val = int(str(i)[1:])# 241 -> 41
            val2 = int(str(i)[0])# 241 -> 2 # 되고자 하는 값
            
            orginVal = int(orgin[1]) #첫
            leftValue = (orginVal+j)%10 #만큼 왼쪽으로 회전

            dp[i][j] = dp[val][j] + right(leftValue,val2)
    # print(i, dp[i])
    # print()

            

val = int(str(goal)[1:])# 241 -> 41
val2 = int(str(goal)[0])# 되고자 하는 값 

orginVal = int(orgin[0]) #첫 번째 값
answer =10000000

for i in range(10) :
    leftValue = (orginVal+i)%10

    answer = min(answer, dp[val][i] + right(leftValue,val2)) 


print(answer)
