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
def name(def_number):
    if def_number == 6:
        return "Body"
    elif def_number == 5:
        return "Head"
    elif def_number == 4:
        return "Tail"
    elif def_number == 3:
        return "Leg"
    elif def_number == 2:
        return "Antenna"
    elif def_number == 1:
        return "Eye"
    else:
        return "Not vaild"
        # For now

def db_auth(player_x):
    if player_x in player_scores:
        # pass
        print("Key exists, no update")
        return True
    else:
        player_scores[player_x] = [0,0,0,0,0,0]
        print("Key not exists, a new key has been created")
        db_auth(player_x)

def validate(player_x,def_dice): # Non-functional, just pass through value for now
    if def_dice == 6:
        if index_auth(player_x,def_dice) == 0:
            player_scores[player_x][def_dice - 1] = player_scores[player_x][def_dice - 1] + 1
            print(f"{def_dice}/{name(def_dice)} is vaild, ")
        else:
            pass # Unfinished
        return 6
    elif def_dice == 5:
        if index_auth(player_x,6) == 1:
            if index_auth(player_x,def_dice) == 0:
                player_scores[player_x][def_dice - 1] = player_scores[player_x][def_dice - 1] + 1
            else:
                pass # Unfinished
        else:
            pass
        return 5
    elif def_dice == 4:
        if index_auth(player_x,6) == 1:
            if index_auth(player_x,def_dice) == 0:
                player_scores[player_x][def_dice - 1] = player_scores[player_x][def_dice - 1] + 1
            else:
                pass # Unfinished
        else:
            pass
        return 4
    elif def_dice == 3:
        if index_auth(player_x,6) == 1:
            if index_auth(player_x,def_dice) <= 4:
                player_scores[player_x][def_dice - 1] = player_scores[player_x][def_dice - 1] + 1
            else:
                pass # Unfinished
        else:
            pass
        return 3
    elif def_dice == 2:
        if index_auth(player_x,5) == 1:
            if index_auth(player_x,def_dice) <= 2:
                player_scores[player_x][def_dice - 1] = player_scores[player_x][def_dice - 1] + 1
            else:
                pass # Unfinished
        else:
            pass
        return 2
    elif def_dice == 1:
        if index_auth(player_x,5) == 1:
            if index_auth(player_x,def_dice) <= 2:
                player_scores[player_x][def_dice - 1] = player_scores[player_x][def_dice - 1] + 1
            else:
                pass # Unfinished
        else:
            pass
        return 1

def index_auth(player_x,index_x):
    index_x = index_x - 1
    return player_scores[player_x][index_x] # Index start from 0, 5 is the sixth index
        # Unfinished

def win_auth(player_y):
    if player_scores[player_y] == [2,2,4,1,1,1]:
        print(f"{player_y} has win")
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
        print(f"Current Player: {player_now}")
    
        input("Press Enter to roll the dice...")  # Wait for the player to press Enter
        rand_dice = roll_dice()

        print(f"dice result: {rand_dice}/{name(rand_dice)}")

        db_auth(player_now)

        validate(player_now,rand_dice)

        
        
        pass # Unfinished

# Finction could not input 2 value/information