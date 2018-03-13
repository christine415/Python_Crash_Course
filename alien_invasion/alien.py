import pygame

class Alien():
    '''Initialize alien and set its initial position'''
    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load("images/cyclop_alien.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
    
    def blitme(self):
        '''Draw the alien at its current position'''
        self.screen.blit(self.image, self.rect)