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
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
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
    
    expand = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    expansion_index = 0
    expand[init[0]][init[1]] = expansion_index
    expansion_index +=1
    
    sol = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    
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
                    visited[cell_0][cell_1] = -1
                    expand[cell_0][cell_1] = expansion_index
                    expansion_index += 1
                    #print cell_0, cell_1
                    if( [cell_0, cell_1] == goal):
                        path = [open[i][0] + 1, cell_0, cell_1]
        
        open.pop(i);
        if(len(open)== 0):
            path = 'fail'
            break
            
        if(path != 0):
            break
    
    # found the expansion
    print expand[0]
    print expand[1]
    print expand[2]
    print expand[3]
    print expand[4]
    
    
    cell_0 = 0
    cell_1 = 0
    while(1):
        max_cost = -100
        max_cost_0 = 0
        max_cost_1 = 0
        max_cost_action = ''
        for j in range(len(delta)):
            x = cell_0 + delta[j][0]
            y = cell_1 + delta[j][1]
            if(x>=0 and x <=(len(grid)-1) and y >= 0 and y <= (len(grid[0])-1)):
                if(expand[x][y] > max_cost):
                    max_cost = expand[x][y]
                    max_cost_0 = x
                    max_cost_1 = y
                    max_cost_action = delta_name[j]

        #print cell_0, cell_1
        #print max_cost_0, max_cost_1
        sol[cell_0][cell_1] = max_cost_action
        cell_0 = max_cost_0
        cell_1 = max_cost_1
        if([max_cost_0, max_cost_1] == goal):
            sol[max_cost_0][max_cost_1] = '*'
            break;
            
        if(expand[max_cost_0][max_cost_1] == max(max(expand))):
            break;
            
    return sol # you should RETURN your result

e=search()
print e[0]
print e[1]
print e[2]
print e[3]
print e[4]