from re import X

#Creates the list for the buckets!
with open('pails.in') as fin:
	X, Y, M = map(int, fin.readline().split())

#Sets the initial output variable
output = 0

for first in range(M + 1): #This will check all the numbers from 0 to 77 as mentioned in the starter code
	x = X * first
	if x > M:
		break
	
 #This section will make sure we aren't overflowing any pails.
	for second in range(M + 1):
		current = (X*first) + (Y*second)
		if current > M:
			break
		output = max(output, current)

#Prints the output variable into the output file!
print(output, file=open('pails.out', 'w'))

#Note: I just used the code we did in class and was given online as starter code, but changed a few variables to make more sense in my head.