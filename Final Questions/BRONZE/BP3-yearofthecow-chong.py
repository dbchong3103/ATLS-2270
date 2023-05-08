'''
Name: Dahn Bi Chong
Problem: Year of the Cow
Objective: For some reason, the cows are into the Chinese Zodiac and this that somehow using those is the best way to determine their age differences. Therefore, they all compare their zodiacs to determine how far apart in age they are from one cow-- Bessie. This code should assign numbers to the zodiacs and be able to compute the differences in age using those numbers. It will also cut up the sentences given to get the crucial information about each cow in comparison to other cows
'''

#Creates a list for the zodiac animals that go from 0 to 11 with the year of the Ox(cow) as zero as it's Bessie's animal 
zodiac = ["Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig", "Rat"]

#Set up Bessie as 0
cows = {"Bessie": 0}

#Thisw determines the amount of cows we are comparing
N = int(input())

#This loop will now iterate through the cows to determine the 
for i in range(N):
    data = input().split()
    
    #Sets up the first, fouth, fifth and last word of the statement as data!
    cow1, rel, animal, cow2 = [data[i] for i in [0, 3, 4, -1]]
    
    #Sets up the difference between each cow based on fourth word!
    if rel == "previous":
        year = cows[cow2] - 1
        while zodiac[year % 12] != animal: #Welcome back the darn Modulo! The weird remainders! 
            year -= 1
    else:
        year = cows[cow2] + 1
        while zodiac[year % 12] != animal:
            year += 1
    cows[cow1] = year
    
#Will only print Elsie's age as that is the main question, though it is possible to determine the age differences of the other cows
print(abs(cows["Elsie"]))