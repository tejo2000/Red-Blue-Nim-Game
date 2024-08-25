# Red-Blue-Nim-Game

Red-Blue Nim Game
The Red-Blue Nim game is a variant of the classic Nim game. Players take turns picking marbles from either a red or a blue pile. Depending on the version of the game (standard or misère), the goal is to either avoid or force being the one to empty a pile.

Programming Language and Version Used: Python 3.9.7

Code Structure
Functions:

Utility Functions:

utility(state, version): Computes the score for a given game state and version.
terminal_test(state): Checks if the game has ended based on the game state.

Game Logic Functions:

actions(state, version): Returns available actions based on the game state and version.
result(state, action): Returns the new game state after a given action.

Alpha-Beta Pruning Functions:

max_value(state, alpha, beta, version): Recursive function for the Maximizer player.
min_value(state, alpha, beta, version): Recursive function for the Minimizer player.
alpha_beta_search(state, version): Main decision-making function using the Alpha-Beta Pruning.
Player Action Functions:

human_move(state): Gets the move choice from the human player.

Game Loop:

play_turn(state, version, current_player): Manages turns between human and computer players.
Main Execution:

The code block under if __name__ == "__main__": is the starting point for the program. It sets up the game and initiates the game loop.


Instructions to Run the Code:
red_blue_nim.py <num-red> <num-blue> <version> <first-player> 
<num-red> and <num-blue> are required. (Number of red and blue marbles respectively)
<version> is either
standard - Player loses if either pile empty on their turn 
misere - Player wins if either pile empty on their turn
 <first-player> can be
computer - play a full game from given state with computer starting the game followed by human 
human - play a full game from given state with human starting the game followed by computer

Example:
python3 red_blue_nim.py 5 2 standard human: initialises the game with 5 red and 2 blue marbles with human taking the first turn in standard version.
