# Beetle Lab 2


# Environment
import random


# Data Base
# Initialize an empty dictionary to store player scores
player_scores = {}


# Functions

# Function to check if the player name already exists
def check_duplicate_name(player_name, player_scores):
    if player_name in player_scores:
        print(f"Player name '{player_name}' already exists. Please choose a different name.")
        return True
    else:
        return False

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
        print(f"\nPlayer {player_x} db_auth")
        print(f"Pre-updated scores for {player_x}:")
        print(player_scores[player_x])
        print(f"Key exists, no database update")
        return True
    else:
        player_scores[player_x] = [0,0,0,0,0,0]
        print(f"{player_x}: Key not exists, a new key has been created")
        print("Rerun db_auth")
        db_auth(player_x)

# Function for checking index
def index_auth(player_x,index_x):
    # index_x = index_x - 1
    return player_scores[player_x][index_x - 1] # Index start from 0, 5 is the sixth index
        # Unfinished
        # Need add more logic

# Function for validate the main logic about the game rules
def validate(player_y,dice_x):
    print("\nValidation:")
    if dice_x == 6:
        if index_auth(player_y,6) == 0:
            print(f"6({name(6)}) is 0 (Empty)")
            if index_auth(player_y,dice_x) == 0:
                add_score(player_y,dice_x)
            else:
                print(f"6({name(6)}) is not 0 (Already has {name(6)})\nAbort add_score")
            # player_scores[player_y][dice_x - 1] = player_scores[player_y][dice_x - 1] + 1
            # print(f"{dice_x}({name(dice_x)}) is vaild\n{name(dice_x)} added 1")
        else:
            pass # Requirements meet
    elif dice_x == 5:
        if index_auth(player_y,6) == 1:
            print(f"Dependent: 6({name(6)}) is 1 (Requirements meet)")
            print(f"{dice_x}/{name(dice_x)} is 1") # Unfinished
            if index_auth(player_y,dice_x) == 0:
                add_score(player_y,dice_x)
            else:
                print(f"5({name(5)}) is not 0 (Already has {name(5)})\nAbort add_score")
        else:
            print(f"Dependent: 6({name(6)}) is not 1 (Requirements not meet)")
            print("The body must exist before the head can be added")

    elif dice_x == 4:
        if index_auth(player_y,6) == 1:
            print(f"Dependent: 6({name(6)}) is 1 (Requirements meet)")
            if index_auth(player_y,dice_x) == 0:
                add_score(player_y,dice_x)
            else:
                print(f"4({name(4)}) is not 0 (Already has {name(4)})\nAbort add_score")
        else:
            print(f"Dependent: 6({name(6)}) is not 1 (Requirements not meet)")
            print("The body must exist before the tail can be added")
    elif dice_x == 3:
        if index_auth(player_y,6) == 1:
            print(f"Dependent: 6({name(6)}) is 1 (Requirements meet)")
            if index_auth(player_y,dice_x) < 4:
                add_score(player_y,dice_x)
            else:
                print(f"3({name(3)}) is not lower than 4 (Already has maximum {name(3)})\nAbort add_score")
        else:
            print(f"Dependent: 6({name(6)}) is not 1 (Requirements not meet)")
            print("The body must exist before the leg can be added")
    elif dice_x == 2:
        if index_auth(player_y,5) == 1:
            print(f"Dependent: 5({name(5)}) is 1 (Requirements meet)")
            if index_auth(player_y,dice_x) < 2:
                add_score(player_y,dice_x)
            else:
                print(f"2({name(2)}) is not lower than 2 (Already has maximum {name(2)})\nAbort add_score")
        else:
            print(f"Dependent: 5({name(5)}) is not 1 (Requirements not meet)")
            print("The head must exist before the antenna can be added")
    elif dice_x == 1:
        if index_auth(player_y,5) == 1:
            print(f"Dependent: 5({name(5)}) is 1 (Requirements meet)")
            if index_auth(player_y,dice_x) < 2:
                add_score(player_y,dice_x)
            else:
                print(f"1({name(1)}) is not lower than 2 (Already has maximum {name(1)})\nAbort add_score")
        else:
            print(f"Dependent: 5({name(5)}) is not 1 (Requirements not meet)")
            print("The head must exist before the eye can be added")
    else:
        print("Unvaild") # For now

def add_score(player_y,dice_x):
    player_scores[player_y][dice_x - 1] = player_scores[player_y][dice_x - 1] + 1
    print(f"{dice_x}({name(dice_x)}) is vaild\n{name(dice_x)} added 1")

# Check for win, run after each db change
def win_auth(player_z):
    if player_scores[player_z] == [2,2,4,1,1,1]:
        print(f"\nPlayer {player_z} has win:")
        print(player_scores[player_z])
        return True
    else:
        return False
    

# Logic
print("----Beetle Lab----\n")
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
    while True:  # Loop until a valid and unique name is entered
        try:
            player_name = input(f"Enter the name for Player {i + 1}: ")

            # Check if name is empty or contains invalid characters (basic validation)
            if player_name.strip() == "":
                raise ValueError("Player name cannot be empty or spaces only.")
            
            if check_duplicate_name(player_name, player_scores):
                raise ValueError(f"Player name '{player_name}' already exists.")
            
            # If name passes all checks, add it to the dictionary
            player_scores[player_name] = [0, 0, 0, 0, 0, 0]
            break  # Exit loop when valid, unique name is entered
        
        except ValueError as ve:
            print(f"Error: {ve}. Please try again.")

# Output the initialized dictionary
print("\nPlayer score tracking initialized:")
print(player_scores)

while not player_win:
    for player_now in player_scores.keys():
        print(f"\n\n----Current Player: {player_now}----")
    
        input("Press Enter to roll the dice [Enter]")  # Wait for the player to press Enter
        rand_dice = roll_dice()

        print(f"\nDice result: {rand_dice}({name(rand_dice)})")

        db_auth(player_now)

        validate(player_now,rand_dice)

        print(f"\nUpdated scores for {player_now}:")
        # print(f"\nPlayer {player_now} updated scores")
        print(player_scores[player_now])
        
        if win_auth(player_now):
            print("\n----Game finished----")
            print(player_scores)
            player_win = True
            break # Avoid loop have extra round
        else:
            pass

# Finction could not input 2 value/information //Fixed
# Explain to play the logic e.g. No change because of condition not meet //Fixed
# Add def check_duplicate_name(player_name, player_scores): //Added
# Add def check_duplicate_name(player_name, player_scores) to loop without breaking the loop //Fixed
# Find out why after player_win = True loop still run an extra round
