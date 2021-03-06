class OxoBoard:
    def __init__(self):
        # Initialising board array
        self.boardList = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def get_square(self, x, y):
        # Returns value of board square
        return self.boardList[y][x]

    def set_square(self, x, y, mark):
        # Fills square with mark, unless it's already filled
        if self.boardList[y][x] == 0:
            self.boardList[y][x] = mark
            return True
        else:
            return False

    def is_board_full(self):
        # Returns false if any of the squares contain 0
        for x in xrange(3):
            for y in xrange(3):
                if self.boardList[y][x] == 0:
                    return False
        return True

    def get_winner(self):
        # Checks rows, columns and diagonals for 3 matching squares that aren't 0 and returns the square value
        for i in xrange(3):
            # Horizontal matches
            if self.boardList[i][0] == self.boardList[i][1] == self.boardList[i][2] and self.boardList[i][0] > 0:
                return self.boardList[i][0]
            # Vertical matches
            elif self.boardList[0][i] == self.boardList[1][i] == self.boardList[2][i] and self.boardList[0][i] > 0:
                return self.boardList[0][i]
        # Diagonal matches
        if self.boardList[0][0] == self.boardList[1][1] == self.boardList[2][2] and self.boardList[0][0] > 0:
            return self.boardList[0][0]
        elif self.boardList[0][2] == self.boardList[1][1] == self.boardList[2][0] and self.boardList[0][2] > 0:
            return self.boardList[0][2]
        return 0

    def show(self):
        # Display the current board state in the terminal
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
    # Prompt the player to enter a square
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


# The main game
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
                board.show()
                print "Player", winner, "wins!"
                break   # End the game
            elif board.is_board_full():
                board.show()
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
