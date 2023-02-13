#Inputs the amount of flowers
n = int(input())

#Inputs flowers into an array
flowers = list(map(int,input().split()))

#Sets output value for now before increase in value
output = 0

#Essentially calcultes the flowers and determines and average flower before stoppping
for i in range(n):
    for j in range(i,n):
        avgPetals = sum(flowers[i:j+1]) / (j-i+1) #Finds average petals
        
        for value in range(i,j+1):
            if flowers[value]== avgPetals:
                output += 1 #adds if average flower has been found.
                break

#Prints output to the terminal!
print(output)