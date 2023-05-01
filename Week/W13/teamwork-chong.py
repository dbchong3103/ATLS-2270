'''
Name: Dahn Bi Chong
Problem: Teamwork
Objective: Farmer John is stupid apparently and cant wrap presents and somehow thinks that hooves are better than hands. So he needs good teams. This really just determines how smart his dumb teams of heckin cows to make janky presents. Note: Some of these comments might just be the ones Anthony made in class for my clarity.
'''
#Opens file and sets up the n and k and cows
with open("teamwork.in") as read:
    n, k = map(int, read.readline().split())
    cows = []
    for i in range(n):
        cows.append(int(read.readline()))


dp = [-1] * n
dp[0] = cows[0]

#Iterates itself through the cows
for i in range(n):
  mx = cows[i]
  for j in range(i,-1,-1): # range(n) -> that goes from 0 to n-1; range(n, m) -> goes from n to m-1
    cr = i - j +1
    if cr > k:
      break
    mx = max(mx, cows[j])
    #Finds out which cow has the best hoof dexterity I guess and then makes all the cows have noice ghoof dexterity
    if j == 0:
      dp[i] = max(dp[i], mx*cr)
    else:
      dp[i] = max(dp[i], dp[j-1] + (mx*cr))

#Prints the output! Yay!
print(dp[n-1], file=open("teamwork.out","w"))