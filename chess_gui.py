import logging
import os

import pygame

from src.board import *
from src.chess_pieces import WSYMBOLS, BSYMBOLS

logging.getLogger().setLevel(logging.DEBUG)

main_logger = logging.getLogger('main')
main_logger.setLevel(logging.DEBUG)


def main():
    """
    The loop the game runs in.
    It takes a user input, checks that input for validity, and calls move on it if it is valid.
    It terminates once the game is won or a player quits the game.
    """
    
    window_size = 256, 256
    length_of_unit_square = int(window_size[0] / 8)
    framerate = 60
    
    pygame.init()
    pygame.display.set_caption('Chess')
    Clock = pygame.time.Clock()
    
    
    screen = pygame.display.set_mode(window_size)

    # font = pygame.font.SysFont('Arial', 20)
    
    colors = {
        'White': [255, 255, 255],
        'Grey': [100, 100, 100],
        'Black': [0, 0, 0]
        }
    screen.fill(colors['Grey'])
    board = Board()

    def checkerboard():
        logging.info('Setting up GUI-Checkerboard')
        for row in board.game_board:
            for square in row:
                if square.row % 2 == 0:
                    if square.column % 2 == 0:
                        pygame.draw.rect(screen, colors['White'], pygame.Rect(square.row * length_of_unit_square,
                                                                              square.column * length_of_unit_square,
                                                                              length_of_unit_square,
                                                                              length_of_unit_square))
                    else:
                        pygame.draw.rect(screen, colors['Black'], pygame.Rect(square.row * length_of_unit_square,
                                                                              square.column * length_of_unit_square,
                                                                              length_of_unit_square,
                                                                              length_of_unit_square))
                else:
                    if square.column % 2 == 1:
                        pygame.draw.rect(screen, colors['White'], pygame.Rect(square.row * length_of_unit_square,
                                                                              square.column * length_of_unit_square,
                                                                              length_of_unit_square,
                                                                              length_of_unit_square))
                    else:
                        pygame.draw.rect(screen, colors['Black'], pygame.Rect(square.row * length_of_unit_square,
                                                                              square.column * length_of_unit_square,
                                                                              length_of_unit_square,
                                                                              length_of_unit_square))
    
    def place_pieces():
        logging.info('Setting up GUI-Pieces')
        for row in board.game_board:
            for square in row:
                if square.piece != '☐':
                    # Black Pieces
                    if square.piece == BSYMBOLS[1]:  # Black Pawn
                        image = pygame.image.load(os.path.join('Pieces', 'black_p.png')).convert()
                        rect = screen.blit(image,
                                           [square.row * length_of_unit_square, square.column * length_of_unit_square])
                        pygame.display.update(rect)
                    if square.piece == BSYMBOLS[2]:  # Black Rook
                        pass
                    if square.piece == BSYMBOLS[3]:  # Black Knight
                        pass
                    if square.piece == BSYMBOLS[4]:  # Black Bishop
                        pass
                    if square.piece == BSYMBOLS[5]:  # Black Queen
                        pass
                    if square.piece == BSYMBOLS[6]:  # Black King
                        pass

                    # White Pieces
                    if square.piece == WSYMBOLS[1]:  # White Pawn
                        image = pygame.image.load(os.path.join('Pieces', 'white_p.png')).convert()
                        rect = screen.blit(image,
                                           [square.row * length_of_unit_square, square.column * length_of_unit_square])
                        pygame.display.update(rect)
                    if square.piece == WSYMBOLS[2]:  # White Rook
                        pass
                    if square.piece == WSYMBOLS[3]:  # White Knight
                        pass
                    if square.piece == WSYMBOLS[4]:  # White Bishop
                        pass
                    if square.piece == WSYMBOLS[5]:  # White Queen
                        pass
                    if square.piece == WSYMBOLS[6]:  # White King
                        pass
                else:
                    pass

    while True:  # Main loop
        Clock.tick(framerate)
        print(board)
    
        checkerboard()
        place_pieces()
        pygame.display.flip()
        
        move_valid = False  # makes the input loop run at least once
        move = None
        pygame.event.pump()
        while not move_valid:
            pygame.event.pump()
            pinput = input(f'{board.turn}: ').lower()  # .lower() to make everything lowercase
            
            if pinput in ['quit', 'exit']:
                print(f'{board.turn} quit the game.')
                return 0
            
            move = board.getMove(pinput)
            
            if move is not None:
                move_valid = board.is_valid_move(move)
            if not move_valid:
                print(f'Move [{pinput}] is not valid.')
            
            logging.debug(f"Move valid? {move_valid}")
        
        board.move(move)


# Makes sure, that the game only runs when it is not being imported.
if __name__ == '__main__':
    main()
