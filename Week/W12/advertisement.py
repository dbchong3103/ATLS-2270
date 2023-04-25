'''
Name: Dahn Bi Chong
Problem: Advertisement
Objective: Determine the maximum area that a rectangular advertisement can be for a specific length of fence that has inconsistent height. NOte, this code doesn't work but I tried and failed.
'''
#Create input list
nums = int(input())

area = [] #store possible areas
stack = []
minHeight = -1
for idx, num in enumerate(nums): # i = 2, n = 5
	if minHeight == -1: #Set a minimum height
		minHeight = num
	elif minHeight > num:
		minHeight = num
        
	while stack and stack[-1][0] >= num:
		stack.pop()

	area.append((minHeight)*(idx+1)) if not stack else (stack[-1][0])*((idx+1)-(stack[-1][1])) #Determines where in the index the NSE is
	stack.append((num, idx))

print(max(area)) #print the maximu possible value