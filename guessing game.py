# This is a guessing game where the user is given three attempts to correctly guess the the right number. After the third attempts, the user failed. 

import random

guesssCount = 1
guessLimit = 3
secretNumber = random.randint(0,10)

while guesssCount <= guessLimit:
    name = int(input("Guess: "))
    if name is not secretNumber:
        print("Try Again")
    guesssCount += 1
    if name == secretNumber:
        print(f"Secret number is {secretNumber}")
        print("You won !!")
        break
else:
    print("Sorry, You failed !!")  
    print(f"The SECRET NUMBER was {secretNumber}")
    

