# Beetle_Lab_2


# Environment
import random


# Data Base
# Initialize an empty dictionary to store player scores
player_scores = {}


# Functions
def roll_dice():
    return random.randint(1,6)

# Converting number to names
def name(number_x):
    if number_x == 6:
        return "Body"
    elif number_x == 5:
        return "Head"
    elif number_x == 4:
        return "Tail"
    elif number_x == 3:
        return "Leg"
    elif number_x == 2:
        return "Antenna"
    elif number_x == 1:
        return "Eye"
    else:
        return "Not vaild"
        # For now

# Database check
def db_auth(player_x):
    if player_x in player_scores:
        # pass
        print(player_scores[player_x])
        print(f"{player_x}: Key exists, no update")
        return True
    else:
        player_scores[player_x] = [0,0,0,0,0,0]
        print(f"{player_x}: Key not exists, a new key has been created")
        print("Rerun db_auth")
        db_auth(player_x)

# Function for checking index
def index_auth(player_x,index_x):
    index_x = index_x - 1
    return player_scores[player_x][index_x] # Index start from 0, 5 is the sixth index
        # Unfinished
        # Need add more logic

def validate(player_y,dice_x):
    if dice_x == 6:
        if index_auth(player_y,dice_x) == 0:
            print(f"{dice_x}/{name(dice_x)} is 0") # Unfinished
            player_scores[player_y][dice_x - 1] = player_scores[player_y][dice_x - 1] + 1
            print(f"{dice_x}/{name(dice_x)} is vaild, ")
        else:
            pass # Unfinished
        return 6
    elif dice_x == 5:
        if index_auth(player_y,6) == 1:
            print(f"{dice_x}/{name(dice_x)} is 1") # Unfinished
            if index_auth(player_y,dice_x) == 0:
                player_scores[player_y][dice_x - 1] = player_scores[player_y][dice_x - 1] + 1
            else:
                pass # Unfinished
        else:
            pass
        return 5
    elif dice_x == 4:
        if index_auth(player_y,6) == 1:
            if index_auth(player_y,dice_x) == 0:
                player_scores[player_y][dice_x - 1] = player_scores[player_y][dice_x - 1] + 1
            else:
                pass # Unfinished
        else:
            pass
        return 4
    elif dice_x == 3:
        if index_auth(player_y,6) == 1:
            if index_auth(player_y,dice_x) <= 4:
                player_scores[player_y][dice_x - 1] = player_scores[player_y][dice_x - 1] + 1
            else:
                pass # Unfinished
        else:
            pass
        return 3
    elif dice_x == 2:
        if index_auth(player_y,5) == 1:
            if index_auth(player_y,dice_x) <= 2:
                player_scores[player_y][dice_x - 1] = player_scores[player_y][dice_x - 1] + 1
            else:
                pass # Unfinished
        else:
            pass
        return 2
    elif dice_x == 1:
        if index_auth(player_y,5) == 1:
            if index_auth(player_y,dice_x) <= 2:
                player_scores[player_y][dice_x - 1] = player_scores[player_y][dice_x - 1] + 1
            else:
                pass # Unfinished
        else:
            pass
        return 1
    else:
        print("Unvaild") # For now

# Check for win, run after each db change
def win_auth(player_z):
    if player_scores[player_z] == [2,2,4,1,1,1]:
        print(f"{player_z} has win")
        return True
    else:
        return False
    

# Logic
print("Beetle Lab")
player_win = False # Default no one win yet

# Ask for the number of players
# while True:
    # num_players = int(input("Enter the number of player: "))
    # break

# Player number input
while True: # Use loop to input until value is integer
    try: # Error management, increase robustness
        num_players = int(input("Enter the number of players: "))
        break  # Exit the loop if the input is valid
    # except:
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Loop to get each player's name and initialize their score list
for i in range(num_players):
    player_name = input(f"Enter the name for Player {i + 1}: ")
    player_scores[player_name] = [0,0,0,0,0,0] # Add player to the dictionary with an empty list for storing scores

# Output the initialized dictionary
print("\nPlayer score tracking initialized:")
print(player_scores)

while not player_win:
    for player_now in player_scores.keys():
        print(f"----Current Player: {player_now}----")
    
        input("Press Enter to roll the dice...")  # Wait for the player to press Enter
        rand_dice = roll_dice()

        print(f"Dice result: {rand_dice}/{name(rand_dice)}")

        db_auth(player_now)

        validate(player_now,rand_dice)

        
        
        pass # Unfinished

# Finction could not input 2 value/information //Fixed
# Explain to play the logic e.g. No change because of condition not meet
