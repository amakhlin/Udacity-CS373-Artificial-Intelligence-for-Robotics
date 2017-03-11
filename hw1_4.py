colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

measurements = ['green', 'green', 'green' ,'green', 'green']


motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]

sensor_right = 0.7

p_move = 0.8

def show(p):
    for i in range(len(p)):
        print p[i]

#DO NOT USE IMPORT
#ENTER CODE BELOW HERE
#ANY CODE ABOVE WILL CAUSE
#HOMEWORK TO BE GRADED
#INCORRECT

def myshow(p):
	for i in range(len(p)):
		print ["%0.2f" % j for j in p[i]]

n = len(colors) 	#rows
m = len(colors[0]) 	#cols
p = [[1./(n*m)] * m for i in range(n)] 

def sense(p, Z):
	q=[[0] * m for i in range(n)] 

	for i in range(len(p)):
		for j in range(len(p[i])):
			hit = (Z == colors[i][j])
			q[i][j] = p[i][j] * (hit * sensor_right + (1.-hit) * (1.-sensor_right))
			
	s = 0
	for i in range(len(q)):		
		s += sum(q[i])
	
	for i in range(len(q)):
		for j in range(len(q[i])):
			q[i][j] = q[i][j] / s
	return q

def move(p, U):
	q=[[0] * m for i in range(n)] 
	x = U[1]
	y = U[0]
	
	for i in range(len(p)):
		for j in range(len(p[i])):
			s = p_move * p[(i-y) % n][(j-x) % m]
			s += (1.-p_move) * p[i % n][j % m]
			q[i][j] = s
	return q
	
#Your probability array must be printed 
#with the following code.
# t = [[0] * m for i in range(n)] 
# t[1][2]=1
# myshow(t)
# print '--'
# myshow(move(t, [0,3]))
for i in range(len(motions)):
	p = move(p, motions[i])
	p = sense(p, measurements[i])
	
#myshow(p)
show(p)


