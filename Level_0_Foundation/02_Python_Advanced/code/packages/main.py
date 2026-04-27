import random
from swg_game import check_win, CHOICES

def play():
    print("--- Welcome to Snake, Water, Gun Game ---")
    print("Choices: s for Snake, w for Water, g for Gun")
    
    user_choice = input("Enter your choice (s/w/g): ").lower()
    
    if user_choice not in CHOICES:
        print("Invalid choice! Please choose s, w, or g.")
        return

    computer_choice = random.choice(list(CHOICES.keys()))
    
    print(f"\nYou chose: {CHOICES[user_choice]}")
    print(f"Computer chose: {CHOICES[computer_choice]}")
    
    result = check_win(user_choice, computer_choice)
    
    if result == 0:
        print("It's a Draw!")
    elif result == 1:
        print("Congratulations! You Win!")
    else:
        print("Computer Wins! Better luck next time.")

if __name__ == "__main__":
    play()
