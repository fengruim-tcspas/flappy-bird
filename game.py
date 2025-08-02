import pygame

print (pygame.ver)

#see this change
screen = pygame.display.set_mode((500, 500))
# lets me color the screen
#screen.fill("black")

bird = pygame.image.load("images/flappy-bird.png")
bird = pygame.transform.scale(bird,(80,80))
bird_rect = bird.get_rect()
bird_rect.x = 200
bird_rect.y = 200
bird_position = bird.get_rect(topleft = [0,255])


pipe = pygame.image.load("images/flappy bird pipe.png")
pipe = pygame.transform.scale(pipe,(100,300))
pipe_rect = pipe.get_rect()
pipe_rect.x = 100
pipe_rect.y = 300

background = pygame.image.load("images/flappy bird background.jpg")
background = pygame.transform.scale(background,(500,500))
background_rect = background.get_rect()
background_rect.x = 0
background_rect.y = 0
velocity = 8
def jump():
    global velocity
    bird_rect.y -= velocity
    velocity -= 1

clock = pygame.time.Clock()
isJumping = False
while True:
    screen.fill("black")
    screen.blit(background,background_rect)
    screen.blit(bird,bird_rect)
    screen.blit(pipe,pipe_rect)
     
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
        
    if screen.get_rect().contains(bird.get_rect().y) == False:
        pygame.quit()
    
        

    clock.tick(30)
    pygame.display.update()
    
    variable = 5
    #if statement formula:
    #   if (variable) (comparison) (value)
    #       examples: if x < 4, if x == 3, if x > 2 ... 
    #  if screen.get_rect().contains(bird_position) (comparison) (value)
    

        
        