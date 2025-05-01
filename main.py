# probably done with this for now.

import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    font = pygame.font.Font(None, 36)

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatables, drawables)
    Asteroid.containers = (updatables, drawables, asteroids)
    AsteroidField.containers = (updatables)
    Shot.containers = (updatables, drawables, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()
    
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        
        for drawable in drawables:
            drawable.draw(screen)

        updatables.update(dt)

        for asteroid in asteroids:
            if asteroid.collision(player):
                sys.exit(f"Game over! Score: {player.score}")
            for shot in shots:
                if asteroid.collision(shot):
                    shot.kill()
                    asteroid.split()
                    player.update_score(asteroid.radius)

        score_text = font.render(f"Score: {player.score}", True, "white")
        screen.blit(score_text, (SCREEN_WIDTH - score_text.get_width() - 10, 10))    

        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()