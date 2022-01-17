import pygame

class Cookie(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("cookie.png")
        self.image = self.image.convert()
        self.image = pygame.transform.scale(self.image, (200, 200))
        white = (255, 255, 255)
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.rect.centerx = 125
        self.rect.centery = screen.get_height()/2

#--------------------------------------------------------------------------------------------------------

class Label(pygame.sprite.Sprite):
    '''An mutatable text Label Sprite subclass'''
    def __init__(self, message, font_name, x_y_center, size, rgb):
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont(font_name, size)
        self.text = message
        self.center = x_y_center
        self.rgb = rgb
     	
    def setText(self, message):
        '''Mutator for text to be displayed on the label.'''
        self.text = message
             	
    def update(self):
        '''Render and center the label text on each Refresh.'''
        self.image = self.font.render(self.text, 1, (self.rgb))
        self.rect = self.image.get_rect()
        self.rect.center = self.center

#--------------------------------------------------------------------------------------------------------

