import random
import time

def play_space_dodger():
    print("========================================")
    print("   WELCOME TO SPACE DODGER MINI-GAME    ")
    print("========================================")
    print("Instructions: Avoid incoming space debris!")
    print("Type 'left' (<) or 'right' (>) to dodge.\n")
    
    score = 0
    game_running = True
    
    while game_running:
        # Generate random obstacle position: 0 for left, 1 for middle, 2 for right
        obstacle_pos = random.randint(0, 2)
        lanes = ["   [X]      ", "      [X]   ", "         [X]"]
        
        print(f"Incoming debris: {lanes[obstacle_pos]}")
        move = input("Dodge (left/right/exit): ").strip().lower()
        
        if move == 'exit':
            print(f"\nGame Over! Final Score: {score}")
            break
            
        # Simple logic mapping user choice to lane numbers
        user_pos = 0
        if move == 'right':
            user_pos = 2
        elif move == 'left':
            user_pos = 0
        else:
            user_pos = 1 # middle default
            
        if user_pos == obstacle_pos:
            print("\n💥 CRASH! You hit the space debris.")
            print(f"Final Score: {score}")
            game_running = False
        else:
            score += 1
            print(f"✨ Dodged successfully! Current Score: {score}\n")
            
if __name__ == "__main__":
    play_space_dodger()
