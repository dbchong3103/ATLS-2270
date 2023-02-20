#open file, per usual
with open('cowqueue.in') as fin:
  n = fin.readline()
  #create my cow list of cows that need to enter through the farm
  cows = []
  for line in fin.readlines():
    #adds to the cow list
    cows.append(list(map(int, line.split())))

#Sorts the cow arrive and questioning time
cows = sorted(cows)

#Decides upon how long it will take for each cow to go through the questioning cycle to give minimum amount of time necessary
cur_time = 0
for x in range(len(cows)):
      if cows[x][0] > cur_time:
            cur_time = sum(cows[x])
      else:
            cur_time += cows[x][1]

#Creates output file and writes it down
print(cur_time, file=open('cowqueue.out', 'w'))