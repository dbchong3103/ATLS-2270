'''
Name: Dahn Bi Chong
Question: High Card Wins
Objective: This code is meant to determine how many points Bessie can achieve based on Elsie's cards. This will use a loop to determine what Bessie's cards are and will compare them
to Elsie's Cards to determine how many points Bessie can win.
'''

fin = open('highcard.in')
n = int(fin.readline())
elsie_has = set()
for i in range(n): 
    elsie_has.add(int(fin.readline()))

#print(elsie_has)

elsie, bessie = [],[]

for i in range(1, n*2+1):
  #print(i)
  if i not in elsie_has:
    bessie.append(i)
  else:
    elsie.append(i)
  #print(bessie)
  #print(elsie)

ans = 0
bessie_index, elsie_index = 0, 0

while (bessie_index < n) and (elsie_index < n):
  if bessie[bessie_index] > elsie[elsie_index]:
    ans += 1
    bessie_index += 1
    elsie_index += 1
  else:
    bessie_index += 1
  
#print(ans)

with open('highcard.out', 'w') as f:
    f.write(str(ans) + '\n')