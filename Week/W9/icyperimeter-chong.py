'''
Name: Dahn Bi Chong
Problem: Icy Perimeter
Objective: This code should determine the minimal perimeter for maximum area of ice cream blobs in Farmer Johns wonky ice cream business. 
'''
from collections import deque 
#deque = doulbly ended queue! (add to front, remove to front, add to back and remove from back)

#Opens file and reads out 
with open("perimeter.in") as r:
	t = r.readline
	n = int(t())
	ice = []
	visited = [[False] * n for _ in range(n)]

	for _ in range(n):
		ice.append(list(t()))

#Sets the maxiumum area to 0 so that is can be added upon later!
max_area = 0
min_peri = float("inf")

#Sets up possible directions
DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

#Checks if the ice cream grid blob is possible aka not out of bounds
def out(a, b, l):
	if a < 0 or b < 0 or a >= l or b >= l:
		return True
	return False

#
def area_and_perimeter(x, y):
	area, peri = 1, 0

	q = deque()
	q.append((x, y))
	visited[x][y] = True

	while q:
		x, y = q.pop()

		for dx, dy in DIRECTIONS:
			nx, ny = x + dx, y + dy
			if out(nx, ny, n) or ice[nx][ny] == ".":
				peri += 1
			else:
				# check if already visited
				if not visited[nx][ny]:
					area += 1
					q.appendleft((nx, ny))
					visited[nx][ny] = True
	return area, peri

#for items equal or otherwise, compares values to determine minimal
for i in range(n):
	for j in range(n):
		if ice[i][j] == "#" and not visited[i][j]:
			area, peri = area_and_perimeter(i, j)

			if area > max_area:
				max_area, min_peri = area, peri
			elif area == max_area:
				if min_peri > peri:
					max_area, min_peri = area, peri

print(max_area, min_peri, file=open("perimeter.out", "w"))