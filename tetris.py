import pygame
import sys
from game import Game
from colors import Colors

pygame.init()

title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("GAME OVER", True, Colors.white)

score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)

dark_blue = (44, 44, 127)

screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption("python tetris")

clock = pygame.time.Clock()

game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)

pygame.key.set_repeat(100, 50)

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
                game.update_score(0, 1)
            if event.key == pygame.K_UP and game.game_over== False:
                game.rotate()
                pygame.key.set_repeat(5000, 5000)
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
    score_value_surface = title_font.render(str(game.score), True, Colors.white)

    screen.fill(Colors.dark_blue)
    screen.blit(score_surface, (365, 20, 50, 50))
    screen.blit(next_surface, (375, 180, 50, 50))

    if game.game_over == True:
        screen.blit(game_over_surface, (320, 450, 50, 50))
    
    pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx, centery = score_rect.centery))
    pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)

    game.draw(screen)

    pygame.display.update()
    clock.tick(60)
    