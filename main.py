import pygame, mySprites
import asyncio
import random

pygame.init()

def main():
    '''This function defines the 'mainline logic' for our game.'''  
    # Display
    screen = pygame.display.set_mode((640, 480))    
    pygame.display.set_caption("Using the mySprites library")
 	
    # Entities
    background = pygame.image.load("background.png")
    background = pygame.transform.scale(background, (640,480))
    cookie = mySprites.Cookie(screen)
    clock = pygame.time.Clock()
    keepGoing = True
    iteration = 0

    global Cookies
    Cookies = 0

    ClickingCookies = 1

    global AutoCookies
    AutoCookies = 0


    numCookiesLabel = mySprites.Label(str(Cookies), "Arial", (cookie.rect.centerx, (cookie.rect.centery - 125)), 25, (0,0,0))
    CookiesLabel = mySprites.Label("Cookies: ", "Arial", ((cookie.rect.centerx+5), (cookie.rect.centery - 160)), 25, (0,0,0))
    CpsLabel = mySprites.Label("Cookies per Second: " + str(AutoCookies), "Arial", (cookie.rect.centerx+10, (cookie.rect.centery + 150)), 20, (0,0,0))
    # Upgrade 1 Information (Mouse Upgrade)
    Upg1Num = 0
    Upg1Boost = 51
    Upg1 = mySprites.Label("Mouse Upgrade", "Arial", (540, 40), 20, (0,0,0))
    Upg1Count = mySprites.Label(str(Upg1Num), "Arial", (450, 50), 18, (0,0,0))
    Upg1CookieReq = 50
    Upg1Price = mySprites.Label(str(Upg1CookieReq), "Arial", (540, 60), 18, (0,0,0))

    # Upgrade 2 Information (Baker)
    Upg2Num = 0
    Upg2Boost = 251
    Upg2 = mySprites.Label("Baker", "Arial", (540, 90), 20, (0,0,0))
    Upg2Count = mySprites.Label(str(Upg2Num), "Arial", (450, 100), 18, (0,0,0))
    Upg2CookieReq = 250
    Upg2Price = mySprites.Label(str(Upg2CookieReq), "Arial", (540, 110), 18, (0,0,0))

    allSprites = pygame.sprite.OrderedUpdates(cookie, Upg2, Upg2Count, Upg2Price, CpsLabel, Upg1, Upg1Count, Upg1Price, CookiesLabel, numCookiesLabel)
 

    # Loop
    while keepGoing:
        # Time
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if cookie.rect.collidepoint(pygame.mouse.get_pos()):
                    Cookies += ClickingCookies
                if (Upg1.rect.collidepoint(pygame.mouse.get_pos()) or Upg1Price.rect.collidepoint(pygame.mouse.get_pos())) and Cookies >= Upg1CookieReq:
                    Cookies -= Upg1CookieReq
                    Upg1CookieReq += Upg1Boost
                    ClickingCookies += 1
                    AutoCookies += 1
                    Upg1Boost += random.choice([1,2,3])
                    Upg1Num += 1
                if (Upg2.rect.collidepoint(pygame.mouse.get_pos()) or Upg2Price.rect.collidepoint(pygame.mouse.get_pos())) and Cookies >= Upg2CookieReq:
                    Cookies -= Upg2CookieReq
                    Upg2CookieReq += Upg2Boost
                    AutoCookies += 10
                    Upg2Boost += random.choice([26,27,28,29,30,31])
                    Upg2Num += 1

        numCookiesLabel.setText(str(Cookies))
        CpsLabel.setText("Cookies per Second: " + str(AutoCookies))
        # Upgrade 1 Label Update
        Upg1Price.setText(str(Upg1CookieReq))
        Upg1Count.setText(str(Upg1Num))
        # Upgrade 2 Label Update
        Upg2Price.setText(str(Upg2CookieReq))
        Upg2Count.setText(str(Upg2Num))
        # Upgrade 3 Label Update
    
        pygame.display.flip()
        screen.blit(background, (0, 0))
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
        

        if iteration % 60 == 0 and iteration != 0:
            Cookies += AutoCookies
       
        iteration += 1
    # Close the game window
    pygame.quit()    
     	
# Call the main function
main()