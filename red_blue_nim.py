# -*- coding: utf-8 -*-
"""test2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZblQ51xXnycfCykiwkF19wU1T90zW3oD
"""

import sys

#  utility function
def utility(state, version):
    if version == "standard":
        return state[0] * 2 + state[1] * 3
    else:  # misere
        return -(state[0] * 2 + state[1] * 3)

def terminal_test(state):
    return state[0] == 0 or state[1] == 0

def actions(state, version):
    if version == "standard":
        order = ['B', 'R']
    else:  # misere
        order = ['R', 'B']

    return [action for action in order if (action == 'R' and state[0] > 0) or (action == 'B' and state[1] > 0)]

def result(state, action):
    if action == 'R':
        return (state[0] - 1, state[1])
    else:  # B
        return (state[0], state[1] - 1)

def max_value(state, alpha, beta, version):
    if terminal_test(state):
        return utility(state, version)
    v = float('-inf')
    for action in actions(state, version):
        v = max(v, min_value(result(state, action), alpha, beta, version))
        if v >= beta:
            return v
        alpha = max(alpha, v)
    return v

def min_value(state, alpha, beta, version):
    if terminal_test(state):
        return utility(state, version)
    v = float('inf')
    for action in actions(state, version):
        v = min(v, max_value(result(state, action), alpha, beta, version))
        if v <= alpha:
            return v
        beta = min(beta, v)
    return v

def alpha_beta_search(state, version):
    best_action = None
    best_val = float('-inf')
    for action in actions(state, version):
        val = min_value(result(state, action), float('-inf'), float('inf'), version)
        if val > best_val:
            best_val = val
            best_action = action
    return best_action

def human_move(state):
    while True:
        choice = input("Choose a marble to pick (R for Red, B for Blue): ").upper()
        if choice in ['R', 'B']:
            return choice
        print("Invalid choice. Please pick either R or B.")

def play_turn(state, version, current_player):
    print(f"\nAvailable Marbles - Red: {state[0]}, Blue: {state[1]}")

    if terminal_test(state):
        if version == "standard":
            winner = "computer" if current_player == "human" else "human"
            score = state[0] * 2 + state[1] * 3
        else:  # misere
            winner = current_player
            score = state[0] * 2 + state[1] * 3

        print(f"{winner} wins with a score of {score}!")
        return state

    if current_player == 'computer':
        move = alpha_beta_search(state, version)
        print(f"Computer chooses to pick {move} marble.")
        new_state = result(state, move)
        return play_turn(new_state, version, 'human')
    else:
        move = human_move(state)
        new_state = result(state, move)
        return play_turn(new_state, version, 'computer')



if __name__ == "__main__":
    num_red = int(sys.argv[1])
    num_blue = int(sys.argv[2])
    version = sys.argv[3] if len(sys.argv) > 3 else "standard"
    first_player = sys.argv[4] if len(sys.argv) > 4 else "computer"

    initial_state = (num_red, num_blue)
    final_state = play_turn(initial_state, version, first_player)