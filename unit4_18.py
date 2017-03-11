# ----------
# User Instructions:
# 
# Create a function optimum_policy() that returns
# a grid which shows the optimum policy for robot
# motion. This means there should be an optimum
# direction associated with each navigable cell.
# 
# un-navigable cells must contain an empty string
# WITH a space, as shown in the previous video.
# Don't forget to mark the goal with a '*'

# ----------

# grid = [[0, 1, 0, 0, 0, 0],
        # [0, 1, 0, 0, 0, 0],
        # [0, 1, 0, 0, 0, 0],
        # [0, 1, 0, 0, 0, 0],
        # [0, 0, 0, 0, 1, 0]]

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]        
  

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost_step = 1 # the cost associated with moving from a cell to an adjacent one.

# ----------------------------------------
# insert code below
# ----------------------------------------

def optimum_policy():
    policy = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    policy[ goal[0] ][ goal[1] ] = '*'
    value = [[99 for row in range(len(grid[0]))] for col in range(len(grid))]
    value[goal[0]][goal[1]] = 0
    open = []
    open.append([ 0, goal[0], goal[1]])
    visited = grid
    visited[goal[0]][goal[1]] = 2
    
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
                        value[x2][y2] = value[x][y] + 1
                        open.append([value[x2][y2], x2, y2])
                        visited[x2][y2] = 2
                        policy[x2][y2] = delta_name[ (i + 2) % 4 ]
                        
                            
    for i in range(len(value)):
        print policy[i]
    return value #make sure your function returns a grid of values as demonstrated in the previous video.

optimum_policy()

