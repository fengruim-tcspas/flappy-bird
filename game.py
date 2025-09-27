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
Font = pygame.font.SysFont("comicansms",25)

game_over = pygame.image.load("images/game_over.png")
game_over = pygame.transform.scale(game_over,(500,500))


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
end_game = False
while game == True:
    text = Font.render(f"Do you want to play? press s to play press w to quit", True, "white")
    screen.fill("black")
    screen.blit(background,background_rect)
    
    screen.blit(bird,bird_position)
    if green_pipe.check_collide(bird_position):
        end_game = True

    if end_game == False: 
        green_pipe.update(screen, bird_position) 

    if end_game == True:
        screen.blit(game_over, (0, 0))
        screen.blit(text,[5,50])
#screen.blit(pipe,pipe_rect)
    if bird_position.x >= green_pipe.bottom_pipe.x and green_pipe.pipe_count == score:
        score += 1


    
#ump()
# loop that checks all possible events in the game (keyboard input, quitting the window, expanding game window, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and end_game == False:
                isJumping = True
                velocity = 8
            

    if isJumping == True and end_game == False:
        jump()
                
    if not screen.get_rect().contains(bird_position):
        end_game = True

    clock.tick(30)
    text = Font.render(f"score: {score}", True, "Black")
    if end_game == False:
        screen.blit(text,[5,50])
    pygame.display.update()
     
       


        
    #if statement formula:
    #   if (variable) (comparison) (value)
    #       examples: if x < 4, if x == 3, if x > 2 ... 
    #  if screen.get_rect().contains(bird_position) (comparison) (value)
    

        
        