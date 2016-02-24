import unittest
from game import Piece, Board

class TestGame(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_piece_functionality(self):
        colour_black = "Black"
        colour_white = "White"
        black_piece_name = "K"
        white_piece_name = "Q"

        black_piece = Piece('Black', 'K')
        white_piece = Piece('White', 'Q')

        self.assertEqual(black_piece.name, black_piece_name)
        self.assertEqual(black_piece.colour, colour_black)

        self.assertEqual(white_piece.name, white_piece_name)
        self.assertEqual(white_piece.colour, colour_white)

        self.assertNotEqual(black_piece, white_piece)

    def test_board_functionality(self):
        # Test correct number of columns
        self.assertEqual(len(self.board.grid.keys()), 8)

        # Test correct number of rows
        self.assertEqual(len(self.board.grid.values()), 8)

    def test_correct_initial_piece_placement(self):

        for colour, row in zip(["White", "Black"], ["1","8"]):
            rook = Piece(colour, 'R')
            self.assertEqual(
                    str(self.board.piece_on_position('A' + row)),
                    str(rook))

    def test_piece_move_functionality(self):
        a2_pawn = self.board.piece_on_position('A2')
        self.board.move_piece('A2', 'A4')
        self.assertEqual(
            self.board.piece_on_position('A2'),
            "  * "
        )
        self.assertEqual(
            self.board.piece_on_position('A4'),
            a2_pawn
        )

if __name__=='__main__':
    unittest.main()
