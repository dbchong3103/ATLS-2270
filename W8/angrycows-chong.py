# Angry Cows
import sys

sys.stdin = open("angry.in")
sys.stdout = open("angry.out", "w")


def count_cows_needed(leftpos, r):
    global cnt
    rightpos = leftpos + r * 2
    cnt += 1
    unaffected = [b for b in bales if b > rightpos]
    if len(unaffected) == 0:
        return
    count_cows_needed(unaffected[0], r)


N, K = map(int, input().split())
bales = sorted(int(input()) for _ in range(N))
lo, hi = 1, 1000000000
while lo < hi:
    mid = (lo + hi) // 2
    cnt = 0
    count_cows_needed(bales[0], mid)
    if cnt <= K:
        hi = mid
    else:
        lo = mid + 1
print(lo)