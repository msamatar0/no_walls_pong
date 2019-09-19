import sys, time, pygame
from random import randint
from pygame.locals import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#defines all game objects
class pong_ball(pygame.sprite.Sprite):
  def __init__(self, color, centerx, centery, radius):
    super().__init__()
    self.image = pygame.Surface([centerx, centery])
    self.image.fill(BLACK)
    self.image.set_colorkey(BLACK)
    pygame.draw.circle(self.image, color, [centerx, centery], radius)
    self.velocity = [randint(4,8),randint(-8,8)]
    self.rect = self.image.get_rect()
        
  def update(self):
    self.rect.x += self.velocity[0]
    self.rect.y += self.velocity[1]

  def bounce(self):
    self.velocity[0] = -self.velocity[0]
    self.velocity[1] = randint(-12,12)


class horz_paddle(pygame.sprite.Sprite):
  def __init__(self, color, width, height):
    super().__init__()
    self.image = pygame.Surface([width, height])
    self.image.fill(BLACK)
    self.image.set_colorkey(BLACK)
    pygame.draw.rect(self.image, color, [0, 0, width, height])
    self.rect = self.image.get_rect()
  
  def move_up(self, dy):
    self.rect.y -= dy
    if self.rect.y < 0:
      self.rect.y = 0

  def move_down(self, dy):
    self.rect.y += dy
    if self.rect.y > 576 - 170:
      self.rect.y = 576 - 170


class vert_paddle(pygame.sprite.Sprite):
  def __init__(self, color, width, height):
    super().__init__()
    self.image = pygame.Surface([width, height])
    self.image.fill(BLACK)
    self.image.set_colorkey(BLACK)
    pygame.draw.rect(self.image, color, [0, 0, width, height])
    self.rect = self.image.get_rect()
  
  def move_left(self, dx):
    self.rect.x -= dx
    if self.rect.x < 0:
      self.rect.x = 0

  def move_right(self, dx):
    self.rect.x += dx
    if self.rect.x > 342:
      self.rect.x = 342

class score_board():
  def __init__(self):
    self.score1 = 0
    self.score2 = 0
    self.font = pygame.font.Font(None, 20)

  def score_disp(self, window, x1, y1, x2, y2):
    self.text1 = self.font.render(str(self.score1), 1, WHITE)
    self.text2 = self.font.render(str(self.score2), 1, WHITE)
    window.blit(self.text1, (x1, y1))
    window.blit(self.text2, (x2, y2))