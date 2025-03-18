n = int(input())

grid = [[s for s in input()]  for _ in range(n)]

combination = []

nums = []
nums_coordinate= {}

start = [0,0]
end = [0,0]

for i in range(n) : 
    for j in range(n) : 
        if grid[i][j].isdigit() : 
            nums.append(int(grid[i][j]))
            nums_coordinate[int(grid[i][j])] = (i,j)
        elif grid[i][j] == 'E' : 
            end = [i,j]
        elif grid[i][j] == 'S' : 
            start = [i,j]


nums.sort()

min_dis = 20*20


def cal_dis() :
    
    dis = abs(nums_coordinate[combination[0]][0]- start[0]) +\
        abs(nums_coordinate[combination[0]][1]-start[1])
    for i in range(2) :
        dis += abs(nums_coordinate[combination[i]][0]- nums_coordinate[combination[i+1]][0]) +\
        abs(nums_coordinate[combination[i]][1]- nums_coordinate[combination[i+1]][1])
    dis += abs(nums_coordinate[combination[2]][0]- end[0]) +\
        abs(nums_coordinate[combination[2]][1]-end[1])
    return dis
        


def choose(idx) : 
    global min_dis
    #print('-'*50)
    if len(combination) == 3 :
        #print(combination)
        min_dis = min(min_dis,cal_dis())
        
        #print(min_dis)
        return 

    for i in range(idx, len(nums)) : 
        combination.append(nums[i])
        choose(i+1)
        combination.pop()

choose(0)

if len(nums) >=3 :
    print(min_dis) 
else : 
    print(-1)

