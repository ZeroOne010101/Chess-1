import os

import pygame

from src.board import *

logging.getLogger().setLevel(logging.DEBUG)

main_logger = logging.getLogger('main')
main_logger.setLevel(logging.DEBUG)


def main():
    """
    The loop the game runs in.
    It takes a user input, checks that input for validity, and calls move on it if it is valid.
    It terminates once the game is won or a player quits the game.
    """
    image_directory = os.path.join(os.getcwd(), 'Pieces')
    print(image_directory)
    
    window_size = 512, 512
    length_of_unit_square = int(window_size[0] / 8)
    framerate = 100
    
    pygame.init()
    pygame.display.set_caption('Chess')
    clock = pygame.time.Clock()
    
    screen = pygame.display.set_mode(window_size)

    # font = pygame.font.SysFont('Arial', 20)

    pieces = {
        'Black': {
            '♗': pygame.image.load(os.path.join(image_directory, 'black_b.png')),  # Black Bishop
            '♔': pygame.image.load(os.path.join(image_directory, 'black_k.png')).convert(),  # Black King
            '♘': pygame.image.load(os.path.join(image_directory, 'black_n.png')).convert(),  # Black Knight
            '♙': pygame.image.load(os.path.join(image_directory, 'black_p.png')).convert(),  # Black Pawn
            '♕': pygame.image.load(os.path.join(image_directory, 'black_q.png')).convert(),  # Black Queen
            '♖': pygame.image.load(os.path.join(image_directory, 'black_r.png')).convert(),  # Black Rook
            },
    
        'White': {
            '♝': pygame.image.load(os.path.join(image_directory, 'white_b.png')).convert(),  # White Bishop
            '♚': pygame.image.load(os.path.join(image_directory, 'white_k.png')).convert(),  # White King
            '♞': pygame.image.load(os.path.join(image_directory, 'white_n.png')).convert(),  # White Knight
            '♟': pygame.image.load(os.path.join(image_directory, 'white_p.png')).convert(),  # White Pawn
            '♛': pygame.image.load(os.path.join(image_directory, 'white_q.png')).convert(),  # White Queen
            '♜': pygame.image.load(os.path.join(image_directory, 'white_r.png')).convert(),  # White Rook
            }
        }
    
    colors = {
        'White': [255, 255, 255],
        'Grey': [100, 100, 100],
        'Black': [0, 0, 0]
        }
    screen.fill(colors['Black'])
    board = Board()

    def checkerboard():
        logging.info('Setting up GUI-Checkerboard')
        for row in board.game_board:
            for square in row:
                if square.row % 2 == 0:
                    if square.column % 2 == 0:
                        pygame.draw.rect(screen, colors['White'], pygame.Rect(square.row * length_of_unit_square + .5,
                                                                              square.column * length_of_unit_square + .5,
                                                                              length_of_unit_square - 1,
                                                                              length_of_unit_square - 1))
                    else:
                        pygame.draw.rect(screen, colors['Grey'], pygame.Rect(square.row * length_of_unit_square + .5,
                                                                             square.column * length_of_unit_square + .5,
                                                                             length_of_unit_square - 1,
                                                                             length_of_unit_square - 1))
                else:
                    if square.column % 2 == 1:
                        pygame.draw.rect(screen, colors['White'], pygame.Rect(square.row * length_of_unit_square + .5,
                                                                              square.column * length_of_unit_square + .5,
                                                                              length_of_unit_square - 1,
                                                                              length_of_unit_square - 1))
                    else:
                        pygame.draw.rect(screen, colors['Grey'], pygame.Rect(square.row * length_of_unit_square + .5,
                                                                             square.column * length_of_unit_square + .5,
                                                                             length_of_unit_square - 1,
                                                                             length_of_unit_square - 1))
    
    def place_pieces():
        logging.info('Setting up GUI-Pieces')
        for row in board.game_board:
            for square in row:
                if square.piece == '☐':
                    image = pieces[square.color][square.piece]
                    screen.blit(image, [square.row * length_of_unit_square, square.column * length_of_unit_square])
    
    while True:  # Main loop
        clock.tick(framerate)
        print(board)

        checkerboard()  # Places the checkerboard pattern in the screen
        place_pieces()  # Places images of the pieces
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
