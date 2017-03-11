# ----------
# User Instructions:
# 
# Define a function, search() that takes no input
# and returns a list
# in the form of [optimal path length, x, y]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1] # Make sure that the goal definition stays in the function.

delta = [[-1, 0 ], # go up
        [ 0, -1], # go left
        [ 1, 0 ], # go down
        [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost = 1

def search():
    # ----------------------------------------
    # insert code here and make sure it returns the appropriate result
    # ----------------------------------------
    visited = grid;
    open = [];
    open.append([0, init[0], init[1]])
    visited[init[0]][init[1]] = -1
    path = 0
    
    while(1):
        min_cost = 1000;
        min_cost_index = 0;
        for i in range( len(open)):
            if(open[i][0] < min_cost):
                min_cost = open[i][0]
                min_cost_index = i
        
        i = min_cost_index
        for j in range(len(delta)):
            cell_0 = open[i][1] + delta[j][0]
            cell_1 = open[i][2] + delta[j][1]
            if(cell_0 >=0 and cell_0 <=(len(grid)-1) and cell_1 >= 0 and cell_1 <= (len(grid[0])-1)):
                if(grid[cell_0][cell_1] != 1 and visited[cell_0][cell_1] != -1):
                    open.append([open[i][0] + 1, cell_0, cell_1])
                    if( [cell_0, cell_1] == goal):
                        path = [open[i][0] + 1, cell_0, cell_1]
        visited[open[i][1]][open[i][2]] = -1
        open.pop(i);
        if(len(open)== 0):
            path = 'fail'
            break
            
        if(path != 0):
            break
    
    return path # you should RETURN your result

print search()
