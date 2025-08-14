import pygame
from constants import *
from player import Player

def main():
    
    print('Starting Asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True
    clock = pygame.time.Clock()
    dt = 0

    updateables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    Player.containers = (updateables, drawables)
    
    ship = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        updateables.update(dt)

        screen.fill('black')

        for thing in drawables:
            thing.draw(screen)
        
        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == '__main__':
    main()