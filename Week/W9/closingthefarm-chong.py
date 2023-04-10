'''
Name: Dahn Bi Chong
Problem: Closing the Farm
Objective: Farmer John is closing his farm and this code will determine whether the entire farm is connected after certain barns close down.
This code should (I really hope it does, I referred to the internal soltuion on the USACO guide for things that I couldn't figure out and now the code is unintentionally basically
identical and if it doesn't work I'm seriously an idiot) use the connections between different farms and the order of closing barns to determine the overall connection of the farm.
'''
#My new best friend, import sys to read and open files. Also, the start I/O didn't have an output and I couldn't get it to work, so I just used sys like the usaco guide.
import sys

sys.stdin = open("closing.in", "r")
sys.stdout = open("closing.out", "w")

#Setting the n and m values as barn and path
barn, path = map(int, input().split())

#determines adjacency of barns
nextTo, order = {}, []
for i in range(1, barn + 1):
	nextTo[i] = []

#record the barns that have been visited and those that have been closed
visited, closed = [False] * (barn + 1), [False] * (barn + 1)
nodes = 0

#DFS stands for Depth First search, not deep first search... I keep getting it wrong
def dfs(node):
	global nodes
	if visited[node] or closed[node]:
		return

	#Tells one to visit this node if it isn't closed and it has been visited either.
	nodes += 1
	visited[node] = True
	
	#Will run anotehr dfs if the barn has not been visited
	for u in nextTo[node]:
		if not visited[u]:
			dfs(u)


#Read the barns that are next to or adjacent to each other by noting paths
for i in range(path):
	a, b = map(int, input().split())
	nextTo[a].append(b)
	nextTo[b].append(a)

#note teh order of closing barns
for i in range(barn):
	order.append(int(input()))

dfs(1)


#This will say that the farm is connected and open if we have visited every "node" aka barn without any of them closing
print("YES") if nodes == barn else print("NO")

#Overall this for loop will determine whether not not we have gone to every barn before any paths have beocme unviable
for i in range(barn - 1):
	visited = [False] * (barn + 1)
	nodes = 0
	closed[order[i]] = True

	#Start from the last closing barn
	dfs(order[barn - 1])

	#Finally check if we have gone to every barn
	if nodes == barn - i - 1:
		print("YES")
	else:
		print("NO")