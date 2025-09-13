import pygame
import random

class Pipe:
    def __init__(self):
        self.image = pygame.image.load("images/flappy bird pipe.png")
        self.image = pygame.transform.scale(self.image,(200,500))
        self.image = self.image.subsurface(self.image.get_bounding_rect().inflate(0,-40))
        self.bottom_pipe = self.image.get_rect()
        self.bottom_pipe.x = 600
        self.pipe_height = random.randint(150,450)
        self.bottom_pipe.y = self.pipe_height
        self.clone = pygame.transform.flip(self.image,False,True)
        self.top_pipe = self.bottom_pipe.copy()
        self.top_pipe.y = (self.bottom_pipe.y - 600)
        self.pipe_count = 0
    
    def check_collide(self, bird):
        if bird.colliderect(self.bottom_pipe) or bird.colliderect(self.top_pipe):
            pygame.quit()

    def update(self, screen, bird):
        speed = 5
        self.check_collide(bird)
        #if the pipe is still on screen:
        if self.bottom_pipe.x >= -60:
            self.bottom_pipe.x -= 5
            self.top_pipe.x -= 5
        else:
           self.bottom_pipe.x = 600
           self.pipe_count += 1 
           self.bottom_pipe.y = random.randint(150,450)
           self.top_pipe.x = 600
           self.top_pipe.y = (self.bottom_pipe.y - 600)
        
        
        #else:
        # set the pipe x to the original x (600)
        # pick a new random height for the pipes
        
        screen.blit(self.image, self.bottom_pipe)
        screen.blit(self.clone, self.top_pipe)
    
