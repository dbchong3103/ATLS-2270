'''
Name: Dahn Bi Chong
Problem: Fruit feast
Objective: Bessie is insane and thinks that for some odd reason she can just have endless oranges and cows. The goal of this code is to determine how many oranges and lemons she can freaking eat by determining how full she can actually get.
'''

from collections import deque

#Opens ze heccking file and max is for maximum fullness aka T, then oranges and lemons as a and b respectivly
with open("feast.in") as read:
	t, a, b = map(int, read.readline().split())

possibile = {(0, False)}  # Keep track of which states we visited
to_process = deque([(0, False)])

#while loop process all changes in food
while to_process:
	full, water = to_process.pop()

	# Drink water and then change teh fullness
	if not water:
		yesWater = (full // 2, True)
		if water not in possibile:
			to_process.appendleft(yesWater)
			possibile.add(yesWater)

	# Eat a fruit and add to the fullness
	for fruit in (a, b):
		after = full + fruit
		to_add = (after, water)
		if after <= t and to_add not in possibile:
			to_process.appendleft(to_add)
			possibile.add(to_add)

#print out the final fullness
best = max([n[0] for n in possibile])
print(best, file=open("feast.out", "w"))