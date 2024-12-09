
# num L R U D 
#  6  4 3 5 2
#  5  4 3  1 6 
# 1 2 3 4 5 6
 

#6215 # 43 

# R
# 3245 # 61 
# L 
# 4235 # 16 

def diceR(dice) : 
    newDice = [
        lst[:] for lst in dice
    ]

    newDice[0][0] = dice[1][1]
    newDice[0][2] = dice[1][0]
    newDice[1][0] = dice[0][0]
    newDice[1][1] = dice[0][2]

    return newDice

def diceL(dice) : 
    newDice = [
        lst[:] for lst in dice
    ]

    newDice[0][0] = dice[1][0]
    newDice[0][2] = dice[1][1]
    newDice[1][0] = dice[0][2]
    newDice[1][1] = dice[0][0]

    return newDice

def diceU(dice) : 
    newDice = [
        lst[:] for lst in dice
    ]
    
    for i in range(1,4) : 
        newDice[0][i] = dice[0][i-1]
    newDice[0][0] = dice[0][3]

    return newDice

def diceD(dice) :
    newDice = [
        lst[:] for lst in dice
    ]
    for i in range(3) :
        newDice[0][i] = dice[0][i+1]
    newDice[0][3] = dice[0][0]
    return newDice

def valid(x,y) :
    global n 
    if x<0 or x>=n or y <0 or y>=n :
        return False
    return True
n,m,r,c = tuple(map(int,input().split()))

d = input().split()

grid = [
    [0 for _ in range(n)] for _ in range(n)
]

dice = [[6,2,1,5], [4,3]]
r-=1
c -=1
grid[r][c] = dice[0][0]

dx,dy = [0,0,1,-1],[-1,1,0,0]

for s in d : 
    if s == "L" : 
        x,y = r+dx[0], c+dy[0] 
        if not valid(x,y) :
            continue 
        dice = diceL(dice)
        
    elif s == "R" :
        x,y = r+dx[1], c+dy[1] 
        if not valid(x,y) :
            continue 
        dice = diceR(dice)    
    elif s == "U" :
        x,y = r+dx[2], c+dy[2] 
        if not valid(x,y) :
            continue 
        dice = diceU(dice)
    elif s =="D" :

        x,y = r+dx[3], c+dy[3] 
        if not valid(x,y) :
            continue 
        dice = diceD(dice)
    r,c = x,y
    grid[r][c] = dice[0][0]

answer = 0
for i in range(n) :
    for j in range(n) :
        answer +=grid[i][j]
print(answer)