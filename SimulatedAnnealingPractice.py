import random
import math
def fAtXY(x,y):
	return 3*(x**2) - x*y + 2*(y**2)
def simulatedAnneling(x0,y0,t,k):
	Ec = fAtXY(x0,y0)
	while t > 0:
		x1 = random.uniform(0,10)
		y1 = random.uniform(0,10)
		En = fAtXY(x1,y1)
		deltaE = En - Ec
		if deltaE <= 0:
			Ec = En
			xc = x1
			yc = y1
		else:
			Paccept = math.e**(-deltaE/t)
			Prand = random.random()
			if Prand < Paccept:
				Ec = En
				xc = x1
				yc = y1
		t = k*t
	print("Minimizing Energy Function E(x,y) = 3x^2 - x*Y + 2y^2; x,y in [0,10] and T = 1000 with d/t initial values ")
	print("(x0,y0) = ({3},{4}) , (x,y) = ({0},{1}) \nE = {2}\n".format(xc,yc,Ec,x0,y0))

simulatedAnneling(5,5,1000,0.5)
simulatedAnneling(0,0,1000,0.5)	
simulatedAnneling(8,0,1000,0.5)	
