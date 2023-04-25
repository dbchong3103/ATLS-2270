#this time errors on the last few cases; that's okay.
cows = []
with open("teamwork.in") as read:
    nk = map(int, read.readline().split())
    n, k = int(nk[0]),int(nk[1])
    cows = []
    for i in range(n):
        cows.append(int(read.readline()))

cows = []

#print(n, k)
#print(cows)

# we want to iterate through cows, and keep track of the best sum to that point
# then we use that information to determine optimal groupings

dp = [-1] * n
#print(dp)
dp[0] = cows[0]
#print(dp)

for i in range(n):
  #print(cows[i])
  #if we don't join the cow we're on to a team, then it's value remains cow[i]
  mx = cows[i]
  for j in range(i,-1,-1): # range(n) -> that goes from 0 to n-1; range(n, m) -> goes from n to m-1
    cr = i - j +1
    if cr > k:
      break
    mx = max(mx, cows[j])
    # if the cow to the left is "better", update max to that value AS LONG AS we are within k
    if j == 0:
      dp[i] = max(dp[i], mx*cr)
    else:
      dp[i] = max(dp[i], dp[j-1] + (mx*cr))

print(dp[n-1], file=open("teamwork.out","w"))
# i = 0; max = 1, for loop -> 0 max = 1
# i = 1; max = 15, for loop -> 1, 0; 1-1+1 = 1 > k, max =15; 0-1+1 = 0> k, 15> 1; max =15
# i= 5; max =2, for loop-> 5,4,3,2,1; cr-> 1, 2, 3, 4(break); ----- max = 9