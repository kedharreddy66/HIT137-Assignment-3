# Tank Battle - Pygame Implementation

Welcome to **Tank Battle**, a side-scrolling 2D tank game built using Pygame. In this game, players control a tank to move, jump, and shoot while battling enemies and bosses across multiple levels.

## Table of Contents

1. [Installation](#installation)
2. [Getting Started](#getting-started)
3. [Controls](#controls)
4. [Game Features](#game-features)
5. [Code Explanation](#code-explanation)

## Installation

Before you begin, make sure you have Python and Pygame installed on your system. Follow the steps below:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/kedharreddy66/HIT137-Assignment-3.git
   cd your-repo-name
   ```

2. **Install Pygame**:
   Install Pygame using pip:
```bash
pip install -r requirements.txt
```

3. **Run the Game**:
   Start the game by running the `main.py` file:
   ```bash
   python main.py
   ```

## Getting Started

Upon starting the game, you will be greeted with an instruction screen. This screen provides information about the controls and game mechanics. Press the `ENTER` key to begin the game.

### Controls

- **Arrow Keys**: Move the tank left or right.
- **SPACE**: Jump.
- **CTRL**: Shoot projectiles.

Your goal is to navigate through enemies and defeat the boss in each level to progress.

## Game Features

- **Multiple Levels**: The game includes 3 levels with increasing difficulty. Each level lasts for 30 seconds, and a boss appears at the 25-second mark.
- **Dynamic Boss Fights**: Each level features a unique boss that gets progressively larger and harder to defeat.
- **Health System**: Collect health packs to regain health and survive longer.
- **Score Tracking**: Your score increases as you defeat enemies and bosses, and it is displayed on the screen alongside the level number.

## Code Explanation

### Structure
The codebase is structured into several modules to keep it organized:
- **`main.py`**: The main entry point of the game. It handles the game loop, user inputs, and transitions between levels.
- **`src/player.py`**: Defines the `Player` class, including movement, jumping, and shooting mechanics.
- **`src/enemy.py`**: Defines the `Enemy` class, including regular enemies and bosses.
- **`src/collectible.py`**: Defines the `Collectible` class for health packs.
- **`src/level.py`**: Manages the level structure, including enemy spawning, boss appearance, and level completion conditions.

### How the Code Works
1. **Game Initialization**: When the game starts (`main.py`), the Pygame library initializes the screen and sets up the game clock.
2. **Start Menu**: The `start_menu` function displays the game title and instructions. The game begins when the player presses `ENTER`.
3. **Game Loop**: The main function controls the game loop, updating player movements, enemy interactions, and projectiles. It also keeps track of scores and health.
4. **Level Management**: The `Level` class handles enemy spawning and collectible generation. A boss appears at the 25-second mark in each level. The level completes after 30 seconds or when the boss is defeated.
5. **Transitioning Levels**: After each level, the next level starts automatically. The game ends when the final boss is defeated, and a message is displayed to congratulate the player.

By following this structure, the code ensures modularity and ease of expansion if more levels or features are added in the future.

Feel free to adjust the details (e.g., https://github.com/kedharreddy66/HIT137-Assignment-3.git) based on your specific project setup! Let me know if you'd like any further modifications.