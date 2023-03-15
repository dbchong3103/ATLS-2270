'''
Name: Dahn Bi Chong
Problem: Moocast
Description: In this problem, I will be looking to compare different cow walkie talkies to determine thenumber of cows
a single cow can broadcast do depending on the power of their walkie-talkie. This will be done by comparing each cow's
postion and power.
'''

#Opens file and creates a list for each line, designating them as different variables.
with open('moocast.in') as read:
	cow_num = int(read.readline())
	x = [0 for _ in range(cow_num)]
	y = [0 for _ in range(cow_num)]
	power = [0 for _ in range(cow_num)]
	for c in range(cow_num):
		x[c], y[c], power[c] = [int(i) for i in read.readline().split()]

print(cow_num)
print(x)
print(y)
print(power)


max_cows=0
print(max_cows, file=open('moocast.out', 'w'))