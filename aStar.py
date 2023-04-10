import copy
Size = 15
def Astar(start , goal , data):
    openlist = [start]
    closedlist = []
    while len(openlist):
        current = openlist[min_index(openlist)]
        if current[1] == goal[1] and current[2] == goal[2]:
            return current

        closedlist.append(current)
        openlist.remove(current)
        for i in range(1,3):
            for j in range(-1,2):
                helper(current,data,closedlist,openlist,goal,i,j)


def helper(current,data,closedlist,openlist,goal,i,j):
    neighbour = current.copy()
    if j:
        if current[i] + j >= 0 and current[i] + j < Size:
            neighbour[i] = current[i] + j
                        
            if check_black(neighbour , data):

                tmp_score = current[3] + 1
                neighbour[5] = current
                neighbour[3] = tmp_score
                neighbour[4] = heuristic(neighbour , goal) + tmp_score
                            
                if check_vists(closedlist , neighbour):
                    new = neighbour.copy()
                    openlist.append(new)


def heuristic(location , goal):
    return abs(location[1] - goal[1]) + abs(location[2] - goal[2])

def createData(grid):
    data = []
    d = []

    for row in range(Size):
        for column in range(Size):
            d = [grid[row][column],row,column,0,0]
            data.append(d)

    return data

def min_index(openlist):
    min = 0
    if len(openlist) > 1:
        for i in range(1,len(openlist)):
            if openlist[i][4] < openlist[min][4]:
                min = i
    return min

def check_vists(closed , neighbour):
    for i in range(0,len(closed)):
        if neighbour[1] == closed[i][1] and neighbour[2] == closed[i][2]:

            return 0
    return 1

def check_black(location, data):

    for i in range(len(data)):
        if data[i][0] == 1:
            if data[i][1] == location[1] and data[i][2] == location[2]:

                return 0
    return 1
def getMove(path):
    moves = []
    while path[5] != None:
        moves.append(path[1:3])
        path = path[5]

    return moves

def addPath(grid,path):
    for row in range(Size):
        for column in range(Size):
            for i in range(len(path)):
                if row == path[i][0] and column == path[i][1]:
                    if i == len(path) - 1:
                        grid[row][column] = 4

                    else:
                        grid[row][column] = 3
