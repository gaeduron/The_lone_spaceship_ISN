
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
        self.explosion = pygame.image.load('expL.png').convert()
        self.hit_1 = pygame.image.load('ship3_hit1.png').convert()
        self.hit_2 = pygame.image.load('ship3_hit2.png').convert()
        
        transp = self.image.get_at((0,0))
        self.explosion.set_colorkey(transp)
        self.hit_1.set_colorkey(transp)
        self.hit_2.set_colorkey(transp)
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
            current_level.win = 2
            current_level.object_list.remove(self)
            self.kill()
        else:
            pos = pygame.mouse.get_pos()
            self.rect.x = pos[0] - 40
            if (event != None):
                if ( event.type == pygame.KEYDOWN ):
                    if event.key == pygame.K_SPACE:
                        bullet = Bullet()
 
                        bullet.rect.x = player.rect.centerx - 2
                        bullet.rect.y = player.rect.centery - 50

                        current_level.object_list.add(bullet)
                        bullet_list.add(bullet)
    def hit(self):
        
        self.lives -= 1

        if self.lives == 2:
            self.image = self.hit_1

        elif self.lives == 1:
            self.image = self.hit_2

        elif self.lives == 0:
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
            self.rect.x = window_width / 2 + 450
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

            if random.randint(0, 1000) <= 5:
                
                bullet = Bullet_mob(1)
                bullet.rect.x = self.rect.centerx - 2
                bullet.rect.y = self.rect.centery 
                current_level.object_list.add(bullet)
                bullet_list.add(bullet)

        elif self.comportement == 2:
            self.rect.y += 2

            self.rect.x += 10 * math.sin(self.rect.y / 20) + 0.5

            if random.randint(0, 1000) <= 10:
                
                bullet = Bullet_mob(1)
                bullet.rect.x = self.rect.centerx - 2
                bullet.rect.y = self.rect.centery 
                current_level.object_list.add(bullet)
                bullet_list.add(bullet)

        elif self.comportement == 3:
            self.rect.y += 2

            self.rect.x += 60 * math.sin(self.rect.y / 20) + 0.5

            if random.randint(0, 1000) <= 20:
                
                bullet = Bullet_mob(1)
                bullet.rect.x = self.rect.centerx - 2
                bullet.rect.y = self.rect.centery 
                current_level.object_list.add(bullet)
                bullet_list.add(bullet)

        elif self.comportement == 4:
            self.rect.y += 2
            if current_level.score % 2 == 0:
                self.rect.x += 8
            else:
                self.rect.x -= 8

            if rdm_nbr <= 1:
                
                bullet = Bullet_mob(2)
                bullet.rect.y = self.rect.centery
                bullet.rect.x = self.rect.centerx
 
                current_level.object_list.add(bullet)
                bullet_list.add(bullet)

            if rdm_nbr == 99:
                
                bullet = Bullet_mob(3)
                bullet.rect.y = self.rect.centery
                bullet.rect.x = self.rect.centerx
 
                current_level.object_list.add(bullet)
                bullet_list.add(bullet)


        elif self.comportement == 5:
            self.rect.y +=2

            if random.randint(0, 1000) <= 20:
                
                bullet = Bullet_mob(1)
                bullet.rect.x = self.rect.centerx - 30
                bullet.rect.y = self.rect.centery 
                current_level.object_list.add(bullet)
                bullet_list.add(bullet)

                bullet = Bullet_mob(1)
                bullet.rect.x = self.rect.centerx + 30
                bullet.rect.y = self.rect.centery 
                current_level.object_list.add(bullet)
                bullet_list.add(bullet)

        elif self.comportement == 6:
            if self.rect.y <= 100:
                self.rect.y +=1

            if random.randint(0, 1000) <= 20:

                bullet = Bullet_mob(1)
                bullet.rect.x = self.rect.centerx - 50
                bullet.rect.y = self.rect.centery
                current_level.object_list.add(bullet)
                bullet_list.add(bullet)
                bullet = Bullet_mob(1)
                bullet.rect.x = self.rect.centerx + 50
                bullet.rect.y = self.rect.centery
                current_level.object_list.add(bullet)
                bullet_list.add(bullet)

            if random.randint(0, 1000) <= 10:

                bullet = Bullet_mob(4)
                bullet.rect.x = self.rect.centerx -25
                bullet.rect.y = self.rect.centery
                current_level.object_list.add(bullet)

            if random.randint(0, 1000) <= 30:

                bullet = Bullet_mob(2)
                bullet.rect.x = self.rect.centerx - 40
                bullet.rect.y = self.rect.centery
                current_level.object_list.add(bullet)
                bullet_list.add(bullet)
                bullet = Bullet_mob(3)
                bullet.rect.x = self.rect.centerx + 40
                bullet.rect.y = self.rect.centery
                current_level.object_list.add(bullet)
                bullet_list.add(bullet)



    def collide(self, player):
        if pygame.sprite.collide_rect(self, player) == True:
            self.sound = pygame.mixer.Sound("explosion.ogg")
            self.sound.play()
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


        block_hit_list = pygame.sprite.spritecollide(self, mob_list, False)

        for block in block_hit_list:
            self.sound = pygame.mixer.Sound("explosion.ogg")
            self.sound.play()
            block.death()
            bullet_list.remove(bullet)
            current_level.object_list.remove(bullet)
            current_level.score += 1


class Bullet_mob(pygame.sprite.Sprite):

    def __init__(self, categorie):
        super().__init__()

        if categorie == 4:
            self.image = pygame.Surface([40, 80])
        else:           
            self.image = pygame.Surface([5, 35])
        self.image.fill(red)
        self.categorie = categorie
        self.rect = self.image.get_rect()
        self.sound = pygame.mixer.Sound("bulletsound.ogg")
        self.sound.set_volume(0.2)
        self.sound.play()

    def update(self, rdm_nbr):
        if self.categorie == 1:
            self.rect.y += 20

        if self.categorie == 2:
            self.rect.y += 10
            self.rect.x += 8

        if self.categorie == 3:
            self.rect.y += 10
            self.rect.x -= 8

        if self.categorie == 4:
            self.rect.y += 20

    def action(self):
        if self.rect.y > window_height:
            bullet_list.remove(self)
            current_level.object_list.remove(self)


        if pygame.sprite.collide_rect(self, player) == True:
            
            self.sound = pygame.mixer.Sound("explosion.ogg")
            self.sound.play()
            player.hit()
            bullet_list.remove(self)
            current_level.object_list.remove(self)

class Icon(pygame.sprite.Sprite):

    def __init__(self):
        super(Icon, self).__init__()
        
        self.image = pygame.image.load('clock.png').convert()
        transp = self.image.get_at((0,0))
        self.image.set_colorkey(transp)
        self.rect = self.image.get_rect()
        self.rect.x = 1100
        self.rect.y = 20
        print("800")

class Icon_2(pygame.sprite.Sprite):

    def __init__(self):
        super(Icon_2, self).__init__()
        
        self.image = pygame.image.load('skull.png').convert()
        transp = self.image.get_at((0,0))
        self.image.set_colorkey(transp)
        self.rect = self.image.get_rect()
        self.rect.x = 1100
        self.rect.y = 65
        print("802")


class Star(pygame.sprite.Sprite):

    def __init__(self, rdm_nbr):

        super().__init__()
        
        self.image = pygame.Surface([4, 4])
        self.image.fill(white)
        self.rect = self.image.get_rect()

        self.rect.x = random.randrange(1280)
        self.rect.y = -40
       

    def spawn(rdm_nbr):

        if rdm_nbr <= 50:
            star = Star(rdm_nbr)
            star_list.add(star)
            current_level.object_list.add(star)


    def update(self, rdm_nbr):

        self.rect.y += 30
        if self.rect.y > window_height:
            star_list.remove(self)
            current_level.object_list.remove(self)


        
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
        self.second = 0
        self.second_str = str(self.second)
        self.minute = 0
        self.minute_str = str(self.minute)
        self.time_str = self.minute_str + ":" + self.second_str
        self.time_txt = self.font.render(self.time_str, True, white)
        
        self.icon = Icon()
        self.object_list.add(self.icon)
        self.icon_2 = Icon_2()
        self.object_list.add(self.icon_2)
        self.win = 0
        self.end_time = 0


    def win_screen(self):
        
        self.end_time = 1

        self.win_txt = "!!! YOU WIN !!!"
        self.win_text = self.font.render(self.win_txt, True, white)

        self.final_score = str(int((self.score * 1234 ) / (self.minute * 60 + self.second)))


        self.win_info = "YOUR SCORE : " + self.final_score
        self.win_info_text = self.font.render(self.win_info, True, white)

    def death_screen(self):
        
        self.end_time = 1
        self.sound.fadeout(4000)

        self.loser_txt = "GAME OVER"
        self.loser_text = self.font.render(self.loser_txt, True, white)
        

        

    def update( self, rdm_nbr ):

        self.object_list.update( rdm_nbr)
        
        self.score_txt = str(self.score)
        self.text = self.font.render(self.score_txt, True, white)

        if self.end_time == 0:
        
            if self.second >= 60:
                self.second = 0
                self.minute += 1
            else:
                self.second += 1 / frames_per_second

        self.second_str = str(int(self.second))
        self.minute_str = str(self.minute)
        self.time_str = self.minute_str + ":" + self.second_str
        self.time_txt = self.font.render(self.time_str, True, white)

        if self.boss_spawn == 1 and len(mob_list) == 0:
             self.win = 1

        if self.win == 1:
            self.win_screen()

        if self.win == 2:
            self.death_screen()
             
 
    def draw( self, window ):

        window.fill( black )
        self.object_list.draw( window )
        window.blit(self.text, (1220 - self.text.get_width() // 2 , 80 - self.text.get_height() // 2 ))
        window.blit(self.time_txt, (1220 - self.time_txt.get_width() // 2 , 40 - self.time_txt.get_height() // 2 ))

        if self.win == 1:           
            window.blit(self.win_text, (650 - self.win_text.get_width() // 2 , 300 - self.win_text.get_height() // 2 ))
            window.blit(self.win_info_text, (650 - self.win_info_text.get_width() // 2 , 400 - self.win_info_text.get_height() // 2 ))

        if self.win == 2:           
            window.blit(self.loser_text, (650 - self.loser_text.get_width() // 2 , 300 - self.loser_text.get_height() // 2 ))


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


        bullet_list = pygame.sprite.Group()
        mob_list = pygame.sprite.Group()
        star_list = pygame.sprite.Group()
        player = Player()
        player.set_position(400, 700)

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

            event = None
            current_level.update(rdm_nbr)

            # Logic

            for bullet in bullet_list:
                bullet.action()
            
            for mob in mob_list:
                mob.collide(player)
            
            
            Mob.spawn(rdm_nbr, current_level.score)
            Star.spawn(rdm_nbr)

            if current_level.win == 1:
                current_level.win_screen()
                

            # Draw

            current_level.draw(window)
            # Framerate

            clock.tick( frames_per_second )

            # Update the screen
            pygame.display.flip()
            pygame.display.update()


                    
        pygame.quit()
