import sys

#open files
sys.stdin = open("div7.in")
sys.stdout = open("div7.out", "w")

#set a sums list for the prefixes
sums = [0]
n = 0

#takes input
length = int(input())
for _ in range(length):
    sums.append((int(input())+sums[-1])%7)

#Finds the first and last numbers for the sums list and uses them to determine amount of cows
for i in range(7):
    try:
        first = sums.index(i)
        last = length-sums[::-1].index(i)
        if last-first > n:
            n = last-first
    except ValueError:
        pass

#records amount of cows
print(n)