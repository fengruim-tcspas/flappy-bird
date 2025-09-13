import pygame
from pipe import Pipe

pygame.init()
print (pygame.ver)
score = 0
playing = True
game = True

#see this change
screen = pygame.display.set_mode((500, 500))
# lets me color the screen
#screen.fill("black")

bird = pygame.image.load("images/flappy-bird.png")
bird = pygame.transform.smoothscale(bird,(80,80))
bird_rect = bird.subsurface(bird.get_bounding_rect().inflate(-30, -30))
#bird_rect.x = 200
#bird_rect.y = 200 
bird_position = bird.get_rect(topleft = [0,255])
Font = pygame.font.SysFont("comicansms",30)


#pipe = pygame.image.load("images/flappy bird pipe.png")
#pipe = pygame.transform.scale(pipe,(100,300))
#pipe_rect = pipe.get_rect()
#pipe_rect.x = 100
#pipe_rect.y = 300

background = pygame.image.load("images/flappy bird background.jpg")
background = pygame.transform.scale(background,(500,500))
background_rect = background.get_rect()
background_rect.x = 0
background_rect.y = 0
velocity = 8

green_pipe = Pipe()

def jump():
    global velocity
    #bird_rect.y -= velocity 
    bird_position.y -=velocity
    velocity -= 1

clock = pygame.time.Clock()
isJumping = False
while game == True:
    screen.blit(background,background_rect)
    text = Font.render(f"Do you want to play? press s to play press w to quit", True, "Black")
    screen.blit(text,[5,50])
    while playing == True:
        screen.fill("black")
        screen.blit(background,background_rect)
        screen.blit(bird,bird_position) 
        green_pipe.update(screen, bird_position)
    #screen.blit(pipe,pipe_rect)
        if bird_position.x >= green_pipe.bottom_pipe.x and green_pipe.pipe_count == score:
            score += 1
    
    
     
    #ump()
    # loop that checks all possible events in the game (keyboard input, quitting the window, expanding game window, etc.)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                
                    isJumping = True
                    velocity = 8
                
    
        if isJumping == True:
            jump()
                    
        if not screen.get_rect().contains(bird_position):
            playing = False
        clock.tick(30)
        text = Font.render(f"score: {score}", True, "Black")
        screen.blit(text,[5,50])
        pygame.display.update()
     
        variable = 5
    #if statement formula:
    #   if (variable) (comparison) (value)
    #       examples: if x < 4, if x == 3, if x > 2 ... 
    #  if screen.get_rect().contains(bird_position) (comparison) (value)
    

        
        