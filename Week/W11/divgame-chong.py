'''
Name: Dahn Bi Chong
Problem: Div Game
Objective: The goal is to determine how many times an operation can be done before the number gets too small or it becomes impossible to continue doing the operation.

Note: This code is identical to the one we did in class, but for some reason it won't return the correct values and I do not know what is wrong. At least, it wouldn't retrun the right numbers for me on my computer.
'''
#This function will actually do the operation.
def answer(n):
    ans = 0
    
    for p in range(2,int(n**2)):
        e = 0 #anything to the power of zero will be one
        while n % p == 0:
            n /= p
            e += 1
        i = 1             
        while e >= i:
            e -= i
            ans += 1
            i += 1
    #Allows for very large numbers
    ans += n > 1 
    return(n)

print(answer(24))
print(answer(1))
print(answer(64))
print(answer(1000000007))
print(answer(997764507000))