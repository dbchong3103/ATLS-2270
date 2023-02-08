import sys, math

#open input file and create output file
sys.stdin = open("square.in", "r")
sys.stdout = open("square.out", "w")

#determines the positions of the boxes
x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

#finds the longest lengths, one for the width, other for height
x = (min(x1,a1))
a = (max(x2,a2))
lengthOne = abs(x-a)

y = (min(y1,b1))
b = (max(y2,b2))
lengthTwo = abs(y-b)

#Gives teh area of teh swuare after determining the longest length
print(max(lengthOne, lengthTwo) ** 2)
