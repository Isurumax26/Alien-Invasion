import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self,ai_settings,screen,ship):
        """Create a bullet object at the ship's current position"""
        super().__init__()
        self.screen =screen

        #create a bullet rect at (0,0) and the set current position
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height) # bullet is not build from the images so we have to bulid it from the scratch
        self.rect.centerx = ship.rect.centerx
        self.rect.top  = ship.rect.top

        #store the bullet's position as a decimal value
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor


    def update(self):
        """Move the bullet up the screen"""
        # update the decimal point the bullet
        self.y -= self.speed_factor
        # update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)