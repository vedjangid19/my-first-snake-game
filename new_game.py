import pygame,random

pygame.init()

#music add
def music_play(music_name):
    pygame.mixer.init()
    pygame.mixer.music.load(music_name)
    pygame.mixer.music.set_volume(0.9)
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()
#screen size
screen_height, screen_weidth = 500, 800

#color
white = (232,209,209)
red = (131,39,39)
bule = (178,102,255)
black =(0,0,0)

gamewindow = pygame.display.set_mode((screen_weidth, screen_height))

#text show on screen
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
def screen_text(score):
    textsurface = myfont.render(f"Score : {score}", False, (0, 0, 0))
    gamewindow.blit(textsurface,(0,0))

def plot_snake(gamewindow,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gamewindow,color,(x,y,snake_size,snake_size))





def gameloop():
    music_play("game.mp3")
    #snake_food
    food_x = random.randint(20,screen_weidth/2)
    food_y = random.randint(20,screen_height/2)
    #gameloop variable
    exit_game = False
    game_over = False
    snk_list = []
    snake_size = 10
    snake_x, snake_y = 50,50
    snk_length = 1
    init_velocity = 5
    velocity_x, velocity_y =0,0
    score = 0
    clock = pygame.time.Clock()
    fps = 30
    while not exit_game:
        
        if game_over :

            gamewindow.fill(white)
            textsurface = myfont.render("Game Over !", False, (0, 0, 0))
            gamewindow.blit(textsurface,(290,175))
            textsurface2 = myfont.render("Press Enter To Play ", False, (0, 0, 0))
            gamewindow.blit(textsurface2,(240,225))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_KP_ENTER:
                        gameloop()
        else:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        velocity_x, velocity_y = 0, -init_velocity
                    if event.key == pygame.K_DOWN:
                        velocity_x, velocity_y = 0, init_velocity
                    if event.key == pygame.K_LEFT:
                        velocity_x, velocity_y = -init_velocity, 0
                    if event.key == pygame.K_RIGHT:
                        velocity_x, velocity_y = init_velocity, 0
                    
        
            snake_x = snake_x + velocity_x 
            snake_y = snake_y + velocity_y
            if abs(snake_x - food_x) < 6 and abs(snake_y-food_y) < 6:
                score +=10
                #music_play("gameover.mp3")
                snk_length += 2
                food_x = random.randint(20,screen_weidth/2)
                food_y = random.randint(20,screen_height/2)
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            if len(snk_list)>snk_length:
                del snk_list[0]
            
            gamewindow.fill(white)
            screen_text(score)
            #pygame.draw.rect(gamewindow,black,(snake_x,snake_y,snake_size,snake_size))
            pygame.draw.rect(gamewindow,red,(food_x,food_y,snake_size,snake_size))
            
            if snake_x < 0 or snake_x > screen_weidth-10 or snake_y < 0 or snake_y >screen_height-10 :
                music_play("gameover.mp3")
                gamewindow.fill(white)
                textsurface = myfont.render("Game Over !", False, (0, 0, 0))
                gamewindow.blit(textsurface,(290,175))
                textsurface2 = myfont.render("Press Enter To Play ", False, (0, 0, 0))
                gamewindow.blit(textsurface2,(240,225))
                stop_music()
            
            if head in snk_list[:-1]:
                music_play("gameover.mp3")
                game_over = True
            plot_snake(gamewindow,black,snk_list,snake_size)
            
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
gameloop()