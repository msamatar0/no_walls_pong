import sys, time, pygame
from pygame.locals import *
from pong_objs import *

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
window_width = 1024
window_height = 576

window = pygame.display.set_mode((window_width, window_height), 0, 32)
pygame.display.set_caption('Pong But With More Paddles Instead Of Walls')

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

def_font = pygame.font.SysFont(None, 48)

player_paddle = horz_paddle(WHITE, 10, 170)
ai_paddle = horz_paddle(WHITE, 10, 170)
player_paddle.rect.x = 20
player_paddle.rect.y = 210
ai_paddle.rect.x = window_width - 30
ai_paddle.rect.y = 210

ball = pong_ball(WHITE,10,10)
ball.rect.x = 345
ball.rect.y = 195

sprites = pygame.sprite.Group()
sprites.add(player_paddle)
sprites.add(ai_paddle)
sprites.add(ball)

#start game
running = True

clock = pygame.time.Clock()

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  #key pressess
  keys = pygame.key.get_pressed()
  if keys[pygame.K_UP]:
    player_paddle.move_up(5)
  if keys[pygame.K_DOWN]:
    player_paddle.move_down(5)

  #game logic
  sprites.update()



  #drawing objs
  window.fill(BLACK)
  pygame.draw.line(window, WHITE, [window_width / 2, 0], [window_width / 2, window_height], 2)
  sprites.draw(window)


  #update screen after drawing
  pygame.display.update()
  clock.tick(60)

pygame.quit()