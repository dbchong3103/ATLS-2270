# Teleportation - Dahn Bi Chong

import math

#reading files
file = open('teleport.in')
data = file.read().split(" ")

print(data)

#all variables
a = int(data[0])
b = int(data[1])
y = int(data[2])
x = int(data[3])

regularD = abs(a-b)
teleportD = abs(a-x) + abs(b-y)

ideal = min(regularD, teleportD)

fileOut = open("teleport.out",'w')
fileOut.write(str(ideal))
fileOut.close()
