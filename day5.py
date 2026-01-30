#Guess Game

import random

jackpot = random.randint(1,100)
guess = int(input("Enter the number you guess: "))
count = 1

while guess != jackpot:
    if guess < jackpot:
        print("guess higher")
    else:
        print("guess lower")
    guess = int(input("enter the number you guess: "))
    count+=1
print("you guessed right! yay")
print("You took ", count, "attempts")