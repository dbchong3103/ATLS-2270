from typing import NamedTuple

MAX_STALL = 100


class Cow(NamedTuple):
	start: int
	end: int
	cool_req: int


class AC(NamedTuple):
	start: int
	end: int
	cool_amt: int
	cost: int


cow_num, ac_num = [int(i) for i in input().split()]
cows = [Cow(*[int(i) for i in input().split()]) for _ in range(cow_num)]
acs = [AC(*[int(i) for i in input().split()]) for _ in range(ac_num)]

min_cost = float("inf")
for mask in range(1 << ac_num):
	stalls = [0 for _ in range(MAX_STALL + 1)]

	cost = 0
	for v, a in enumerate(acs):
		if mask & (1 << v):
			for i in range(a.start, a.end + 1):
				stalls[i] += a.cool_amt
			cost += a.cost

	valid = True
	for c in cows:
		for i in range(c.start, c.end + 1):
			if stalls[i] < c.cool_req:
				valid = False
				break
		if not valid:
			break
	else:
		min_cost = min(min_cost, cost)

print(min_cost)