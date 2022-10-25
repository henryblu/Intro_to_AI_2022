TEMPLATE_FIELD = '|e|e|e|\n|e|e|e|\n|e|e|e|\n'
HUGE_NUMBER = 1000000


class AlphaBetaNode(object):
    def __init__(self):
        pass

    def generate_children(self):
        pass

    def is_max_node(self):
        pass

    def is_end_state(self):
        pass

    def value(self):
        pass 


class TicTacToe(AlphaBetaNode):
    """Class that contains current state of the game and implements AlphaBetaNode methods
    :attr state: Current state of the board (str)
    :attr state: Indicates whose turn it is (Boolean)
    """

    def __init__(self, state, crosses_turn):
        super().__init__()
        self.state = state
        self.crosses_turn = crosses_turn

    def is_end_state(self):
        return ('?' not in self.state) or self.won('x') or self.won('o')

    def won(self, c):
        triples = [self.state[0:3], self.state[3:6], self.state[6:9], self.state[::3], self.state[1::3],
                   self.state[2::3], self.state[0] + self.state[4] + self.state[8],
                   self.state[2] + self.state[4] + self.state[6]]
        combo = 3 * c
        return combo in triples

    def __str__(self):
        field = TEMPLATE_FIELD
        for c in self.state:
            field = field.replace('e', c, 1)
        return field

    def is_max_node(self):
        return self.crosses_turn

    def generate_children(self):
        """
        Generates list of all possible states after this turn
        :return: list of TicTacToe objects
        """
        children=[]
        for x in range(9):
            if self.state[x] == '?':
                child = self.state[0:x] + ('x' if self.crosses_turn else 'o') + self.state[x+1:9]
                children.append(TicTacToe(child, (False if self.crosses_turn else True)))

        return children

    def value(self):
        """
        Current score of the game (0, 1, -1)
        :return: int
        """

        if ('?' not in self.state): return 0
        elif self.won('x'): return 1
        elif self.won('o'): return -1



def alpha_beta_value(node):
    """Implements the MinMax algorithm with alpha-beta pruning, this function sees whos turn it is in the initial state (Xs or Os) and calls either a min_value search or a max value search using alpha beta peramiters.

    :param node: State of the game (TicTacToe)
    :return: int
    """
    if node.crosses_turn: 
        return max_value(node, (-HUGE_NUMBER) , HUGE_NUMBER )
    else: 
        return min_value(node, (-HUGE_NUMBER) , HUGE_NUMBER )


def max_value(node, alpha, beta):
    """
    
    """
    if node.is_end_state(): return node.value()
    v = -HUGE_NUMBER
    for child in node.generate_children():
       v = max(v, min_value(child, alpha, beta))
       alpha = max(alpha, v)
       if alpha >= beta: return v
    return v


def min_value(node, alpha, beta):
    if node.is_end_state(): return node.value()
    v = HUGE_NUMBER
    for child in node.generate_children():
       v = min(v, max_value(child, alpha, beta))
       beta = min(beta, v)
       if alpha >= beta: return v
    return v
