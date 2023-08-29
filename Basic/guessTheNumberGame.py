#guess the number game
import random
#using random module getting random number
random_no=random.randint(1,5)
#getting user guessed number to match random number
guess_number=int(input("Enter your guess number from 1 to 5"))
#using this attempt variable calculating user input attempt
attempt=1
while random_no!=guess_number:
    if attempt<=2:
         if random_no>guess_number:
             print("Your guessed number is lower")
         else:
             print("Your guessed number is higher")
    else:
        break
    attempt+=1
    guess_number=int(input("Enter the number again to guess "))
if attempt>2:
     print("You loss the game")
else:
    print("You won the game")