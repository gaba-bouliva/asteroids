import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    py_time = pygame.time.Clock()
    dt = 0.3


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 )
    asteroid_field = AsteroidField()
    


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dt = pygame.time.Clock().tick(60) / 1000
                return

        screen.fill(BLACK)
        Player.screen = screen
        updatable_player_index = Player.containers.index(updatable)
        drawable_player_index = Player.containers.index(drawable)
        asteroids_group_index = Asteroid.containers.index(asteroids)
        shots_group_index = Shot.containers.index(shots)

        for updatable_player in Player.containers[updatable_player_index]:
            updatable_player.update(dt)
            for asteroid in Asteroid.containers[asteroids_group_index]:
                for shot in Shot.containers[shots_group_index]:
                    if shot.check_collision(asteroid):
                        shot.kill()
                        asteroid.split()
                if asteroid.check_collision(player):
                    print("Game over!")
                    sys.exit(0)
                
        for drawable_player in Player.containers[drawable_player_index]:
            drawable_player.draw(screen)
        

        pygame.display.flip()



if __name__ == "__main__":
    main()
