from alphabeta import TicTacToe
from alphabeta import alpha_beta_value


def play(state):
    """Makes turn and prints the result of it until the game is over
    :param state: The initial state of the game (TicTacToe)
    """
    return alpha_beta_value(state)

def main():
    """This function will look at the current state of a tic tac toe board and predict which player (X's or O's) will win given they pick the optimal moves.

    Outcomes:
     1 = X's win
     0 = Draw
    -1 = O's win
    """

    board = 'oo?' + 'x??' + 'x??'
    state = TicTacToe(state = board, corsses_turn = True)
    print(play(state))


if __name__ == '__main__':
    main()
