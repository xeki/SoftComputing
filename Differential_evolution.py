import random
def fittness(inputVector):
	return	(int(inputVector[0][0])**2 +int(inputVector[0][1]) - 11)**2 + (int(inputVector[0][0]) + int(inputVector[0][1])**2 -7)**2
#for summation of x square
def sumOfSquare(inputVector):
	return 	inputVector[0][0]**2 + inputVector[0][1]**2 + inputVector[0][2]**2 + inputVector[0][3]**2 + inputVector[0][4]**2
def binaryGeneticAlgorithm(N,xl,xu,d,F,co):
	v = [[0]*d for i in range(N)]
	costVector = [[0]*d for i in range(1)]
	trial = [[0]*d for i in range(1)]
	mv = [[0]*d for i in range(1)]
	for i in range(0,N):
		for j in range(0,d):
			v[i][j] = random.randint(xl,xu)
	tempIndex = random.randint(1,N-1)
	for i in range(0,d):
		costVector[0][i] = v[tempIndex][i]
	#score = fittness(costVector)
	score = sumOfSquare(costVector)
	for i in range(0,N):
		ti = i
		loop = True
		while loop:
			c = random.randint(0,N-1)
			if c != ti:
				loop = False
		loop = True
		while loop:
			a = random.randint(0,N-1)
			if a != c & a != ti:
				loop = False
		loop = True
		while loop:
			b = random.randint(0,N-1)
			if b != c & b != ti & b !=a:
				loop = False
		for j in range(0,d):
			trial[0][j] = v[c][j] + F*(v[b][j] - v[a][j])
		k = random.randint(0,d-1)	
		for l in range(0,d):
			if (random.random() <= co) | (l == k):
				mv[0][l] = trial[0][l]
			else:	
				mv[0][l] = v[ti][l]
		newScore = sumOfSquare(mv)
		if newScore < score:
			score = newScore
			costVector = mv
		print("iteration {0} scores = {1}".format(i,newScore))
	print("Minimum score : {0}".format(score))
binaryGeneticAlgorithm(1000,-5,5,5,0.5,0.85)			
	