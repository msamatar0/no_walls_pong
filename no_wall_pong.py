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

player_paddle_side = horz_paddle(WHITE, 10, 170)
player_paddle_top = vert_paddle(WHITE, 170, 10)
player_paddle_bottom = vert_paddle(WHITE, 170, 10)

ai_paddle_side = horz_paddle(WHITE, 10, 170)
ai_paddle_top = vert_paddle(WHITE, 170, 10)
ai_paddle_bottom = vert_paddle(WHITE, 170, 10)

player_paddle_side.rect.x = 20
player_paddle_side.rect.y = 210

player_paddle_top.rect.x = 196
player_paddle_top.rect.y = 20

player_paddle_bottom.rect.x = 196
player_paddle_bottom.rect.y = 546

ai_paddle_side.rect.x = 994
ai_paddle_side.rect.y = 210

ai_paddle_top.rect.x = 708
ai_paddle_top.rect.y = 20

ai_paddle_bottom.rect.x = 708
ai_paddle_bottom.rect.y = 546

ball = pong_ball(WHITE, 512, 288, 6)

#builds a list of all sprites for updating
sprites = pygame.sprite.Group()
sprites.add(player_paddle_side)
sprites.add(ai_paddle_side)
sprites.add(player_paddle_top)
sprites.add(ai_paddle_top)
sprites.add(player_paddle_bottom)
sprites.add(ai_paddle_bottom)
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
    player_paddle_side.move_up(5)
  if keys[pygame.K_DOWN]:
    player_paddle_side.move_down(5)
  if keys[pygame.K_LEFT]:
    player_paddle_top.move_left(5)
    player_paddle_bottom.move_left(5)
  if keys[pygame.K_RIGHT]:
    player_paddle_top.move_right(5)
    player_paddle_bottom.move_right(5)

  #ai does its best to keep up with the ball
  ai_paddle_side.rect.y = ball.rect.y + 70
  if ai_paddle_side.rect.y < 0:
    ai_paddle_side.rect.y = 0
  if ai_paddle_side.rect.y > 576 - 170:
    ai_paddle_side.rect.y = 576 - 170

  ai_paddle_top.rect.x = ball.rect.x + 100
  ai_paddle_bottom.rect.x = ball.rect.x + 100
  if ball.rect.x < 576:
    ai_paddle_top.rect.x = 576
    ai_paddle_bottom.rect.x = 576
  if ai_paddle_top.rect.x < 576:
    ai_paddle_top.rect.x = 576
    ai_paddle_bottom.rect.x = 576
  if ai_paddle_top.rect.x > 1024 - 170:
    ai_paddle_top.rect.x = 1024 - 170
    ai_paddle_bottom.rect.x = 1024 - 170
  #game logic
  sprites.update()
  
  if (pygame.sprite.collide_mask(ball, player_paddle_side) or 
    pygame.sprite.collide_mask(ball, ai_paddle_side) or 
    pygame.sprite.collide_mask(ball, player_paddle_top) or  
    pygame.sprite.collide_mask(ball, ai_paddle_top) or 
    pygame.sprite.collide_mask(ball, player_paddle_bottom) or 
    pygame.sprite.collide_mask(ball, ai_paddle_bottom)):
      ball.bounce()

  #drawing objs
  window.fill(BLACK)
  pygame.draw.line(window, WHITE, [window_width / 2, 0], [window_width / 2, window_height], 2)
  sprites.draw(window)


  #update screen after drawing
  pygame.display.update()
  clock.tick(60)

pygame.quit()