import random

CHOICES = {"s": "Snake", "w": "Water", "g": "Gun"}

def check_win(user, computer):
    """
    Returns:
    1 if user wins, -1 if computer wins, 0 if it's a draw
    """
    if user == computer:
        return 0
    
    # Win conditions for user
    # Snake (s) vs Water (w) -> Snake wins
    # Water (w) vs Gun (g) -> Water wins
    # Gun (g) vs Snake (s) -> Gun wins
    
    if (user == "s" and computer == "w") or (user == "w" and computer == "g") or (user == "g" and computer == "s"):
        return 1
    else:
        return -1
