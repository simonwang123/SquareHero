import pygame
from random import randint
import time

# Initialize pygame and store colors that will be used into variables
pygame.init()
red = (255,0,0)
black = (0,0,0)
white = (255,255, 255)

# Store images, sound and fonts to be used into variables. Set volume, create Screen object for GUI canvas and clock object for FPS.
saitama = pygame.image.load('images\\saitama.png')
rotatedsaitama = pygame.transform.rotate(saitama, 180)
icon = pygame.image.load('images\\icon.png')
introbg = pygame.image.load('images\\openbg.jpg')
sound = pygame.mixer.Sound('sounds\\opentrack.wav')
sound.set_volume(0.3)
crashsound = pygame.mixer.Sound('sounds\\crash.wav')
Screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Square Hero')
pygame.display.set_icon(icon)
font1 = pygame.font.Font("fonts\\aldhabi.ttf", 70)
font2 = pygame.font.Font("fonts\\aldhabi.ttf", 40)
clock = pygame.time.Clock()


# Enter the INTRODUCTION LOOP when called. If the player presses the space key, end loop and enter GAME LOOP. 
def gameIntro():
    GameStart = False
    sound.play(loops = -1)
    while GameStart == False:
        for event in pygame.event.get():
            Screen.blit(introbg,(0,0,800,600))    
            text = font1.render("Press Space key to be a hero.", True, white)
            Screen.blit(text, [150,490])
            pygame.display.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    GameStart = True
                    sound.stop()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
# Enter the GAME LOOP when called.
def gameLoop():

# Print the head of Saitama on the screen when called. After 30 points, print an upside-down head instead.
    def head():
        if points < 30:
            Screen.blit(saitama, (200,(headPosition),49,60))
        else:
            Screen.blit(rotatedsaitama,(200,(headPosition),49,60))

# Print an rectangular obstacle when called. The starting y position and height of the bottom block is dependent on the height of the first block. At 30 points thereafter, blocks will turn white.            
    def obstacle1(xloc1, yloc, xsize, ysize1):
        if points < 30:
            pygame.draw.rect(Screen, black, (xloc1, yloc, xsize, ysize1))
            pygame.draw.rect(Screen, black, (xloc1, ysize1 + space, xsize, 600 - ysize1 - space))
        else:
            pygame.draw.rect(Screen, white, (xloc1, yloc, xsize, ysize1))
            pygame.draw.rect(Screen, white, (xloc1, ysize1 + space, xsize, 600 - ysize1 - space))

    def obstacle2(xloc2, yloc, xsize, ysize2):
        if points < 30:
            pygame.draw.rect(Screen, black, (xloc2, yloc, xsize, ysize2))
            pygame.draw.rect(Screen, black, (xloc2, ysize2 + space, xsize, 600 - ysize2 - space))
        else:
            pygame.draw.rect(Screen, white, (xloc2, yloc, xsize, ysize2))
            pygame.draw.rect(Screen, white, (xloc2, ysize2 + space, xsize, 600 - ysize2 - space))            

    def obstacle3(xloc3, yloc, xsize, ysize3):
        if points < 30:
            pygame.draw.rect(Screen, black, (xloc3, yloc, xsize, ysize3))
            pygame.draw.rect(Screen, black, (xloc3, ysize3 + space, xsize, 600 - ysize3 - space))
        else:
            pygame.draw.rect(Screen, white, (xloc3, yloc, xsize, ysize3))
            pygame.draw.rect(Screen, white, (xloc3, ysize3 + space, xsize, 600 - ysize3 - space))

    def obstacle4(xloc4, yloc, xsize, ysize4):
        if points < 30:
            pygame.draw.rect(Screen, black, (xloc4, yloc, xsize, ysize4))
            pygame.draw.rect(Screen, black, (xloc4, ysize4 + space, xsize, 600 - ysize4 - space))
        else:
            pygame.draw.rect(Screen, white, (xloc4, yloc, xsize, ysize4))
            pygame.draw.rect(Screen, white, (xloc4, ysize4 + space, xsize, 600 - ysize4 - space))

# Print the current score when called. After 30 points, print *Hero* below the score counter and play the OPM opening theme.
    def score(points):
        text = font2.render("Score: "+ str(points), True, red)
        Screen.blit(text, [20,0])
        if points >= 30:
            text5 = font2.render("*Hero*", True, red)
            Screen.blit(text5, [20, 50])
        if points == 30 and (xloc1 == 169 or xloc2 == 169 or xloc3 == 169 or xloc4 == 169):
            sound.play(loops = -1)

# Initialize the variables as they should be before the game begins
    Exit = False
    GameOver = False
    points = 0
    headPosition = 300
    headChange = 0
    yloc = 0
    xloc1 = 800
    xloc2 = 1000
    xloc3 = 1200
    xloc4 = 1400
    xsize = 50
    ysize1 = randint(100,300)
    ysize2 = ysize1 + randint(-100,100)
    ysize3 = ysize2 + randint(-100,100)
    ysize4 = ysize3 + randint(-100,100)
    space = 120
    y1checker = 0
    y2checker = 0
    y3checker = 0
    y4checker = 0
    yinit1 = ysize1
    yinit2 = ysize2
    yinit3 = ysize3
    yinit4 = ysize4
    speed = 0.5
    
# Enter the GAME LOOP 
    while not Exit:
        
# If player lost, enter the nested GAME OVER LOOP. If player presses R key, reset all variables and re-enter GAME LOOP by ending GAME OVER LOOP. 
        while GameOver == True:
            Screen.fill(white)
            text = font1.render('Game Over!', True, black)
            text2 = font2.render('Press R to play again or Q to quit.', True, black)
            text3 = font2.render('Your Score was', True, black)
            text4 = font1.render(str(points), True, black)
            Screen.blit(text, [270,0])
            Screen.blit(text2, [205,90])
            Screen.blit(text3, [295,280])
            Screen.blit(text4, [360, 300])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        xloc1 = 800
                        xloc2 = 1000
                        xloc3 = 1200
                        xloc4 = 1400
                        headPosition = 300
                        points = 0
                        ysize1 = randint(100,300)
                        ysize2 = ysize1 + randint(-100,100)
                        ysize3 = ysize2 + randint(-100,100)
                        ysize4 = ysize3 + randint(-100,100)
                        y1checker = 0
                        y2checker = 0
                        y3checker = 0
                        y4checker = 0
                        yinit1 = ysize1
                        yinit2 = ysize2
                        yinit3 = ysize3
                        yinit4 = ysize4
                        GameOver = False
                    if event.key == pygame.K_q:
                        GameOver = False
                        Exit = True
                if event.type == pygame.QUIT:
                    GameOver = False
                    Exit = True
                    pygame.quit()
                    quit()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Exit = True
                pygame.quit()
                quit()
# While the player is holding down the space key, raise the head's y position (on the cartesian plane) by 2 pixels. When the player lets go of the space key, don't make any additional changes to the head position.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    headChange = -2
            if event.type == pygame.KEYUP:             
                headChange = 0
                
# Every frame (round of the loop), move all obstacles to the left by 1 pixel.
        xloc1 -= 1
        xloc2 -= 1
        xloc3 -= 1
        xloc4 -= 1
        
# Every frame (round of the loop), move the head position downwards by one pixel but add any changes according to keystrokes. 
        headPosition = headPosition + headChange
        headPosition += 1
        
# Add a point when an obstacle has passed the head completely.
        if xloc1 == 169 or xloc2 == 169 or xloc3 == 169 or xloc4 == 169:
            points += 1
            
# The height of the new obstacle is randomly generated depending on the height of the previous one (but it can never be more than 130 pixels higher or lower).          
        if points < 50:
            if xloc1 < -50:            
                xloc1 = 800
                ysize1 = ysize4 + randint(-130,130)
                yinit = ysize1
                if ysize1 < 0:
                    ysize1 = ysize4 + randint(0, 130)
                if ysize1 + space > 550:
                    ysize1 = ysize4 + randint(-130, 0)                
            if xloc2 < -50:
                xloc2 = 800
                ysize2 = ysize1 + randint(-130,130)
                if ysize2 < 0:
                    ysize2 = ysize1 + randint(0, 130)
                if ysize2 + space > 550:
                    ysize2 = ysize1 + randint(-130, 0)                
            if xloc3 < -50:
                xloc3 = 800
                ysize3 = ysize2 + randint(-130,130)
                if ysize3 < 0:
                    ysize3 = ysize2 + randint(0, 130)
                if ysize3 + space > 550:
                    ysize3 = ysize2 + randint(-130, 0)                
            if xloc4 < -50:
                xloc4 = 800
                ysize4 = ysize3 + randint(-130,130)
                if ysize4 < 0:
                    ysize4 = ysize3 + randint(0, 130)
                if ysize4 + space > 550:
                    ysize4 = ysize3 + randint(-130, 0) 

# Every frame (round of the loop), wipe the screen canvas clean (white before 30 points and black at 30 points thereafter). Then, set new score and positions of obstacles/head. Then, update the screen.                       
        if points < 30:
            Screen.fill(white)
        else:
            Screen.fill(black)
            
# After 50 points, start moving obstacles vertically. Change speed at point milestones.
        if points >= 50:
            if points < 60:
                speed = 0.3
            if points >= 60 and points < 70:
                speed = 0.6
            if points >= 70:
                speed = 0.8
                            
            if xloc1 < -50:            
                xloc1 = 800
                ysize1 = ysize4 + randint(-75,75)
                yinit = ysize1
                if ysize1 < 0:
                    ysize1 = ysize4 + randint(0, 75)
                if ysize1 + space > 550:
                    ysize1 = ysize4 + randint(-75, 0)                
            if xloc2 < -50:
                xloc2 = 800
                ysize2 = ysize1 + randint(-75,75)
                if ysize2 < 0:
                    ysize2 = ysize1 + randint(0, 75)
                if ysize2 + space > 550:
                    ysize2 = ysize1 + randint(-75, 0)                
            if xloc3 < -50:
                xloc3 = 800
                ysize3 = ysize2 + randint(-75,75)
                if ysize3 < 0:
                    ysize3 = ysize2 + randint(0, 75)
                if ysize3 + space > 550:
                    ysize3 = ysize2 + randint(-75, 0)                
            if xloc4 < -50:
                xloc4 = 800
                ysize4 = ysize3 + randint(-75,75)
                if ysize4 < 0:
                    ysize4 = ysize3 + randint(0, 75)
                if ysize4 + space > 550:
                    ysize4 = ysize3 + randint(-75, 0)

# Switch OFF (Move down if):  <More than 75 pixels higher than original position> OR <Higher than top of the screen> OR <More than 150px higher than 4th block> 
            if ysize1 <= yinit1 - 75 or ysize1 <= 0:
                y1checker = 1
# Switch ON (Move up if): <More than 75 pixels lower than original position> OR <Lower than bottom of screen> OR <More than 150 px lower than 4th block>
            if ysize1 >= yinit1 + 75 or ysize1 + space >= 600:
                y1checker = 0
            if y1checker == 1:
                ysize1 = ysize1 + speed
            elif y1checker == 0:
                ysize1 = ysize1 - speed
 
            if ysize2 == yinit2 - 75 or ysize2 <= 0 or ysize2 <= ysize1 - 150:
                y2checker = 1
            if ysize2 == yinit2 + 75 or ysize2 + space >= 600 or ysize2 >= ysize1 + 150:
                y2checker = 0
            if y2checker == 1:
                ysize2 = ysize2 + speed
            elif y2checker == 0:
                ysize2 = ysize2 - speed
                
            if ysize3 == yinit3 - 75 or ysize3 <= 0 or ysize3 <= ysize2 - 150:
                y3checker = 1
            if ysize3 == yinit3 + 75 or ysize3 + space >= 600 or ysize3 >= ysize2 + 150:
                y3checker = 0
            if y3checker == 1:
                ysize3 = ysize3 + speed
            elif y3checker == 0:
                ysize3 = ysize3 - speed                

            if ysize4 == yinit4 - 75 or ysize4 <= 0 or ysize4 <= ysize3 - 150:
                y4checker = 1
            if ysize4 == yinit4 + 75 or ysize4 + space >= 600 or ysize4 >= ysize3 + 150:
                y4checker = 0
            if y4checker == 1:
                ysize4 = ysize4 + speed
            elif y4checker == 0:
                ysize4 = ysize4 - speed


        obstacle1(xloc1, yloc, xsize, ysize1)
        obstacle2(xloc2, yloc, xsize, ysize2)
        obstacle3(xloc3, yloc, xsize, ysize3)
        obstacle4(xloc4, yloc, xsize, ysize4)
        head()
        score(points)
        pygame.display.update() 

# End the game if the head touches the bottom or the top of the screen. Also play a crash sound and end the OPM opening theme if it's playing.
        if headPosition == 0 or headPosition + 60 == 600 :
            sound.stop()
            crashsound.play()
            time.sleep(1)
            GameOver = True
            
# End the game if the head touches an obstacle (if the obstacle's x and y positions ever coincide). Also play a crash sound and end the OPM opening theme if it's playing.
        if headPosition <= ysize1 and 170 <= xloc1 <= 242 or headPosition + 60 >= ysize1 + space and 170 <= xloc1 <= 242 or headPosition <= ysize2 and 170 <= xloc2 <= 242 or headPosition + 60 >= ysize2 + space and 170 <= xloc2 <= 242 or headPosition <= ysize3 and 170 <= xloc3 <= 242 or headPosition + 60 >= ysize3 + space and 170 <= xloc3 <= 242 or headPosition <= ysize4 and 170 <= xloc4 <= 242 or headPosition + 60 >= ysize4 + space and 170 <= xloc4 <= 242:
            sound.stop()
            crashsound.play()
            time.sleep(1)
            GameOver = True
            
# Load 120 FPS    
        clock.tick(120)   

# Call the INTRODUCTION LOOP. When player breaks the INTRODUCTION LOOP, call the GAME LOOP. When player breaks the GAME LOOP, end the program.
gameIntro()
gameLoop()
pygame.quit()
quit()
