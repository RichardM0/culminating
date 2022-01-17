import pygame
pygame.init()
def main():
    '''This function defines the 'mainline logic' for our game.'''  
    # Display
    screen = pygame.display.set_mode((640, 480))    
    pygame.display.set_caption("Using the mySprites library")
 	
    # Entities
    background = pygame.Surface(screen.get_size())
    background.fill((255, 255, 255))
    screen.blit(background, (0, 0))

    cookie = pygame.image.load("cookie.png")
    cookie = cookie.convert()
    pygame.transform.scale()

    clock = pygame.time.Clock()
    keepGoing = True
    # Loop
    while keepGoing:
        # Time
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False

    
        pygame.display.flip()
        screen.blit(cookie, (0, 0))
    # Close the game window
    pygame.quit()    
     	
# Call the main function
main()