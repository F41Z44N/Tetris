import pygame
import sys
from game import Game


pygame.init()
dark_blue = (44, 44, 127)

screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("python tetris")

clock = pygame.time.Clock()

game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 300)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game.game_over == True:
                game.game_over = False
                game.reset()
            if event.key == pygame.K_LEFT and game.game_over== False:
                game.move_left()
                game.move_left_shadow()
            if event.key == pygame.K_RIGHT and game.game_over== False:
                game.move_right()
                game.move_right_shadow()
            if event.key ==pygame.K_DOWN and game.game_over== False:
                game.move_down()
            if event.key == pygame.K_UP and game.game_over== False:
                game.rotate()
            if event.key == pygame.K_SPACE and game.game_over== False:
                while True:
                    game.current_block.move(1, 0)
                    if not game.block_inside() or not game.block_fits():
                        game.current_block.move(-1, 0)
                        game.lock_block()
                        break
        if event.type == GAME_UPDATE and game.game_over== False:
            game.move_down()
            game.move_down_shadow()

    # drawing
    screen.fill(dark_blue)
    game.draw(screen)

    pygame.display.update()
    clock.tick(60)
    