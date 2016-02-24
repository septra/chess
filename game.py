class Piece(object):
    """
    Definition for a piece.
    """
    def __init__(self, colour, name, uid = None):
        self.colour = colour
        self.name = name
        self.uid = uid

    def valid_moves(self, position):
        pass

    def __repr__(self):
        return str("{name}({colour})".\
                    format(
                        name=self.name,
                        colour=self.colour[0]))

class Board(object):
    """
    The main game class.
    """
    def __init__(self):
        self.grid = {
            letter: [None]*8 for letter in "ABCDEFGH"
        }
        self.place_black()
        self.place_white()

    def move_piece(self, cur_position, next_position):
        piece  = self.piece_on_position(cur_position)
        print piece
        self.grid[next_position[0]][int(next_position[1])-1] = piece
        self.grid[cur_position[0]][int(cur_position[1])-1] = None

    def piece_on_position(self, position):
        return self.grid[position[0]][int(position[1])-1]

    def place_white(self):
        # Place pawns
        pawns = [Piece('Whites', 'P', uid=x) for x in xrange(1,9)]
        for n,x in enumerate("ABCDEFGH"):
            self.grid[x][1] = pawns[n]

        # Place Rooks
        rooks = [Piece('Whites', 'R', uid=x) for x in xrange(1,3)]
        self.grid['A'][0], self.grid['H'][0] = rooks

        # Place Knights
        knights = [Piece('Whites', 'N', uid=x) for x in xrange(1,3)]
        self.grid['B'][0], self.grid['G'][0] = knights

        # Place Bishops
        bishops = [Piece('Whites', 'B', uid=x) for x in xrange(1,3)]
        self.grid['C'][0], self.grid['F'][0] = bishops

        # Place King and Queen
        king = Piece('Whites', 'K')
        queen = Piece('Whites', 'Q')
        self.grid['D'][0], self.grid['E'][0] = queen, king

    def place_black(self):
        # Place pawns
        pawns = [Piece('Blacks', 'P', uid=x) for x in xrange(1,9)]
        for n,x in enumerate("ABCDEFGH"):
            self.grid[x][6] = pawns[n]

        # Place Rooks
        rooks = [Piece('Blacks', 'R', uid=x) for x in xrange(1,3)]
        self.grid['A'][7], self.grid['H'][7] = rooks

        # Place Knights
        knights = [Piece('Blacks', 'N', uid=x) for x in xrange(1,3)]
        self.grid['B'][7], self.grid['G'][7] = knights

        # Place Bishops
        bishops = [Piece('Blacks', 'B', uid=x) for x in xrange(1,3)]
        self.grid['C'][7], self.grid['F'][7] = bishops

        # Place King and Queen
        king = Piece('Blacks', 'K')
        queen = Piece('Blacks', 'Q')
        self.grid['D'][7], self.grid['E'][7] = queen, king

    def __repr__(self):
        return "\n".join(str(row) for row in self.grid)
