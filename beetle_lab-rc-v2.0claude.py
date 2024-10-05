# Beetle Game
# A dice game where players build a beetle by rolling dice

import random

# Player Data Storage
# Dictionary to store player scores where:
# - Keys are player names
# - Values are lists of 6 integers representing beetle parts:
#   [eyes, antennae, legs, tail, head, body]
player_scores = {}

def check_duplicate_name(player_name, player_scores):
    """Check if a player name already exists in the game."""
    if player_name in player_scores:
        print(f"Player name '{player_name}' already exists. Please choose a different name.")
        return True
    return False

def add_players():
    """
    Add players to the game.
    Continuously prompts for player names until an empty input is given.
    """
    while True:
        player_name = input("Enter player name (leave blank to finish): ").strip()
        if player_name == "":
            break
        if not check_duplicate_name(player_name, player_scores):
            player_scores[player_name] = [0, 0, 0, 0, 0, 0]
            print(f"Player '{player_name}' added.")

def roll_dice():
    """Simulate rolling a six-sided die."""
    return random.randint(1, 6)

def name(number):
    """Convert dice number to beetle part name."""
    part_names = {
        6: "Body",
        5: "Head",
        4: "Tail",
        3: "Leg",
        2: "Antenna",
        1: "Eye"
    }
    return part_names.get(number, "Not valid")

def db_auth(player):
    """
    Verify player exists in database and initialize if needed.
    Debug function to show current player scores.
    """
    if player in player_scores:
        print(f"\nPlayer {player} db_auth")
        print(f"Pre-updated scores for {player}:")
        print(player_scores[player])
        print("Key exists, no database update")
        return True
    else:
        player_scores[player] = [0, 0, 0, 0, 0, 0]
        print(f"{player}: Key not exists, a new key has been created")
        print("Rerun db_auth")
        db_auth(player)

def index_auth(player, index):
    """Get the current count of a specific beetle part for a player."""
    return player_scores[player][index - 1]

def add_score(player, dice_value):
    """Increment the count of a specific beetle part for a player."""
    player_scores[player][dice_value - 1] += 1
    print(f"{dice_value}({name(dice_value)}) is valid\n{name(dice_value)} added 1")

def validate(player, dice_value):
    """
    Validate if a dice roll can be used to add a beetle part.
    Checks game rules and dependencies between parts.
    """
    print("\nValidation:")
    
    # Dictionary defining part dependencies and max counts
    part_rules = {
        6: {"max": 1, "depends_on": None},
        5: {"max": 1, "depends_on": 6},
        4: {"max": 1, "depends_on": 6},
        3: {"max": 4, "depends_on": 6},
        2: {"max": 2, "depends_on": 5},
        1: {"max": 2, "depends_on": 5}
    }
    
    rule = part_rules[dice_value]
    current_count = index_auth(player, dice_value)
    
    # Check dependency
    if rule["depends_on"]:
        if index_auth(player, rule["depends_on"]) == 0:
            print(f"Dependent: {rule['depends_on']}({name(rule['depends_on'])}) "
                  f"is not 1 (Requirements not met)")
            print(f"The {name(rule['depends_on']).lower()} must exist before "
                  f"the {name(dice_value).lower()} can be added")
            return
    
    # Check if maximum count reached
    if current_count < rule["max"]:
        add_score(player, dice_value)
    else:
        print(f"{dice_value}({name(dice_value)}) has reached its maximum "
              f"({rule['max']})\nAbort add_score")

def win_auth(player):
    """Check if a player has won by completing their beetle."""
    winning_condition = [2, 2, 4, 1, 1, 1]
    if player_scores[player] == winning_condition:
        print(f"\nPlayer {player} has won:")
        print(player_scores[player])
        return True
    return False

# Main game loop
def main():
    print("----Beetle Game----\n")
    
    # Initialize players
    add_players()
    
    print("\nPlayer score tracking initialized:")
    print(player_scores)
    
    player_win = False
    while not player_win:
        for current_player in player_scores:
            print(f"\n\n----Current Player: {current_player}----")
            
            input("Press Enter to roll the dice")
            dice_result = roll_dice()
            
            print(f"\nDice result: {dice_result}({name(dice_result)})")
            
            db_auth(current_player)
            validate(current_player, dice_result)
            
            print(f"\nUpdated scores for {current_player}:")
            print(player_scores[current_player])
            
            if win_auth(current_player):
                print("\n----Game finished----")
                print(player_scores)
                return

if __name__ == "__main__":
    main()