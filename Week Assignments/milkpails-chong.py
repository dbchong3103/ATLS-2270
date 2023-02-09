from re import X
with open('pails.in') as fin:
	buck1, buck2, order = map(int, fin.readline().split())
 
#print(buck1, buck2, order)

outvar = 0
#outvar should be the final value output

for first in range(order + 1): # this checks all numbers from 0 -> 77
	#print(buck1 * first)
	x = buck1 * first
	if x > order:
		break
	
	for second in range(order + 1):
		current = (buck1*first) + (buck2*second)
		if current > order:
			break
		#print(current)
		outvar = max(outvar, current)

#print(outvar)
print(outvar, file=open('pails.out', 'w'))