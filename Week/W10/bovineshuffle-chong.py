'''
Name: Dahn Bi Chong
Problem: The Bovine Shuffle
Objective: 
'''
from collections import deque

with open("shuffle.in", "r") as input_file:
	n = int(input_file.readline())

	cows_after_shuffle = [0] * n
	a = list(map(int, input_file.readline().split()))

for i in range(n):
    #a is the shuffle
    a[i] -= 1
    # print(a)
    cows_after_shuffle[a[i]] += 1
    # print(cows_after_shuffle)
    # print("============")
    
# print(cows_after_shuffle)
ans = n
no_cows = deque()

#find no_cow positions after one shuffle
for i in range(n):
    if cows_after_shuffle[i] == 0:
        no_cows.append(i)
        ans -= 1
    # print(no_cows)
    # print(ans)
    
while no_cows:
    curr = no_cows.popleft()
    
    cows_after_shuffle[a[curr]] -= 1
    # print(cows_after_shuffle)
    
    if cows_after_shuffle[a[curr]] == 0:
        no_cows.append(a[curr])
        ans -= 1
        
# print(ans)
print(ans, file=open("shuffle.out", "w"))