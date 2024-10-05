# Beetle Game

Beetle is a simple yet entertaining dice game for two or more players, where the goal is to be the first to draw a complete beetle. The game is played using a single six-sided die, with each roll determining which beetle part can be drawn. This project includes a Python implementation of the Beetle game, allowing players to play against the computer or with a second player.

## Game Rules

1. Players take turns rolling a six-sided die to determine which part of the beetle they can draw.
2. The body must be drawn first by rolling a **6**.
3. Once the body is drawn, other parts can be added:
   - **5**: Draw the head (required before adding eyes or antennae)
   - **4**: Draw the tail
   - **3**: Draw one of the four legs
   - **2**: Draw one of the two antennae (only after the head is drawn)
   - **1**: Draw one of the two eyes (only after the head is drawn)
4. The first player to draw all parts of the beetle wins.

## Features

- **Single Player Mode**: Play against the computer.
- **Multiplayer Mode**: Play against a friend.
- **Simple Graphics**: Visual representation of the beetle as parts are drawn.

## How to Play

1. Run the Python script to start the game.
2. Choose between single-player or multiplayer mode.
3. Take turns rolling the die and drawing parts until a player completes the beetle.

## Getting Started

To get started, clone the repository and run the game script:

```sh
# Clone the repository
git clone https://github.com/username/beetle-game.git

# Navigate to the directory
cd beetle-game

# Run the game
python beetle.py
```

## Development Steps

1. **Decomposition**: The game was broken down into logical steps, including rolling the die, checking conditions, and drawing parts.
2. **Pseudocode**: An algorithm was drafted in pseudocode to outline the game mechanics.
3. **Implementation**: The pseudocode was translated into Python, followed by testing and debugging.

## Resources

- [Beetle Game Overview Video](https://www.youtube.com/watch?v=Jxe__lV9VHw&t=27s)

## Contributing

Feel free to fork the repository and submit pull requests for new features or improvements.

## License

This project is licensed under the MIT License.

### Written by ChatGPT-4
