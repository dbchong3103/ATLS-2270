
#Opens file and creates list with split
fileIn = open("diamond.in",'r')
diamond = fileIn.readline().split()
N,k = int(diamond[0]),int(diamond[1])

#turns strings into integers
diamonds = [int(fileIn.readline()) for i in range(N)]
large = 0

#Checks if the value of i index is a lesser or equal value to the h index!
for i in range(N):
  diamKept = 0
  for h in range(N):
    if diamonds[h] <= diamonds[i]+k:
      if diamonds[h] >= diamonds[i]:
        diamKept += 1
      
#Checks to find the largest diamonds kept
  if diamKept > large:
    large = diamKept
    
fileOut = open("diamond.out",'w')
fileOut.write(str(large))
fileOut.close()