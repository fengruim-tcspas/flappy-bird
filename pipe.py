import pygame
import random

class Pipe:
    def __init__(self):
        self.image = pygame.image.load("images/flappy bird pipe.png")
        self.image = pygame.transform.scale(self.image,(200,500))
        self.image = self.image.subsurface(self.image.get_bounding_rect())
        self.collision = self.image.get_rect()
        self.collision.x = 200
        self.collision.y = 200
        self.clone = pygame.transform.flip(self.image,False,True)
        self.clone_collision = self.collision.copy()
        self.clone_collision.y = (self.collision.y - 100)
    def update(self, screen):
        speed = 5
        self.collision.x -= 5
        screen.blit(self.image, self.collision)
        self.clone_collision.x -= 5
        screen.blit(self.clone, self.clone_collision)
    
    
        
