"""Author: Jason Wang
   Date: May 27 2014
   Description: This file contains all the code for the sprites used in the game
"""
import pygame
pygame.init()
#creates player class
class Player(pygame.sprite.Sprite): 
    '''This class defines the sprite for Player'''
    #takes the value for screen from main program  
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        #loades the player image and sets it half way from the top and bottom        
        self.image = pygame.image.load('heli.png')
        self.image= self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.bottom = screen.get_height()/2
    #when this is called it moves the player
    def change_direction(self,displacement):
        #sets the max area they player can move in
        screen_rect = pygame.Rect((0, 0), (640, 500))
        #this moves the player rect according to displacement
        self.rect.move_ip((0,displacement))
        self.rect.clamp_ip(screen_rect)
    #This is called when the player dies and replaces the normal image with
    #a explosion
    def explode(self):
        self.image = pygame.image.load('explosion.png')
 #creates the bolt class       
class Bolt(pygame.sprite.Sprite):
    def __init__(self,ysize,space):
        pygame.sprite.Sprite.__init__(self)
        #loads their image
        self.image=pygame.image.load('lightening2.png')
        self.image= self.image.convert_alpha()
        #this transforms the sprite size thing way the game can have random size
        #bolts each time
        self.image=pygame.transform.scale(self.image, (70,ysize))
        self.rect = self.image.get_rect()
        self.rect.bottom = 400+space
        self.rect.left = 700
        
        self.speed = -4 #horizontal speed of -8
    #this speeds up the bolt    
    def speedup(self):
        self.speed-=0.05
    #This resets their potion and creates their new random size each time they
    #reach the end of the screen
    def reset(self, ysize, space):
        self.image=pygame.image.load('lightening2.png')
        self.image= self.image.convert_alpha()
        self.image=pygame.transform.scale(self.image, (70,ysize))
        self.rect = self.image.get_rect()
        self.rect.bottom = 400+space
        self.rect.left = 700
        
    def update(self):
        self.rect.move_ip(self.speed,0)
       
#This creates the second bolt
class Bolt2(pygame.sprite.Sprite):
    def __init__(self,yloc, ysize):
        pygame.sprite.Sprite.__init__(self)
        
        #create pygame surface with default width 70, height ysize+500
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('lightening.png')
        self.image= self.image.convert_alpha()
        self.image=pygame.transform.scale(self.image, (70,ysize+500))
        self.rect = self.image.get_rect()
        self.rect.bottom = int(yloc+ysize)
        self.rect.left = 700
        
        self.speed = -4
    
    def speedup(self):
        self.speed-=0.05
    
    def reset(self,yloc,ysize):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('lightening.png')
        self.image= self.image.convert_alpha()
        self.image=pygame.transform.scale(self.image, (70,ysize+500))
        self.rect = self.image.get_rect()
        self.rect.bottom = int(yloc+ysize)
        self.rect.left = 700
        
    def update(self):
        self.rect.move_ip(self.speed,0)
        
class ScoreKeeper(pygame.sprite.Sprite):
    #This class defines a label sprite to display the score.
    def __init__(self):
        #This initializer loads the custom font "vermin_vibes.ttf", and
        #sets the starting score to 0
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
 
        # Load our custom font, and initialize the starting score.
        self.__font = pygame.font.Font("vermin_vibes.ttf", 40)
        self.__score = 0
         
    def scored(self,value):
        #This method takes a value as a parameter and adds to the score
        self.__score += value
     
    def get_score(self):
        #Returns the score
        return self.__score
 
    def update(self):
        #This method will be called automatically to display
        #the current score at the top of the game window.
        message = "Score: %d" %\
                (self.__score)
        self.image = self.__font.render(message, 1, (193,205,193))
        self.rect = self.image.get_rect()
        self.rect.center = (320, 30)

class EndZone(pygame.sprite.Sprite):
    #This class defines the sprite for our left and right end zones
    def __init__(self, screen):
        #This initializer takes a screen surface as parameters. The endzone 
        #is set at the bottom of the screen
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
         
        # Our endzone sprite will be a 1 pixel tall black line.
        self.image = pygame.Surface((screen.get_width(),1))
        self.image = self.image.convert()
        self.image.fill((0, 0, 0))
         
        # Set the rect attributes for the endzone
        self.rect = self.image.get_rect()
        self.rect.left=0
        self.rect.bottom=screen.get_height()
        
class OffScreen(pygame.sprite.Sprite):
    #This class defines the sprite for our left and right end zones
    def __init__(self, screen):
        #This initializer takes a screen surface as parameters. The endzone 
        #is set at the bottom of the screen
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
         
        # Our endzone sprite will be a 1 pixel tall black line.
        self.image = pygame.Surface((1,screen.get_width()))
        self.image = self.image.convert()
        self.image.fill((0, 0, 0))
         
        # Set the rect attributes for the endzone
        self.rect = self.image.get_rect()
        self.rect.left=0
        self.rect.bottom=screen.get_height()




    
           
            