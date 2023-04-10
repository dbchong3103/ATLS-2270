'''
Name: Dahn Bi Chong
Problem: Moocast
Objective: In this problem, I will be looking to compare different cow walkie talkies to determine thenumber of cows
a single cow can broadcast do depending on the power of their walkie-talkie. This will be done by comparing each cow's
postion and power.
'''
#Opens the moocast file and sets up teh number of cows as well as their positions and power
with open("moocast.in") as read:
	cow_num = int(read.readline())
	x = [0 for _ in range(cow_num)]
	y = [0 for _ in range(cow_num)]
	power = [0 for _ in range(cow_num)]
	#makes it so the first number is the x pos, then the y pos then the power
	for c in range(cow_num):
		x[c], y[c], power[c] = [int(i) for i in read.readline().split()]

#Uses the distances and power of each walkie to 
connected = [[False for _ in range(cow_num)] for _ in range(cow_num)]
for i in range(cow_num):
	for j in range(cow_num):
		distance = (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2
		connected[i][j] = distance <= power[i] ** 2

#this function will determine how many cows can be reached with the original cow c
def reachable_cows(c: int) -> int:
	global visited 
	visited[c] = True
	reached = 1  # we can always reach the initial cow c
	for newCow in range(cow_num):
		#If loop will coubel check that we can actually reach the new cow if it hasn't already been reached
		if not visited[newCow] and connected[c][newCow]:
			visited[newCow] = True
			reached += reachable_cows(newCow)
	return reached

#Sets the max cows value and then uses the visited variable to determine the actual amount of reachable cows and updates the value
max_cows = 0
for c in range(cow_num):
	visited = [False for _ in range(cow_num)]
	max_cows = max(max_cows, reachable_cows(c))

print(max_cows, file=open("moocast.out", "w"))