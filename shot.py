import pygame
from circleshape import CircleShape
from constants import *


class Shot(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)
  
  def draw(self, screen):
    pygame.draw.circle(screen, WHITE, (self.position.x, self.position.y), self.radius, 2)
  
  def update(self, dt):
    self.position += (self.velocity * dt)
    if (self.position.x < -self.radius or 
        self.position.x > SCREEN_WIDTH + self.radius or
        self.position.y < -self.radius or 
        self.position.y > SCREEN_HEIGHT + self.radius):
        self.kill() 