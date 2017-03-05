import random
def fittness(inputVector):
	return	(int(inputVector[0][0])**2 +int(inputVector[0][1]) - 11)**2 + (int(inputVector[0][0]) + int(inputVector[0][1])**2 -7)**2
#for summation of x square
def sumOfSquare(inputVector):
	return 	inputVector[0]**2 + inputVector[1]**2 + inputVector[2]**2 + inputVector[3]**2 + inputVector[4]**2
def binaryGeneticAlgorithm(N,xl,xu,d,F,co):
	v = [[0]*d for i in range(N)]
	trial = [0]*d 
	for i in range(0,N):
		for j in range(0,d):
			v[i][j] = random.uniform(xl,xu)
	bestScore = None
	maxScore = None
	difference = 100
	iteration = 1
	#for i in range(0,N):
	while(iteration < 1000):
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
			k = random.randint(0,d-1)		
			for j in range(0,d):
				if (random.random() < co) or (j == k):
					trial[j] = v[c][j] + F*(v[b][j] - v[a][j])
				else:
					trial[j] = v[ti][j]
			newScore = sumOfSquare(trial)		
			if bestScore== None or newScore < bestScore:
				bestScore = newScore
				for i in range(0,d):
					v[ti][j] = trial[j]
			#if maxScore == None or newScore > maxScore:
				#maxScore = newScore
				#difference = maxScore - bestScore
		iteration = iteration + 1
		print("iteration {0} scores = {1}".format(iteration,newScore))
	print("Minimum score : {0}".format(bestScore))
binaryGeneticAlgorithm(20,-5,5,5,.75,0.85)			
	