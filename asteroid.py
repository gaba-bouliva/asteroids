import pygame
from circleshape import CircleShape
from constants import *
import random


class Asteroid(CircleShape):
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
    
  def split(self):
    self.kill()
    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    else:
      print("splitting large asteroids")
      random_angle = random.uniform(20, 50)

      velocity_1 = self.velocity.rotate(random_angle)
      velocity_2 = self.velocity.rotate(-random_angle)

      new_radius = self.radius - ASTEROID_MIN_RADIUS

      child_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
      child_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)

      child_asteroid_1.velocity = velocity_1 * 1.2
      child_asteroid_2.velocity = velocity_2 * 1.2

      # Asteroid.containers[0].add(child_asteroid_1)
      # Asteroid.containers[0].add(child_asteroid_2)
