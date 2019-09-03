from src.board import *

import logging
import pygame


# logging.getLogger().setLevel(logging.DEBUG)

# main_logger = logging.getLogger('main')
# main_logger.setLevel(logging.DEBUG)

def main():
    """
    The loop the game runs in.
    It takes a user input, checks that input for validity, and calls move on it if it is valid.
    It terminates once the game is won or a player quits the game.
    """
    
    window_size = 256, 256
    length_of_unit_square = int(window_size[0] / 8) - 2
    
    pygame.init()
    pygame.display.set_caption('Chess')
    screen = pygame.display.set_mode(window_size)
    
    font = pygame.font.SysFont('Arial', 20)
    
    colors = {
        'White': [255, 255, 255],
        'Black': [0, 0, 0]
        }
    screen.fill(colors['Black'])
    board = Board()
    
    def checkerboard():
        for row in board.game_board:
            for square in row:
                if square.row % 2 == 0:
                    if square.column % 2 == 0:
                        pygame.draw.rect(screen, colors['White'], pygame.Rect(square.row * length_of_unit_square,
                                                                              square.column * length_of_unit_square,
                                                                              length_of_unit_square,
                                                                              length_of_unit_square))
                    else:
                        pass
                else:
                    if square.column % 2 == 1:
                        pygame.draw.rect(screen, colors['White'], pygame.Rect(square.row * length_of_unit_square,
                                                                              square.column * length_of_unit_square,
                                                                              length_of_unit_square,
                                                                              length_of_unit_square))
                    else:
                        pass
    
    while True:
        print(board)
        
        checkerboard()
        pygame.display.flip()
        
        move_valid = False  # makes the input loop run at least once
        move = None
        while not move_valid:
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
