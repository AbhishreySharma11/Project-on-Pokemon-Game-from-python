# Pokemon Battle Game in Python

## Introduction

This Python program simulates a simple interactive Pokemon battle game. It allows a trainer to select a starter Pokemon and battle against random wild Pokemon in turn-based combat. The game features save/load functionality allowing persistent progress using JSON serialization.

The project demonstrates fundamental concepts including object-oriented programming, input validation, file handling, randomization, and encapsulation. It provides an engaging way for beginners to practice Python programming in a game development context.

## Setup Instructions

### Prerequisites

- Python 3.x installed on your system. Download from [python.org](https://www.python.org/downloads/).

### Installation

1. Copy the full Python code into a file named `main.py` (or organize into modules if preferred).
2. Ensure the `save.json` file (created when saving your game) will be in the same directory as the script.

### Running the Game

- Open a terminal or command prompt.
- Navigate to the directory containing `main.py`.
- Run the program:
- Follow the on-screen prompts to enter trainer name, select Pokemon, battle, save progress, or exit.

## Code Details

### pokemon.py (Class Pokemon)

- Defines Pokemon attributes: `name`, `hp`, `attack`, `defense`.
- Includes `random_pokemon()` to generate random wild Pokemon with preset stats.
- `__str__()` method provides a formatted string of Pokemon stats.

### player.py (Class Player)

- Represents the trainer whose attributes include `name` and chosen `pokemon`.
- Offers starter Pokemon selection with validation.
- Starter Pokemon stats vary slightly per choice.

### battle.py (Function battle)

- Implements turn-based combat with randomized attacker each turn.
- Calculates damage as `attack - defense` minimum 1.
- Updates and displays HP after each attack.
- Declares and outputs the battle winner.

### utils.py (Save/Load Functions)

- `save_game(filename, player)`: Serializes player and Pokemon info to JSON file.
- `load_game(filename)`: Deserializes JSON to reconstruct player and Pokemon.

### main.py (Program Entrypoint)

- Greets player and attempts to load saved game.
- If no saved data, lets user create a new profile.
- Presents user menu to battle, view Pokemon, save, or exit.
- Validates inputs and processes user commands.

## Design Highlights

- Object-oriented approach encapsulates entities and logic.
- Static methods simplify random Pokemon generation.
- Robust input validation for user safety.
- File persistence preserves game state between sessions.
- Randomized battle turns add dynamic gameplay.

## Future Enhancements

- Add special moves, types, and abilities in battles.
- Support multiple Pokemon per player with switching.
- Create graphical interface using `pygame` or other GUI libraries.
- Expand Pokedex with more Pokemon variants.
- Introduce experience points, leveling, and evolution.
- Implement network multiplayer battles.
- Improve save system with multiple profiles and slots.

---

Thank you for playing the Pokemon Battle Game!
