# A Small Coin Class just to group
# variables togehter
import pygame
import random

class Coin:
  
  def __init__(self):
    x = random.randint(0, 790)
    y = random.randint(0, 590)
    self.rect = pygame.Rect(x, y, 20, 20)
    self.isHidden = False
  
  
