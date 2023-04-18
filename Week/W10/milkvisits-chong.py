'''
Name: Dahn Bi Chong
Problem: Milk Visits
Objective:  Apparently farmers have absolutely cracked tastebuds and can taste the difference in different types of milk. Farmer John now needs to determine whether he will have satisfied, super taste bud farmer friends. This code will determine whether or whether not each farmer friend is satisfied with their milk visit by checking where these N farms are and if M farmers get their desired milk type and outputting that into simple 1s and 0s, aka binary. 
'''

#This opens the file abd sets up two empty lists
with open("milkvisits.in") as read:
	farmNum, qNum= [int(i) for i in read.readline().split()]
	farms = read.readline()
	neighbors = [[] for _ in range(farmNum)]
	for f in range(farmNum - 1):
		f1, f2 = [int(i) - 1 for i in read.readline().split()]
		neighbors[f1].append(f2)
		neighbors[f2].append(f1)

	queries = []
	for _ in range(qNum):
		query = read.readline().split()
		query[0], query[1] = int(query[0]) - 1, int(query[1]) - 1
		queries.append(query)

#Essentialy "creates" the tree and takes note of each component of the tree (farms and roads)
component_num = 0
component = [-1 for _ in range(farmNum)]


#This for loop will process what farms have been visited for not and use that information to number each farm
for f in range(farmNum):
    #Checks for vivist
	if component[f] != -1:
		continue
	frontier = [f]
	curr_type = farms[f]
	while frontier:
		curr = frontier.pop()
		#Assign numbers
		component[curr] = component_num
		for n in neighbors[curr]:
		#Visit new neighbor!
			if farms[n] == curr_type and component[n] == -1:
				frontier.append(n)
	component_num += 1

#Opens file again, but this time check for milk and writes out the binary!
with open("milkvisits.out", "w") as written:
	for a, b, milk in queries:
     #Checks for milk compatibility!
		if component[a] == component[b]:
			print(1 if farms[a] == milk else 0, end="", file=written)
		else:
			# Output 1 otherwise because both milk types will be visited
			print(1, end="", file=written)
	print(file=written)