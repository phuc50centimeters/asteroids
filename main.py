import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)


    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        # Update
        for object in updatable:
            if isinstance(object, Player):
                object.shot_cooldown -= dt

            object.update(dt)

        # Check collisions
        for asteroid in asteroids:
            # Check game over
            if asteroid.is_colliding(player):
                print("Game over!")
                sys.exit()

            # Check bullet
            for shot in shots:
                if shot.is_colliding(asteroid):
                    shot.kill()
                    asteroid.split()

        # Draw
        for object in drawable:
            object.draw(screen)

        pygame.display.flip()

        # Pause the game until 1/60th of a second has passed 
        # Make sure the game run at 60FPS
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()
