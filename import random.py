import random

print("Welcome to Rock-Paper-Scissors!")
print("Type rock, paper, or scissors to play. Type quit to exit the game.\n")

options = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0

while True:
    player_choice = input("Your choice: ").lower()

    if player_choice == "quit":
        print(f"\nFinal Score -> You: {player_score}, Computer: {computer_score}")
        print("Thanks for playing!")
        break

    if player_choice not in options:
        print("Invalid choice. Try again!")
        continue

    computer_choice = random.choice(options)
    print(f"Computer chose: {computer_choice}")

    if player_choice == computer_choice:
        print("It's a tie!\n")
    elif (
        (player_choice == "rock" and computer_choice == "scissors") or
        (player_choice == "paper" and computer_choice == "rock") or
        (player_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win this round!\n")
        player_score += 1
    else:
        print("Computer wins this round!\n")
        computer_score += 1
