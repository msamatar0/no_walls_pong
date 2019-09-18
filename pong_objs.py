import pygame
from random import randint
from pygame.locals import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#defining all game objects
class pong_ball(pygame.sprite.Sprite):

  def __init__(self, color, center, radius):
    super().__init__()
    self.image = pygame.Surface([center, radius])
    self.image.fill(BLACK)
    self.image.set_colorkey(BLACK)
    pygame.draw.circle(self.image, color, [0, 0, center, radius])
    self.velocity = [randint(4,8),randint(-8,8)]
    self.circle = self.image.get_circle()
        
  def update(self):
    self.rect.x += self.velocity[0]
    self.rect.y += self.velocity[1] 

    

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


class ball(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        # Draw the ball (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        self.velocity = [randint(4,8),randint(-8,8)]
        
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
