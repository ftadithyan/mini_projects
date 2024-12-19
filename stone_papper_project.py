import random

def stone_paper_scissors():
    print("🎉 Welcome to the Ultimate Stone, Paper, Scissors Showdown! 🎮")
    print("TYPE:'STONE', 'PAPER', or 'SCISSOR' to play.")
    print("TYPE 'EXIT' to quit the game.\n")

    options = ["stone", "paper", "scissors"]
    user_score = 0
    computer_score = 0

    while True:
        user_choice = input("YOUR CHOISE: ").strip().lower()

        # Exit condition
        if user_choice == "exit":
            print(f"\nGame Over! FINAL SCORE - You: {user_score}, Computer: {computer_score}")
            break

        # Validate user input
        if user_choice not in options:
            print("Invalid choice! Please choose 'stone', 'paper', or 'scissors'.")
            continue

        # Computer's random choice
        computer_choice = random.choice(options)
        
        print(f"Computer chose: {computer_choice}")

        # Determine the winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "stone" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "stone") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win this round! 🎉")
            user_score += 1
        else:
            print("Computer wins this round! 😢")
            computer_score += 1

        # Display current score
        print(f"Score - You: {user_score}, Computer: {computer_score}\n")

# Run the game
stone_paper_scissors()