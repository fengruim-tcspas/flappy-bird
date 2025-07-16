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
velocity = 50
def jump():
    global velocity
    bird_rect.y -= velocity
    velocity -= 1

clock = pygame.time.Clock()
while True:
    screen.fill("black")
    screen.blit(background,background_rect)
    screen.blit(bird,bird_rect)
    screen.blit(pipe,pipe_rect)
    
    jump()
    # loop that checks all possible events in the game (keyboard input, quitting the window, expanding game window, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    clock.tick(30)
    pygame.display.update()
        