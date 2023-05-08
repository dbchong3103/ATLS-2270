'''
Name: Dahn Bi Chong
Problem: Block Game
Objective: Farmer John is just so very weird and think that his cows need to develop reading skills! So he has a bunch of blocks that have letters on them. The goal of this code is to determine the miniumu amount of visible letters needed on his blocks so that the cows can make all of the words given. This will be done by counting what letters are in the words and how many of each letter there are.
'''

#We'll use sys to open and close our file, because the hecking open() hates me!
import sys

sys.stdin = open("blocks.in", "r")
sys.stdout = open("blocks.out", "w")

#This function here will count the amount of each letter that appears in the word to determine how many of what letter we need
def count(s):
    amt = [0]*26
    for c in s:
        amt[ord(c)-ord('a')] += 1
    return amt

#Set up the amount of boards as N and resets the answer to all zero
n = int(input())
ans = [0]*26

#Will go through the words to determine the letters of each word
for i in range(n):
    s1, s2 = input().split()
    amt1, amt2 = count(s1), count(s2) #uses the count fucntion we made earlier to count the amount of words
    for j in range(26): #This section essentially adds all the total letters
        ans[j] += max(amt1[j], amt2[j]) 

for i in ans:
    print(i)