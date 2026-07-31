# Build a num guessing game - computer picks a random num user keep guessing it unitl its correct 
'''import random 
com = random.randint(1,100)
count = 0 

while True  :
    count = count + 1
    a = int(input("Guess number between 1-100 : "))
    if a > 100 and a < 0 :
        print("Please guess number betweem 1-100")
    if a > com :
        print("Guess smaller number.... ")
    elif a < com :
        print("Guess bigger number...")
    else: 
        print("You guessed the number.")
        break 
if a == com :
    print(f"Congratulation!!! You won the game , you guessed the num {a} in {count} attempt..")'''

#Build rock paper scissors game
import random
option = ["rock", "paper", "scissor"]
com_choice = random.choices(option)




print("=== Rock Paper Scissor Game with Computer===")
user_choice = input("Choose rock, paper or scissor : ")

if com_choice == user_choice:
    print("It's a tie.")
elif (com_choice == "rock" and user_choice == "paper") or \
    (com_choice == "paper" and user_choice == "scissor")or \
    (com_choice == "scissor" and user_choice == "rock") :
    print(" Congratulations!!! You won the game")
else :
    print("Sorry.. you lose!!!!")
print(f"Computer choice : {com_choice}")
print("Thankyou for playing the game.....")