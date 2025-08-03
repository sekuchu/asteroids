from constants import *
import pygame

def main():
    pygame.init()
    Clock = pygame.time.Clock
    dt = 0
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill(color="black")
        pygame.display.flip()
        
        Clock().tick(60)
        dt = Clock().tick(60) / 1000
        
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()