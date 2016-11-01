class OxoBoard:
    def __init__(self):
        """ The initialiser. Initialise any fields you need here. """
        boardList = [[0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0]]

        # raise NotImplementedError("TODO: implement __init__")

    def get_square(self, x, y):
        """ Return 0, 1 or 2 depending on the contents of the specified square. """
        self.x = x
        self.y = y

        return boardList[self.y * 3 + self.x]
        # raise NotImplementedError("TODO: implement get_square")

    def set_square(self, x, y, mark):
        """ If the specified square is currently empty (0), fill it with mark and return True.
            If the square is not empty, leave it as-is and return False. """
        if boardList[self.y * 3 + self.x] == 0:
            boardList[self. y * 3 + self.x] = mark
        else:
            return False
        # raise NotImplementedError("TODO: implement set_square")

    def is_board_full(self):
        """ If there are still empty squares on the board, return False.
            If there are no empty squares, return True. """
        # cycles through x, 0, 1, 2 and for each does y, 0, 1, 2. If any are empty false is returned and the cycle breaks. If the cycle finishes it returns true.
        for y in xrange(3):
            for x in xrange(3):
                if boardList[y * 3 + x] == 0:
                    return False
                    break
            return True

        # raise NotImplementedError("TODO: implement is_board_full")

    def get_winner(self):
        """ If a player has three in a row, return 1 or 2 depending on which player.
            Otherwise, return 0. """

        if boardList[1] == boardList [2] == boardList[3]:  # horizontal wins
            return boardList[1]
        elif boardList[4] == boardList [5] == boardList[6]:
            return boardList[4]
        elif boardList[7] == boardList[8] == boardList[9]:
            return boardList[7]
        elif boardList[1] == boardList[4] == boardList[7]:  #vertical wins
            return boardList[1]
        elif boardList[2] == boardList[5] == boardList[8]:
            return boardList[2]
        elif boardList[3] == boardList[6] == boardList[9]:
            return boardList[3]
        elif boardList[1] == boardList[5] == boardList[9]:  #diagonal wins
            return boardList[1]
        elif boardList[3] == boardList[5] == boardList[7]:
            return boardList[3]
        else:
            return 0
        # raise NotImplementedError("TODO: implement get_winner")

    def show(self):
        """ Display the current board state in the terminal. You should not need to edit this. """
        for y in xrange(3):
            if y > 0:
                print "--+---+--"
            for x in xrange(3):
                if x > 0:
                    print '|',

                # Print a space for empty (0), an O for player 1, or an X for player 2
                print " OX"[self.get_square(x, y)],
            print


def input_square():
    """ Prompt the player to enter a square. You should not need to edit this. """
    while True:
        input = raw_input("Enter x,y where x=0,1,2, y=0,1,2: ")
        if input.count(',') != 1:
            print "Input must contain exactly one comma!"
            continue

        x, y = input.split(',')
        try:
            x = int(x)
            y = int(y)
        except ValueError:
            print "Input must be two numbers separated by a comma!"
            continue

        if x < 0 or x > 2 or y < 0 or y > 2:
            print "Input is out of bounds!"
            continue

        return x, y


# The main game. You should not need to edit this.
if __name__ == '__main__':
    board = OxoBoard()
    current_player = 1
    while True:
        board.show()
        print "Choose a square, Player", current_player
        x, y = input_square()

        if board.set_square(x, y, current_player):
            # Move was played successfully, so check for a winner
            winner = board.get_winner()
            if winner != 0:
                print "Player", winner, "wins!"
                break   # End the game
            elif board.is_board_full():
                print "It's a draw!"
                break   # End the game
            else:
                # Switch players
                if current_player == 1:
                    current_player = 2
                else:
                    current_player = 1
        else:
            # Move was not played successfully
            print "That square is already filled!"
