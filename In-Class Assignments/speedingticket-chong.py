import sys

#open files and write output file
sys.stdin = open("speeding.in","r")
sys.stdout = open("speeding.out", "w")

#turn strings from input into integers, input
N, M = map(int, input().split())

#create blank lists for the speed limit and the speeding crazy cow
spdLimit= []
bessieSpeed= []

#make list for the road speed limits, N is road segments
for i in range(N):
	length, limit = map(int, input().split())
	spdLimit.extend([limit] * length)
    #just learned, .extend appends to a list!
 
#makes a list for bessie's unusual speeding habits(what a cow), M is Bessie speeding segments
for i in range(M):
	length, speed = map(int, input().split())
	bessieSpeed.extend([speed] * length)

#sets 0 and then finds the difference between bessie and the limit, range is 100 because the road lenght is set to 100
ans = 0
for i in range(100):
	dif = bessieSpeed[i] - spdLimit[i]
	ans = max(dif, ans)
 
#prints higher value between the difference and 0
print(ans)