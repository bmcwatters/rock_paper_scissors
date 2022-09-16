import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

print("Ready to play Rock Paper Scissors?")
print()

while True:            
    user_input = input("Type: Rock/Paper/Scissors or Q to quit ").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        print("Type something valid!")
        continue

    random_number= random.randint(0,2)
    # 0 == rock  1 == paper  2== scissors

    computer_pick = options[random_number]
    print (f"Computer picked {computer_pick}. ")

    if user_input == "rock" and computer_pick == "scissors":
        print("You Won!")
        user_wins += 1
        continue
    elif user_input == "paper" and computer_pick == "rock":
        print("You Won!")
        user_wins +=1
        continue
    elif user_input == "scissors" and computer_pick == "paper":
        print("You Won!")
        user_wins += 1       
        continue
    else:
        print("You Lost!")
        computer_wins +=1
        continue

print(f"You won {user_wins} times and the computer won {computer_wins} times.")
print()        
if user_wins < computer_wins:
    print("You Suck!")

print("Goodbye!")


