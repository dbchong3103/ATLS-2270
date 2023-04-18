'''
Name: Dahn Bi Chong
Problem: The Bovine Shuffle
Objective: Farmer John, who I am increasingly convined is a pyschopath, is teaching his cows how to dance. Because apparently 100s of dancing cows in not absolutely terrifying. However, because I am an accomplice to his actions, this code should help him figure out what spots are always taken as he teaches the cows the bovine shuffle.
'''

#must import deque to well... deque the cows
from collections import deque

#opens file!
with open("shuffle.in", "r") as input_file:
	n = int(input_file.readline())

	cows_after_shuffle = [0] * n
	a = list(map(int, input_file.readline().split()))

#Essentially set up shuffle, and cow count
for i in range(n):
    #a is the shuffle
    a[i] -= 1
    cows_after_shuffle[a[i]] += 1

#n indicates spaces with no cows
ans = n
#for the areas with no cows we can start using deque to add and remove!
no_cows = deque()

#find no_cow positions after one shuffle
for i in range(n):
    if cows_after_shuffle[i] == 0:
        no_cows.append(i)
        ans -= 1

#This while statement actually counts the cows and the no cow positions to determine where cows will always be
while no_cows:
    curr = no_cows.popleft()
    
    cows_after_shuffle[a[curr]] -= 1
    
    if cows_after_shuffle[a[curr]] == 0:
        no_cows.append(a[curr])
        ans -= 1
        
# print(ans)
print(ans, file=open("shuffle.out", "w"))