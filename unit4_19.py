# ----------
# User Instructions:
# 
# Implement the function optimum_policy2D() below.
#
# You are given a car in a grid with initial state
# init = [x-position, y-position, orientation]
# where x/y-position is its position in a given
# grid and orientation is 0-3 corresponding to 'up',
# 'left', 'down' or 'right'.
#
# Your task is to compute and return the car's optimal
# path to the position specified in `goal'; where
# the costs for each motion are as defined in `cost'.

# EXAMPLE INPUT:

# grid format:
#     0 = navigable space
#     1 = occupied space 
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]
goal = [2, 0] # final position
init = [4, 3, 0] # first 2 elements are coordinates, third is direction
cost = [2, 1, 20] # the cost field has 3 values: right turn, no turn, left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D() should return the array
# 
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
#
# ----------


# there are four motion directions: up/left/down/right
# increasing the index in this array corresponds to
# a left turn. Decreasing is is a right turn.

forward = [[-1,  0], # go up
           [ 0, -1], # go left
           [ 1,  0], # go down
           [ 0,  1]] # do right
forward_name = ['up', 'left', 'down', 'right']

# the cost field has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']


# ----------------------------------------
# modify code below
# ----------------------------------------

def optimum_policy2D():
    policy2D = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    # value[orientation][x][y] -> y, x, orientation
    value = [[[999 for row in range(len(grid[0]))] for col in range(len(grid))] for k in range(len(forward))]

    change = True
    while(change):
        change = False
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                for o in range(len(forward)):
                    if(grid[x][y]!=0):
                        continue
                    # goal cell
                    if(x == goal[0] and y == goal[1] and o == 1):
                        if(value[o][x][y] != 0):
                            value[o][x][y] = 0
                            policy2D[x][y] = '*'
                            change = True
                    # not a goal cell
                    # iterate over actions
                    for a in range(len(action)):
                        x2 = x + forward[ (o + action[a]) % 4 ][0]
                        y2 = y + forward[ (o + action[a]) % 4 ][1]
                        o2 = (o + action[a]) % 4
                        if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]) and grid[x2][y2] == 0:
                            v2 = value[o2][x2][y2] + cost[a]
                            if(v2 < value[o][x][y]):
                                value[o][x][y] = v2
                                change = True
                                #policy2D[x][y] = action_name[a]
    
    # for x in range(len(grid)):
        # for y in range(len(grid[0])):
            # for o in range(len(forward)):
                # # goal cell
                # print x, y, o, '-> ', value[o][x][y]
    
    x = init[0]
    y = init[1]
    o = 0
    while(1):
        if(x == goal[0] and y == goal[1]):
            policy2D[x][y] = '*'
            break
            
        v_min = 999
        for a in range(len(action)):
            x2 = x + forward[ (o + action[a]) % 4 ][0]
            y2 = y + forward[ (o + action[a]) % 4 ][1]
            o2 = (o + action[a]) % 4
            if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]) and grid[x2][y2] == 0:
                if((value[o2][x2][y2] + cost[a]) < v_min):
                    v_min = value[o2][x2][y2] + cost[a]
                    v_min_x = x2
                    v_min_y = y2
                    v_min_o = o2
                    v_min_action = action_name[a]
                    #print 'considering ', x2, y2, o2, v_min
        
        
        policy2D[x][y] = v_min_action
        x = v_min_x
        y = v_min_y
        o = v_min_o
        #print 'picked ^^^^^^^^^^', x, y, o, v_min
        
    
    for i in range(len(policy2D)):
        print policy2D[i]
        
    return policy2D # Make sure your function returns the expected grid.

optimum_policy2D()

