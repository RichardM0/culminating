import pygame, mySprites
import asyncio
import random
# cookie clicker
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
    Cookies = 1000000

    ClickingCookies = 1

    global AutoCookies
    AutoCookies = 0
    plusNum = 1

    numCookiesLabel = mySprites.Label(str(Cookies), "Arial", (cookie.rect.centerx, (cookie.rect.centery - 125)), 25, (0,0,0))
    CookiesLabel = mySprites.Label("Cookies: ", "Arial", ((cookie.rect.centerx+5), (cookie.rect.centery - 160)), 25, (0,0,0))
    CpsLabel = mySprites.Label("Cookies per Second: " + str(AutoCookies), "Arial", (cookie.rect.centerx, (cookie.rect.centery + 150)), 20, (0,0,0))
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

    # Upgrade 3 Information (Milk Stand)
    Upg3Num = 0
    Upg3Boost = 1502
    Upg3 = mySprites.Label("Milk Stand", "Arial", (540, 140), 20, (0,0,0))
    Upg3Count = mySprites.Label(str(Upg3Num), "Arial", (450, 150), 18, (0,0,0))
    Upg3CookieReq = 1500
    Upg3Price = mySprites.Label(str(Upg3CookieReq), "Arial", (540, 160), 18, (0,0,0))

    # Upgrade 4 Information (Milk Stand)
    Upg4Num = 0
    Upg4Boost = 12504
    Upg4 = mySprites.Label("Cookie Farm", "Arial", (540, 190), 20, (0,0,0))
    Upg4Count = mySprites.Label(str(Upg4Num), "Arial", (450, 200), 18, (0,0,0))
    Upg4CookieReq = 12500
    Upg4Price = mySprites.Label(str(Upg4CookieReq), "Arial", (540, 210), 18, (0,0,0))

    Upg5Num = 0
    Upg5Boost = 25004
    Upg5 = mySprites.Label("Cookie Factory", "Arial", (540, 240), 20, (0,0,0))
    Upg5Count = mySprites.Label(str(Upg5Num), "Arial", (450, 250), 18, (0,0,0))
    Upg5CookieReq = 25000
    Upg5Price = mySprites.Label(str(Upg5CookieReq), "Arial", (540, 260), 18, (0,0,0))

    Upg6Num = 0
    Upg6Boost = 100004
    Upg6 = mySprites.Label("Cookie Sanctuary", "Arial", (540, 290), 20, (0,0,0))
    Upg6Count = mySprites.Label(str(Upg6Num), "Arial", (450, 300), 18, (0,0,0))
    Upg6CookieReq = 100000
    Upg6Price = mySprites.Label(str(Upg6CookieReq), "Arial", (540, 310), 18, (0,0,0))

    Multi1 = mySprites.Label("x1", "Arial", (440, 440), 20, (0,0,0))
    Multi10 = mySprites.Label("x10", "Arial", (480, 440), 20, (0,0,0))
    Multi25 = mySprites.Label("x25", "Arial", (520, 440), 20, (0,0,0))
    Multi100 = mySprites.Label("x100", "Arial", (570, 440), 20, (0,0,0))

    allSprites = pygame.sprite.OrderedUpdates(cookie, Upg6, Upg6Count, Upg6Price, Upg5, Upg5Count, Upg5Price, Upg4, Upg4Count, Upg4Price, Upg3, Upg3Count, Upg3Price, Upg2, Upg2Count, Upg2Price, CpsLabel, Upg1, Upg1Count, Upg1Price, CookiesLabel, numCookiesLabel, Multi1, Multi10, Multi25, Multi100)
 

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
                if (Upg1.rect.collidepoint(pygame.mouse.get_pos()) or Upg1Price.rect.collidepoint(pygame.mouse.get_pos())) and Cookies >= Upg1CookieReq * plusNum:
                    Cookies -= Upg1CookieReq*plusNum
                    Upg1CookieReq += Upg1Boost*plusNum
                    ClickingCookies += 1*plusNum
                    AutoCookies += 1*plusNum
                    Upg1Boost += random.choice([1,2,3])*plusNum
                    Upg1Num += plusNum
                if (Upg2.rect.collidepoint(pygame.mouse.get_pos()) or Upg2Price.rect.collidepoint(pygame.mouse.get_pos())) and Cookies >= Upg2CookieReq * plusNum:
                    Cookies -= Upg2CookieReq*plusNum
                    Upg2CookieReq += Upg2Boost*plusNum
                    AutoCookies += 10*plusNum
                    Upg2Boost += random.choice([26,27,28,29,30,31])*plusNum
                    Upg2Num += plusNum
                if (Upg3.rect.collidepoint(pygame.mouse.get_pos()) or Upg3Price.rect.collidepoint(pygame.mouse.get_pos())) and Cookies >= Upg3CookieReq * plusNum:
                    Cookies -= Upg3CookieReq*plusNum
                    Upg3CookieReq += Upg3Boost*plusNum
                    AutoCookies += 50*plusNum
                    Upg3Boost += random.choice([100,101,102,103,104])*plusNum
                    Upg3Num += plusNum
                if (Upg4.rect.collidepoint(pygame.mouse.get_pos()) or Upg4Price.rect.collidepoint(pygame.mouse.get_pos())) and Cookies >= Upg4CookieReq * plusNum:
                    Cookies -= Upg4CookieReq*plusNum
                    Upg4CookieReq += Upg4Boost*plusNum
                    AutoCookies += 200*plusNum
                    Upg4Boost += random.choice([500,501,502,503,504])*plusNum
                    Upg4Num += plusNum
                if (Upg5.rect.collidepoint(pygame.mouse.get_pos()) or Upg5Price.rect.collidepoint(pygame.mouse.get_pos())) and Cookies >= Upg5CookieReq * plusNum:
                    Cookies -= Upg5CookieReq*plusNum
                    Upg5CookieReq += Upg5Boost*plusNum
                    AutoCookies += 750*plusNum
                    Upg5Boost += random.choice([900,901,902,903,904])*plusNum
                    Upg5Num += plusNum
                if (Upg6.rect.collidepoint(pygame.mouse.get_pos()) or Upg6Price.rect.collidepoint(pygame.mouse.get_pos())) and Cookies >= Upg6CookieReq * plusNum:
                    Cookies -= Upg6CookieReq*plusNum
                    Upg6CookieReq += Upg6Boost*plusNum
                    AutoCookies += 1800*plusNum
                    Upg6Boost += random.choice([1400,1401,1402,1403,1404])*plusNum
                    Upg6Num += plusNum
                if Multi1.rect.collidepoint(pygame.mouse.get_pos()):
                    plusNum = 1
                if Multi10.rect.collidepoint(pygame.mouse.get_pos()):
                    plusNum = 10
                if Multi25.rect.collidepoint(pygame.mouse.get_pos()):
                    plusNum = 25
                if Multi100.rect.collidepoint(pygame.mouse.get_pos()):
                    plusNum = 100
                  


        numCookiesLabel.setText(str(Cookies))
        CpsLabel.setText("Cookies per Second: " + str(AutoCookies))
        # Upgrade 1 Label Update
        Upg1Price.setText(str(Upg1CookieReq))
        Upg1Count.setText(str(Upg1Num))
        # Upgrade 2 Label Update
        Upg2Price.setText(str(Upg2CookieReq))
        Upg2Count.setText(str(Upg2Num))
        # Upgrade 3 Label Update
        Upg3Price.setText(str(Upg3CookieReq))
        Upg3Count.setText(str(Upg3Num))
        # Upgrade 4 Label Update
        Upg4Price.setText(str(Upg4CookieReq))
        Upg4Count.setText(str(Upg4Num))
        # Upgrade 5 Label Update
        Upg5Price.setText(str(Upg5CookieReq))
        Upg5Count.setText(str(Upg5Num))
        # Upgrade 6 Label Update
        Upg6Price.setText(str(Upg6CookieReq))
        Upg6Count.setText(str(Upg6Num))
    
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