import math

fileIn = open('promote.in', 'r')

#create ints for  each rank
bronzeIn, bronzeOut = map(int, fileIn.readline().split())
silverIn, silverOut = map(int, fileIn.readline().split())
goldIn, goldOut = map(int, fileIn.readline().split())
platIN, platOut = map(int, fileIn.readline().split())

#set each rank
silver = 0
gold = 0
plat = 0

fileIn.close()

#operations to determine movement between ranks
plat = platOut - platIN
gold = (platOut + goldOut) - (platIN + goldIn)
silver = (platOut + goldOut + silverOut) - (platIN + goldIn + silverIn)

#determine answer
ans = str(silver) + '\n' +str(gold) + '\n' +str (plat)\

#write into output file
fileOut = open('promote.out', 'w')
fileOut.write(ans)
fileOut.close()