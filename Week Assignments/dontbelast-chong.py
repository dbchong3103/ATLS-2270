#Import sys mnostly becuase I couldn't figure this out without it (I am also still confused on how sys works but I'm working on it)
import sys

#Opens,reads and writes files
sys.stdin = open("notlast.in", "r")
sys.stdout = open("notlast.out", "w")

# with open('notlast.in') as read: --> Note: I need to figure out how to work with functions, because I am always confused using them
# 	raw = {}
# 	for _ in range(int(read.readline())):
# 		name, amt = read.readline().split()
# 		amt = int(amt)
# 		if name not in raw:
# 			raw[name] = 0
# 		raw[name] += amt

# cows = [(amt, name) for name, amt in raw.items()]

# taking input and uses split to create a list
n = int(input())
data = [input().split() for a in range(n)]

#Create directory of cow names and cow milk produciton staring at zero for data later
names = {'Annabelle':0, 'Bessie':0, 'Daisy':0, 'Elsie':0, 'Gertie':0, 'Henrietta':0, 'Maggie':0}
#Ints the cow procution numbers
for cows in data:
	names[cows[0]] += int(cows[1])

#Create a tie for if the cows all somehow magically produce the same amount of milk
if len(set(names.values())) == 1:
	print("tie")
 
#Determine the second least amount of milk produciton
else:
	minTwo = sorted(set(names.values()))[1]
	count = 0
    #If there is a different add to the count and change name printed
	for key, value in names.items():
		if value == minTwo:
			ans = key
			count += 1
		#Again, if multiple cows magically produce the same amount, determine a tie
		if count > 1:
			ans = "tie"
			break
	print(ans)