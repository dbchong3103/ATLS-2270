# Year of the Cow (2021 February, bronze1)
# NuttyJamie's Solution
"""
1. create a list (zodiac) of all 12 animals
2. assume Bessie was born in year 0, and use a dictionary to store all cows' birth years
3. We extract all the essential information from the input
   (i.e. the 1st, 4th, 5th and the last word from each phrase)
4. Since year 0 is the year of Ox (as we have assumed), 
   then year 1 is the year of Tiger,
         ...
        year 11 is the year of Rat,
        year 12 is the year of Ox again.
    Also, year -1 is the year of Rat.
   More Generally, year i is the year of zodiac[i % 12]
5. we use while loops to find the birth year for each cow
6. the absolute value of Elsie's birth year is our final answer
"""
zodiac = ["Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig", "Rat"]
cows = {"Bessie": 0}
N = int(input())
for i in range(N):
    phrase = input().split()
    cow1, rel, animal, cow2 = [phrase[i] for i in [0, 3, 4, -1]]
    if rel == "previous":
        year = cows[cow2] - 1
        while zodiac[year % 12] != animal:
            year -= 1
    else:
        year = cows[cow2] + 1
        while zodiac[year % 12] != animal:
            year += 1
    cows[cow1] = year
print(abs(cows["Elsie"]))