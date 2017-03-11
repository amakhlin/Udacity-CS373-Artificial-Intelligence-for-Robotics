# ----------
# User Instructions:
# 
# Create a function compute_value() which returns
# a grid of values. Value is defined as the minimum
# number of moves required to get from a cell to the
# goal. 
#
# If it is impossible to reach the goal from a cell
# you should assign that cell a value of 99.

# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 5]
goal = [len(grid)-1, len(grid[0])-1]



delta_name = ['^', '<', 'v', '>']

cost_step_adj = 1 # the cost associated with moving from a cell to an adjacent one.
cost_step_diag = 1.5

# ----------------------------------------
# insert code below
# ----------------------------------------

def compute_cost_to_goal(grid, init, goal, cost_step_adj, cost_step_diag):
    delta = [[-1, 0 ], # 0 go up
             [ 0, -1], # 1 go left
             [ 1, 0 ], # 2 go down
             [ 0, 1 ], # 3 go right
             [-1, -1], # 4 diag up-left
             [-1, 1],  # 5 diag up-right
             [1, -1],  # 6 diag down-left
             [1, 1],]  # 7 diag down-right
             
    value = [[999 for row in range(len(grid[0]))] for col in range(len(grid))]
    value[goal[0]][goal[1]] = 0
    open = []
    open.append([ 0, goal[0], goal[1]])
    visited = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    visited[goal[0]][goal[1]] = 1
    
    while(1):
        if len(open) == 0:
            break;
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            x = next[1]
            y = next[2]

            for i in range(len(delta)):
                x2 = x + delta[i][0]
                y2 = y + delta[i][1]
                if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                    if visited[x2][y2] == 0 and grid[x2][y2] == 0:
                        if i < 4:
                            cost = cost_step_adj
                        else:
                            cost = cost_step_diag                  
                        value[x2][y2] = value[x][y] + cost
                        open.append([value[x2][y2], x2, y2])
                        visited[x2][y2] = 1
                        
                            
    #for i in range(len(value)):
    #    print value[i]
    return value[init[0]][init[1]] # return cost to the goal from the init state

print compute_cost_to_goal(grid, init, goal, cost_step_adj, cost_step_diag)