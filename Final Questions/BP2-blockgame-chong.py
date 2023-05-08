'''
Name: Dahn Bi Chong
Problem: Block Game
Objective:
'''


import sys

sys.stdin = open("blocks.in", "r")
sys.stdout = open("blocks.out", "w")

def countfreq(s): #count frequency of each letter in a string
    freqs = [0]*26
    for c in s:
        freqs[ord(c)-ord('a')] += 1
    return freqs

n = int(input())

ans = [0]*26
for i in range(n):
    s1, s2 = input().split() #2 words on the same board
    freq1, freq2 = countfreq(s1), countfreq(s2) #letter count of each word
    for j in range(26):
        ans[j] += max(freq1[j], freq2[j]) #add the count of each letter from either of the words
        #after iterating through all boards, the sums of letter counts are the letter countrs in combinations

for i in ans:
    print(i)