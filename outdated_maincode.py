# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 12:36:06 2015

@author: kabiraduron
"""

import pygame
import random

""" Couleurs """

black = (0, 0, 1)
white = (255, 255, 255)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)


""" Class"""


class Player(pygame.sprite.Sprite):

    def __init__(self):

        super(Player, self).__init__()
        self.image = pygame.image.load('ship2.png')
        self.rect = self.image.get_rect()
        self.origin_x = self.rect.centerx
        self.origin_y = self.rect.centery
        self.pos = (self.rect.x)
        self.speed = 10
        self.tspeed = 0
        self.k_left = self.k_right = 0

        self.level = None


    def set_position(self, x, y):
        self.rect.x = x - self.origin_x
        self.rect.y = y - self.origin_y

    def set_level( self, level ):
        self.level = level
        current_level.object_list.add(self)


    def update(self, collidable=pygame.sprite.Group(), event=None):

        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0] - 40
        if (event != None):
            if event.type == pygame.MOUSEBUTTONDOWN:
                bullet = Bullet()
                print("pow")
                bullet.rect.x = player.rect.centerx - 2
                bullet.rect.y = player.rect.centery - 50
 ###               active_object_list.add(bullet)
                current_level.object_list.add(bullet)
                bullet_list.add(bullet)


class Mob(pygame.sprite.Sprite):

    def __init__(self, rdm_nbr):

        super().__init__()

        if rdm_nbr == 1 or rdm_nbr == 2 or rdm_nbr == 0:
            mob_sprite = 'mob1.png'
        if rdm_nbr == 3 or rdm_nbr == 4:
            mob_sprite = 'mob2.png'
        if rdm_nbr == 5 or rdm_nbr == 6:
            mob_sprite = 'mob3.png'
        if rdm_nbr == 7 or rdm_nbr == 8:
            mob_sprite = 'mob4.png'
        if rdm_nbr == 9 or rdm_nbr == 10:
            mob_sprite = 'mob5.png'
        
        self.image = pygame.image.load(mob_sprite).convert()
        transparent = self.image.get_at((0,0))
        self.image.set_colorkey(transparent)
        self.rect = self.image.get_rect()
        

    def spawn(rdm_nbr):
        if rdm_nbr <= 10:
            mob = Mob(rdm_nbr)
 

            mob.rect.x = random.randrange(1280)
            mob.rect.y = 40
 

            mob_list.add(mob)
            current_level.object_list.add(mob)

    def update(self):
        self.rect.y += 2
    
            
        


class Bullet(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([5, 35])
        self.image.fill(yellow)

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y -= 30

    def action(self):
        if bullet.rect.y < -10:
            bullet_list.remove(bullet)
            current_level.object_list.remove(bullet)
            print("clear")

        block_hit_list = pygame.sprite.spritecollide(bullet, mob_list, True)
 
        # For each block hit, remove the bullet and add to the score
        for block in block_hit_list:
            bullet_list.remove(bullet)
            current_level.object_list.remove(bullet)

        
class Level(object):
    """
    L'objet Level sert gerer tout les sprites 

    """
    def __init__(self, player_object):
        self.object_list = pygame.sprite.Group()
        self.player_object = player_object
        self.score = 0

    def update( self ):
        self.object_list.update()
 
    def draw( self, window ):
        window.fill( black )
        self.object_list.draw( window )

    def random(self):
        rdm_nbr = random.randint(0,201)
        return rdm_nbr
        

class Level_01( Level ):
 
        def __init__( self, player_object ):
 
                super( Level_01, self ).__init__( player_object )
"""

 //////       //////        /// / MAIN / ///      //////       ///////

"""

if ( __name__ == "__main__" ):
        pygame.init()
 
        window_size = window_width, window_height = 1280, 800
        window = pygame.display.set_mode( window_size )
        pygame.mouse.set_visible(0)
        pygame.display.set_caption("Shmup")

        clock = pygame.time.Clock()
        frames_per_second = 30

 ###       active_object_list = pygame.sprite.Group()
        bullet_list = pygame.sprite.Group()
        mob_list = pygame.sprite.Group()
        player = Player()
        player.set_position(400, 700)
 ###       active_object_list.add( player )

        level_list = []
        level_list.append( Level_01( player ) )
 
        current_level_number = 0
        current_level = level_list[ current_level_number ]
 
        player.set_level( current_level )

        running = True

        """
 
               ___________GAME LOOP _________

        """
        
        while (running == True):

            for event in pygame.event.get():
                if ( event.type == pygame.QUIT ) or \
                ( event.type == pygame.KEYDOWN and \
                ( event.key == pygame.K_ESCAPE or event.key == pygame.K_q ) ):                    
                    running = False
            # Update
                
            player.update( current_level.object_list, event )
                                         ###active_object_list.update()
            event = None
            current_level.update()

            # Logic

            for bullet in bullet_list:
                bullet.action()
            
            rdm_nbr = current_level.random()
            print(rdm_nbr)
            Mob.spawn(rdm_nbr)

            # Draw

            current_level.draw(window)
                                         ###active_object_list.draw(window)

            # Framerate

            clock.tick( frames_per_second )

            # Update the screen
            
            pygame.display.update()
 
        pygame.quit()
