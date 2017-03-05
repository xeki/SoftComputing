import math
from decimal import *
def fatx(fx,x0):
	#4x1**2 - 3x2**2 -6x1x2 -4x1
	return Decimal(fx[0]*(x0[0]**2) +fx[1]*(x0[1]**2) + fx[2]*x0[0]*x0[1] + fx[3]*x0[0])
def fderivatives(x):
    s =[0.0,0.0]
    s[0] =  -1*( 8*x[0]-6*x[1]-4)
    s[1] = -1*(6*x[1] -6*x[0])
    return s
def gradiantdesent(fx,lamda, s1,x0, e):
	tempxi= x0
	tempxj=[0.0,0.0]
	iteration = 1
	s = s1
	tempxj[0] = tempxi[0] + lamda*s[0]
	tempxj[1] = tempxi[1] + lamda*s[1]
	loop = True
	while loop:
		tempxi = tempxj
		fi = fatx(fx,tempxi)
		tempxj[0] = tempxi[0] + lamda*s[0]
		tempxj[1] = tempxi[1] + lamda*s[1]
		fj = fatx(fx,tempxj)
		if fi == 0:
			change = 1
		else:
			change = math.fabs((fj-fi)/fi)
		print("Iteration: {0} \nx1({0}) = {1}, x2({0}) = {2} and x1({3}) = {4}, x2({3}) = {5}\nf{0} = {6}, f{3}={7}\nChangeRate: {8}".format(iteration,tempxi[0]
		,tempxi[1],iteration +1,tempxj[0],tempxj[1],fi,fj,change))
		iteration = iteration + 1
		s = fderivatives(tempxj)
		if(change < e):
			loop = False
		elif (math.fabs(s[0]) < e) and (math.fabs(s[1]) < e):
			loop = False
		#loop = (iteration<50)
fx =[4,3,-6,-4]
lamda = 0.125
s1 = [4,0]
x0 = [0.0,0.0]
e = 0.01	
print("For initial value of x(0,0) and epsilon=0.01 ")	
gradiantdesent(fx,lamda,s1,x0,e)
#print("value {0}".format(fatx(fx,[2.1,2.1])))

		