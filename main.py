from constants import *
from player import *
import pygame

def main():
    pygame.init()
    Clock = pygame.time.Clock
    dt = 0
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    # Create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # Assign groups to Player class
    Player.containers = (updatable, drawable)

    # Create player (added automatically to groups)
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill(color="black")
        

        # Update all updatable sprites
        updatable.update(dt)

        # Draw all drawable sprites
        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()
        
        Clock().tick(60)
        dt = Clock().tick(60) / 1000
        
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()