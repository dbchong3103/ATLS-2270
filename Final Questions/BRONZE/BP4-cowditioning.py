'''
Name: Dahn Bi Chong
Problem: Air Cowditioning II
Obecjtive: Farmer John's cows are hot because summer sucks. The solution? AIR CONDITIONING! However, we live in a capitalist society and so everything costs unholy amounts of money! This code will help Farmer John determine how not to go broke while trying to keep all of his beef cool and comfy. (I wrote this while very tired, if I sound insane it's cause I am).
'''

#Because the terminal is used to input data there is no open file or sys

#Set up the number of cows versus the amount of air conditioning
numCows, numAC = input().split()
numCows, numAC = int(numCows), int(numAC)
cool = [0 for i in range(100)]

#This determines the temperature rewuirements of each cow and correlates that to required AC
for i in range(numCows):
    tempCow = input().split()
    for r in range(int(tempCow[0])-1, int(tempCow[1])):
        cool[r] = int(tempCow[2])
ac = [[int(i) for i in input().split()] for r in range(numAC)]
bestCase = 1000000000

for i in range(1 << numAC):
    temp = cool[:]
    moneyCounter = 0
    for r in range(numAC):
        if (1 << r) & i:
            for s in range(ac[r][0] - 1, ac[r][1]):
                temp[s] -= ac[r][2]
            moneyCounter += ac[r][3]
    if max(temp) <= 0:
        bestCase = min(bestCase, moneyCounter)

print(bestCase)