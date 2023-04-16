'''
Name: Dahn Bi Chong
Problem: Exponentation II
Objective: Determine a to the b to the c and then mod with the crazy number to determine remainder of divison, I think.
'''
#I had to look up what the heck modulo was, and I still don't really get it other than the fact that it seems to be a math thingy to determine remainders
MOD = 10 ** 9 + 7

#This does the whole a to the b to the c power equation and then modulos
def solution():
    for _ in range(int(input())):
        a, b, c = map(int, input().split()) #splits the three necessary integers
        print(pow(a, pow(b, c, MOD - 1), MOD))

#just needed a way to actually use function
if __name__ == "__main__":
    solution()