"""Author: Jason Wang
   Date: May 27 2014
   Description: This program is a game called storm flyer you the player 
   controll a helicopter your goal is to dodge the 2 lighting bolts each
   time you do so you get one point after getting 5 points the game speeds up
   you control the helicopter with the up arrow key, it will go down by itself
   if no key is held
"""
# Initialize 
import pygame,sprites
import random
pygame.mixer.init()
pygame.init()
#sets the number of times key press is sent to pygame
pygame.key.set_repeat(17,17) 
# Display 
screen = pygame.display.set_mode((700, 500)) 
pygame.display.set_caption("Storm flyer") 
  
# Entities 
#loads the sound for the background and sets the volume
pygame.mixer.music.load('storm.wav')
pygame.mixer.music.set_volume(1) 
pygame.mixer.music.play(-1)
#loads and sets volume for the helicopter sound effect
heli=pygame.mixer.Sound('Helicopter.wav')
heli.set_volume(0.2)
heli.play(-1)
#loads and sets volume for the explode effect when player dies
explode=pygame.mixer.Sound('Explosion.wav')
explode.set_volume(1)
#loads the 2 pics of the background
background = pygame.image.load('DarkStone.png')
background2 = pygame.image.load('DarkStone.png')
background = background.convert()

#these are the values for that are used for scrolling the background
x=0
screenWidth = 700
 

# "Game Over" Image to Display After Game Loop Terminates
gameover_img = pygame.image.load('gameover.png')
gameover_img = gameover_img.convert_alpha()

# sprites 
#creates and sets the values to make the random spaces for the 2 thunder bolts
yloc = 0
space = 100
ysize = random.randint(110,190)
#creates player
player=sprites.Player(screen)

#create bolt and bolt2 and group them
bolt=sprites.Bolt(ysize,space)
bolt2=sprites.Bolt2(yloc,ysize,)
boltGroup=pygame.sprite.Group(bolt,bolt2)
#creates the sprite which check to see if the thunder bolts reach the end of the
#screen and the sprite that checks to see if player is on bottom of screen
offscreen=sprites.OffScreen(screen)
endzone=sprites.EndZone(screen)
score_keeper = sprites.ScoreKeeper()
#groups all sprites together
allSprites = pygame.sprite.Group\
           (score_keeper,bolt,bolt2,player,offscreen,endzone)

  
# ACTION 

# Assign  
clock = pygame.time.Clock() 
keepGoing = True
 
    
    # Loop 
while keepGoing: 
  
    # Time 
    clock.tick(30) 
#this blits the background on the screen and moves them towards the left
#this helps to create the illusion that the player is moving forward
    screen.blit(background, (x, 0))
    screen.blit(background2, (x+screenWidth, 0))
    x=x-4
#sets the backgrounds to their start postion if they go off screen    
    if x==-700:
        x=0
    # Events 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            keepGoing = False
        #the controls for the user if they press up arrow key they go up
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.change_direction(-10)
#checks to see if player collides with the bottom of screen or the bolts
    if player.rect.colliderect(endzone.rect) or\
       pygame.sprite.spritecollide(player,boltGroup, True):
#plays the dealth sound effect and stops the helicoper sound effects and ends
#the game
        explode.play()
        heli.stop()
        player.explode()
        keepGoing = False
    
    #player's direction goes down every frame
    player.change_direction(5)
    
    allSprites.clear(screen, background) 
    allSprites.update()
#checks to see if these sprites have collided with each other or not    
    bolt_off_screen = pygame.sprite.spritecollide(offscreen,boltGroup,False)
#if the bolt sprites reach the end of screen it calls their reset and they are
#put back to their start postions and this also sends a new random value for 
#their height
    if bolt_off_screen:
        ysize = random.randint(110,190)
        bolt.reset(ysize,space)
        bolt2.reset(yloc,ysize,)
        boltGroup=pygame.sprite.Group(bolt,bolt2)
#adds a score if the bolt sprite collides with the offscreen sprite if it did
#this means the player has not collided with them and has passed though them
        allSprites = pygame.sprite.Group\
                    (score_keeper,bolt,bolt2,player,offscreen,endzone)
        score_keeper.scored(1)
#this speeds up the game each time the player gets 5 points    
    if (score_keeper.get_score()%5==0) and (score_keeper.get_score()!=0):
        bolt.speedup()
        bolt2.speedup()
        
    allSprites.draw(screen)
    pygame.display.flip()

#Blit gameover on screen
screen.blit(gameover_img, (150, 100))
pygame.display.flip()
#Delay by 4500 miliseconds
pygame.mixer.music.fadeout(4500)
pygame.time.delay(4500)
# Close the game window 
pygame.quit()
  
      
