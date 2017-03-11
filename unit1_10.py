p=[0.2,0.2,0.2,0.2,0.2]
cells=['green', 'red', 'red', 'green', 'green']
pHit = 0.6
pMiss = 0.2

for i in range(len(p)):
	if cells[i] == 'red':
		p[i] *= pHit;
	else:
		p[i] *= pMiss;

print p