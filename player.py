import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
  def __init__(self, x, y):
    self.x = x
    self.y = y
    super().__init__(self.x, self.y, PLAYER_RADIUS)
    self.rotation = 1
    self.shot_timer = 0
  
  def triangle(self):
    forward = pygame.Vector2(0, 1).rotate(self.rotation)
    right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
    a = self.position + forward * self.radius
    b = self.position - forward * self.radius - right
    c = self.position - forward * self.radius + right
    return [a, b, c]
  
  def draw(self, screen):
    pygame.draw.polygon(screen, WHITE, self.triangle(), 2)
  
  def rotate(self, dt):
    self.rotation = PLAYER_TURN_SPEED * dt
  
  def update(self, dt):
    keys = pygame.key.get_pressed()
    self.shot_timer -= dt
    if keys[pygame.K_a]:
      self.rotate(-dt)
    if keys[pygame.K_d]:
      self.rotate(dt)
    if keys[pygame.K_w]:
      self.move(dt)
    if keys[pygame.K_s]:
      self.move(-dt)
    if keys[pygame.K_SPACE]:
      if self.shot_timer <= 0:
        self.shoot()
        self.shot_timer = PLAYER_SHOOT_COOLDOWN
    
  def move(self, dt):
    forward = pygame.Vector2(0, 1).rotate(self.rotation)
    self.position += forward * PLAYER_SPEED * dt

    if self.position.x > Player.screen.get_width():
      self.positionx = 0
    elif self.position.x < 0:
      self.position.x = Player.screen.get_width()
    
    if self.position.y > Player.screen.get_height():
      self.position.y = 0
    elif self.position.y < 0:
      self.position.y = Player.screen.get_height()

  
  def shoot(self):
    shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
    velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
    shot.velocity = velocity