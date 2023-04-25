'''
Name: Dahn Bi Chong
Problem: Haybales
Objective: Determine min spice and max flavor because these cows are weird. (SOrry for bad commenting I spend too long trying to open the hecking file)
'''

#open file
with open('hayfeast.in') as fin:
    num = fin.readline().split()
    n,m = int(num[0]),int(num[1])
    bales = []
    for line in fin.readlines():
    #add bales
        bales.append(list(map(int, line.split())))

#set variables
left = 0
right = 0
spicyArray = []

#loop proceeds to determine sum of flavorsand the spicy levels
while left < n and right < n:
  flavor = 0 
  for i in range(left, right+1):
    flavor = flavor + bales[i][0]
    #print(flavor)
  if flavor < m:
    right += 1
  else:
    maxSpicy = 0
    window = right - left
    tempSpicy = []
    for i in range(left, right+1):
      tempSpicy.append(bales[i][1])
    #  windowMax = max([nums[i], nums[i+1], nums[i+2]])
    #  ans.append(windowMax)
    maxSpicy = max(tempSpicy)
    spicyArray.append(maxSpicy)
    left +=1

print(min(spicyArray), file=open('hayfeast.out', 'w'))