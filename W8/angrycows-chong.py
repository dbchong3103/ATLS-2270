'''
Name: Dahn Bi Chong
Problem: Angry Cows
Objective: This code should be able to determine how to win Bessie's totally original angry cows games. The code will be able to determine
the radius of detonation for the cows to be able to explode every hay bale on the scene.
'''

#Opens file with sys, I've learned I think I like sys more to open things because I for the love of God could not get the starter code to work...
import sys

sys.stdin = open("angry.in")
sys.stdout = open("angry.out", "w")

#Creates a function to determine the cows required to explode all the bales using poisitons (left and right) of the bales.
def countCows(left, r):
    global count
    right = left + r * 2
    count += 1
    x = [b for b in bales if b > right]
    if len(x) == 0:
        return
    countCows(x[0], r)

#Sets up the intergers for N and K using split, also sets up the ints for the haybales and sets up a low and high range
N, K = map(int, input().split())
bales = sorted(int(input()) for _ in range(N))
low, hi = 1, 1000000000

#Uses a while function to compare low and high and add to the low value, which is essentially the minimum power required to explode all the bales.
while low < hi:
    mid = (low + hi) // 2
    count = 0
    countCows(bales[0], mid)
    if count <= K:
        hi = mid
    else:
        low = mid + 1
print(low)