

# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 12:36:06 2015

@author: kabiraduron

Touches : Espace    /pour tirer
          La souris /pour déplacer le vaisseau
          Esc       /pour quitter la partie

""" 

import pygame
import random
import math

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
        self.image = pygame.image.load('ship3.png').convert()
        self.explosion = pygame.image.load('expL.png') 
        transp = self.image.get_at((0,0))
        self.explosion.set_colorkey(transp)
        self.image.set_colorkey(transp)
        self.rect = self.image.get_rect()
        self.origin_x = self.rect.centerx
        self.origin_y = self.rect.centery
        self.pos = (self.rect.x)
        self.speed = 10
        self.tspeed = 0
        self.k_left = self.k_right = 0
        self.lives = 3
        self.level = None


    def set_position(self, x, y):
        self.rect.x = x - self.origin_x
        self.rect.y = y - self.origin_y

    def set_level( self, level ):
        self.level = level
        current_level.object_list.add(self)


    def update(self, collidable=pygame.sprite.Group(), event=None):
        if self.lives <= 0:
            print("GAME OVER")
            print(current_level.score)
            pygame.quit()
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0] - 40
        if (event != None):
            if ( event.type == pygame.KEYDOWN ):
                if event.key == pygame.K_SPACE:
                    bullet = Bullet()
                    #print("pow")
                    bullet.rect.x = player.rect.centerx - 2
                    bullet.rect.y = player.rect.centery - 50
 ###               active_object_list.add(bullet)
                    current_level.object_list.add(bullet)
                    bullet_list.add(bullet)
    def hit(self):
        self.lives -= 1
        
        if self.lives == 0:
           self.image = self.explosion


class Mob(pygame.sprite.Sprite):

    def __init__(self, rdm_nbr, score):

        super().__init__()

        self.lives = 1

        if rdm_nbr <= 10:

            if score <= 20:
                position = 1
                mob_sprite = 'mob1.png'
                self.comportement = 1
                self.lives = 1
                if rdm_nbr <=2:
                    exp_sprite = 'exp1.png'
                elif rdm_nbr > 2 and rdm_nbr <= 4:
                    exp_sprite = 'exp2.png'
                elif rdm_nbr > 4 and rdm_nbr <= 6:
                    exp_sprite = 'exp3.png'
                elif rdm_nbr > 6 and rdm_nbr <= 10:
                    exp_sprite = 'exp4.png'
            elif score > 20 and score <= 40:
                position = 1
                mob_sprite = 'mob2.png'
                self.comportement = 2
                self.lives = 1
                if rdm_nbr <=2:
                    exp_sprite = 'exp1.png'
                elif rdm_nbr > 2 and rdm_nbr <= 4:
                    exp_sprite = 'exp2.png'
                elif rdm_nbr > 4 and rdm_nbr <= 6:
                    exp_sprite = 'exp3.png'
                elif rdm_nbr > 6 and rdm_nbr <= 10:
                    exp_sprite = 'exp4.png'
            elif score > 40 and score <= 60:
                position = 2
                mob_sprite = 'mob5.png'
                self.comportement = 3
                self.lives = 1
                if rdm_nbr <=2:
                    exp_sprite = 'exp1.png'
                elif rdm_nbr > 2 and rdm_nbr <= 4:
                    exp_sprite = 'exp2.png'
                elif rdm_nbr > 4 and rdm_nbr <= 6:
                    exp_sprite = 'exp3.png'
                elif rdm_nbr > 6 and rdm_nbr <= 10:
                    exp_sprite = 'exp4.png'
            elif score > 60 and score <= 80:
                position = 1
                mob_sprite = 'mob3.png'
                self.comportement = 4
                self.lives = 2
                if rdm_nbr <=2:
                    exp_sprite = 'exp1.png'
                elif rdm_nbr > 2 and rdm_nbr <= 4:
                    exp_sprite = 'exp2.png'
                elif rdm_nbr > 4 and rdm_nbr <= 6:
                    exp_sprite = 'exp3.png'
                elif rdm_nbr > 6 and rdm_nbr <= 10:
                    exp_sprite = 'exp4.png'
            elif score > 80 and score <= 100:
                position = 1
                mob_sprite = 'mob4.png'
                self.comportement = 5
                self.lives = 5
                if rdm_nbr <=2:
                    exp_sprite = 'expL.png'
                elif rdm_nbr > 2 and rdm_nbr <= 4:
                    exp_sprite = 'expL.png'
                elif rdm_nbr > 4 and rdm_nbr <= 6:
                    exp_sprite = 'expL.png'
                elif rdm_nbr > 6 and rdm_nbr <= 10:
                    exp_sprite = 'expL.png'
            elif score >= 100 and len(mob_list) == 0:
                position = 3
                mob_sprite = 'boss.png'
                self.comportement = 6
                self.lives = 50
                exp_sprite = 'expL2.png'
                current_level.boss_spawn = 1
                
                
        
        self.image = pygame.image.load(mob_sprite).convert()
        self.explosion = pygame.image.load(exp_sprite).convert()
        transparent = self.image.get_at((0,0))
        self.image.set_colorkey(transparent)
        self.explosion.set_colorkey(transparent)
        self.rect = self.image.get_rect()

        if position == 1:
            self.rect.x = random.randrange(1280)
            self.rect.y = -40

        if position == 2:
            self.rect.x = window_width / 2 + 300
            self.rect.y = -50

        if position == 3:
            self.rect.x = window_width / 2 - 100
            self.rect.y = -50
            
        

    def spawn(rdm_nbr, score):
        if current_level.boss_spawn == 0:
            if current_level.score < 80:
                if rdm_nbr <= 10:
                    mob = Mob(rdm_nbr, score) 
    
                    mob_list.add(mob)
                    current_level.object_list.add(mob)
            elif current_level.score < 100:
                if rdm_nbr <= 3:
                    mob = Mob(rdm_nbr, score) 
    
                    mob_list.add(mob)
                    current_level.object_list.add(mob)
            elif score >= 100 and len(mob_list) == 0:
                if rdm_nbr <= 10:
                    mob = Mob(rdm_nbr, score) 
    
                    mob_list.add(mob)
                    current_level.object_list.add(mob)

    def death(self):
        self.lives -= 1

        if self.lives == 0:
            self.image = self.explosion
        

    def update(self, rdm_nbr):
        if self.rect.y >  800:
            mob_list.remove(self)
            current_level.object_list.remove(self)
        if self.lives <= 0:

            mob_list.remove(self)
            current_level.object_list.remove(self)

        if self.comportement == 1:
            self.rect.y += 8

        elif self.comportement == 2:
            self.rect.y += 2

            self.rect.x += 10 * math.sin(self.rect.y / 20) + 0.5

        elif self.comportement == 3:
            self.rect.y += 2

            self.rect.x += 60 * math.sin(self.rect.y / 20) + 0.5

        elif self.comportement == 4:
            self.rect.y += 2
            if current_level.score % 2 == 0:
                self.rect.x += 8
            else:
                self.rect.x -= 8

        elif self.comportement == 5:
            self.rect.y +=2

        elif self.comportement == 6:
            self.rect.y +=1


    def collide(self, player):
        if pygame.sprite.collide_rect(self, player) == True:
            self.death()
            player.hit()
            
            
        


class Bullet(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([5, 35])
        self.image.fill(yellow)

        self.rect = self.image.get_rect()
        self.sound = pygame.mixer.Sound("bulletsound.ogg")
        self.sound.set_volume(0.4)
        self.sound.play()

    def update(self, rdm_nbr):
        self.rect.y -= 30

    def action(self):
        if bullet.rect.y < -10:
            bullet_list.remove(bullet)
            current_level.object_list.remove(bullet)
            #print("clear")

        block_hit_list = pygame.sprite.spritecollide(self, mob_list, False)
       # print(block_hit_list)
        # For each block hit, remove the bullet and add to the score
        for block in block_hit_list:
            self.sound = pygame.mixer.Sound("explosion.ogg")
            self.sound.play()
            block.death()
            bullet_list.remove(bullet)
            current_level.object_list.remove(bullet)
            current_level.score += 1
            #print("score = ", current_level.score)

        
class Level(object):
    """
    L'objet Level sert gerer tout les sprites 

    """
    def __init__(self, player_object):
        self.object_list = pygame.sprite.Group()
        self.player_object = player_object
        self.score = 0
        self.score_txt = "0"
        self.boss_spawn = 0
        self.sound = pygame.mixer.Sound("ironmaiden.ogg")
        self.sound.play()
        self.font = pygame.font.SysFont("FreeMono", 50)
        self.text = self.font.render(self.score_txt, True, white)

    def update( self, rdm_nbr ):
        self.object_list.update( rdm_nbr)
        self.score_txt = str(self.score)
        self.text = self.font.render(self.score_txt, True, white) 
        print(self.score_txt)
        #print(mob_list)
        if self.boss_spawn == 1 and len(mob_list) == 0:
             print("!!! YOU WIN !!!")
             print("your score is : ", self.score)
             pygame.quit()
 
    def draw( self, window ):
        window.fill( black )
        self.object_list.draw( window )
        window.blit(self.text, (60 - self.text.get_width() // 2 , 40 - self.text.get_height() // 2 ))

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
        window = pygame.display.set_mode( window_size, pygame.RESIZABLE )
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
            rdm_nbr = current_level.random()              
            player.update( current_level.object_list, event )
                                         ###active_object_list.update()
            event = None
            current_level.update(rdm_nbr)

            # Logic

            for bullet in bullet_list:
                bullet.action()
            
            for mob in mob_list:
                mob.collide(player)
            
            
            #print(rdm_nbr)
            Mob.spawn(rdm_nbr, current_level.score)

            # Draw

            current_level.draw(window)
            
                                         ###active_object_list.draw(window)

            # Framerate

            clock.tick( frames_per_second )

            # Update the screen
            pygame.display.flip()
            pygame.display.update()
 
        pygame.quit()
