
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
red = (255, 0, 0)


"""
    Class

    /// Ici nous allons initialiser les différents objets

"""


class Player(pygame.sprite.Sprite):
    """
    La classe player va permettre de gérer: _les actions du joueur
                                            _le sprite du joueur
                                            _le statut du joueur
    """
    def __init__(self):
        """
        initialisation des caractéristiques de l'objet

        """

        super(Player, self).__init__()

        #On charge les différentes images de l'objet
        self.image = pygame.image.load('image_sprite/ship3.png').convert()
        self.explosion = pygame.image.load('image_sprite/expL.png').convert()
        self.hit_1 = pygame.image.load('image_sprite/ship3_hit1.png').convert()
        self.hit_2 = pygame.image.load('image_sprite/ship3_hit2.png').convert()

        #On met en transparence une couleur clé des images(vert ici) 
        transp = self.image.get_at((0, 0))
        self.explosion.set_colorkey(transp)
        self.hit_1.set_colorkey(transp)
        self.hit_2.set_colorkey(transp)
        self.image.set_colorkey(transp)

        #On attribue au sprite la taille de l'image rectangle 
        self.rect = self.image.get_rect()

        #On initialise les différentes caractéristiques de l'objet
        self.origin_x = self.rect.centerx
        self.origin_y = self.rect.centery
        self.pos = (self.rect.x)
        self.speed = 10
        self.tspeed = 0
        self.k_left = self.k_right = 0
        self.lives = 3
        self.level = None

    def set_position(self, x, y):
        """ On donne la position de départ du sprite """

        self.rect.x = x - self.origin_x
        self.rect.y = y - self.origin_y

    def set_level(self, level):
        """ On joint le sprite au niveau """

        self.level = level
        current_level.object_list.add(self)

    def update(self, collidable=pygame.sprite.Group(), event=None):
        """ On met à jour à chaque tour les caractéristiques de l'objet """

        #test si le joueur est mort
        if self.lives <= 0:
            current_level.win = 2
            current_level.object_list.remove(self)
            self.kill()

        else:
            #On attribue au sprite la position actuelle de la souris
            pos = pygame.mouse.get_pos()
            self.rect.x = pos[0] - 40

            #On test si le joueur tire
            if (event != None):
                if (event.type == pygame.KEYDOWN):
                    if event.key == pygame.K_SPACE:
                        bullet = Bullet()

                        bullet.rect.x = player.rect.centerx - 2
                        bullet.rect.y = player.rect.centery - 50

                        current_level.object_list.add(bullet)
                        bullet_list.add(bullet)

    def hit(self):
        """ On gère les vies du joueur """

        #Lorsque cette fonction est appelée, le joueur perd une vie
        self.lives -= 1

        #On change l'image du sprite en fonction des vies du joueur
        if self.lives == 2:
            self.image = self.hit_1

        elif self.lives == 1:
            self.image = self.hit_2

        elif self.lives == 0:
            self.image = self.explosion


class Mob(pygame.sprite.Sprite):
    """
    La classe Mob va gérer les différents ennemis:  _leurs images
                                                    _leurs mouvements
                                                    _leurs attaques
                                                    _leurs morts
                                                    _leurs sons
                                                    _leurs apparition

    Une particularité de cet objet est que les différents mob ont
    des ordres d'apparition différents et des caractéristiques différentes

    """

    def __init__(self, rdm_nbr, score):
        """ Initialisation des caractéristiques de l'ennemi
            Variable:
                - rdm_nbr correspond au nombre aléatoire généré à chaque
                tour. Il servira à déterminer le sprite d'explosion du mob
                - score est le score du joueur, il permet de changer le
                type de mob qui apparait en fonction de l'avancement du
                joueur
        """

        super().__init__()

        #On va ici déterminer les caractéristiques du mob généré
        self.dead = 0

        #premier type de mob
        if score <= 20:
            position = 1
            mob_sprite = 'image_sprite/mob1.png'
            self.comportement = 1
            self.lives = 1
            if rdm_nbr <= 2:
                exp_sprite = 'image_sprite/exp1.png'
            elif rdm_nbr > 2 and rdm_nbr <= 4:
                exp_sprite = 'image_sprite/exp2.png'
            elif rdm_nbr > 4 and rdm_nbr <= 6:
                exp_sprite = 'image_sprite/exp3.png'
            elif rdm_nbr > 6 and rdm_nbr <= 10:
                exp_sprite = 'image_sprite/exp4.png'

        #second type de mob
        elif score > 20 and score <= 40:
            position = 1
            mob_sprite = 'image_sprite/mob2.png'
            self.comportement = 2
            self.lives = 1
            if rdm_nbr <= 2:
                exp_sprite = 'image_sprite/exp1.png'
            elif rdm_nbr > 2 and rdm_nbr <= 4:
                exp_sprite = 'image_sprite/exp2.png'
            elif rdm_nbr > 4 and rdm_nbr <= 6:
                exp_sprite = 'image_sprite/exp3.png'
            elif rdm_nbr > 6 and rdm_nbr <= 10:
                exp_sprite = 'image_sprite/exp4.png'

        #troisième type de mob
        elif score > 40 and score <= 60:
            position = 2
            mob_sprite = 'image_sprite/mob5.png'
            self.comportement = 3
            self.lives = 1
            if rdm_nbr <= 2:
                exp_sprite = 'image_sprite/exp1.png'
            elif rdm_nbr > 2 and rdm_nbr <= 4:
                exp_sprite = 'image_sprite/exp2.png'
            elif rdm_nbr > 4 and rdm_nbr <= 6:
                exp_sprite = 'image_sprite/exp3.png'
            elif rdm_nbr > 6 and rdm_nbr <= 10:
                exp_sprite = 'image_sprite/exp4.png'

        #quatrième type de mob
        elif score > 60 and score <= 80:
            position = 1
            mob_sprite = 'image_sprite/mob3.png'
            self.comportement = 4
            self.lives = 2
            if rdm_nbr <= 2:
                exp_sprite = 'image_sprite/exp1.png'
            elif rdm_nbr > 2 and rdm_nbr <= 4:
                exp_sprite = 'image_sprite/exp2.png'
            elif rdm_nbr > 4 and rdm_nbr <= 6:
                exp_sprite = 'image_sprite/exp3.png'
            elif rdm_nbr > 6 and rdm_nbr <= 10:
                exp_sprite = 'image_sprite/exp4.png'

        #cinquième type de mob
        elif score > 80 and score <= 100:
            position = 1
            mob_sprite = 'image_sprite/mob4.png'
            self.comportement = 5
            self.lives = 5
            if rdm_nbr <= 2:
                exp_sprite = 'image_sprite/expL.png'
            elif rdm_nbr > 2 and rdm_nbr <= 4:
                exp_sprite = 'image_sprite/expL.png'
            elif rdm_nbr > 4 and rdm_nbr <= 6:
                exp_sprite = 'image_sprite/expL.png'
            elif rdm_nbr > 6 and rdm_nbr <= 10:
                exp_sprite = 'image_sprite/expL.png'

        #Boss de fin
        elif score >= 100 and len(mob_list) == 0:
            position = 3
            mob_sprite = 'image_sprite/boss.png'
            self.comportement = 6
            self.lives = 50
            exp_sprite = 'image_sprite/expL2.png'
            current_level.boss_spawn = 1

        #On met en transparence une couleur clé des images(vert ici)
        self.image = pygame.image.load(mob_sprite).convert()
        self.explosion = pygame.image.load(exp_sprite).convert()
        transparent = self.image.get_at((0, 0))
        self.image.set_colorkey(transparent)
        self.explosion.set_colorkey(transparent)

        #On attribue au sprite la taille de l'image rectangle
        self.rect = self.image.get_rect()

        #On donne sa position au sprite en fonction de son type
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
        """ On appelle cette fonction pour gérer l'apparition des ennemis
            en fonction du rdm_nbr et du score
        """
        #les mobs n'apparaissent que si le boss n'est pas encore apparu
        if current_level.boss_spawn == 0:

            #En fonction du score on gère la fréquence d'apparition des
            #ennemis
            if current_level.score < 80:
                if rdm_nbr <= 10:
                    mob = Mob(rdm_nbr, score)
                    #ajout du mob dans des listes pour pouvoir le gérer
                    mob_list.add(mob)
                    current_level.object_list.add(mob)

            elif current_level.score < 100:
                if rdm_nbr <= 3:
                    mob = Mob(rdm_nbr, score)
                    #ajout du mob dans des listes pour pouvoir le gérer
                    mob_list.add(mob)
                    current_level.object_list.add(mob)
            #On test les conditions pour faire apparaitre le boss
            elif score >= 100 and len(mob_list) == 0:
                if rdm_nbr <= 10:
                    mob = Mob(rdm_nbr, score)
                    #ajout du mob dans des listes pour pouvoir le gérer
                    mob_list.add(mob)
                    current_level.object_list.add(mob)

    def death(self):
        """cette fonction gère les vie de l'ennemi"""
        if self.lives >= 1:
            self.lives -= 1

        #On gère ici la mort de l'ennemi
        if self.lives == 0:
            self.image = self.explosion
            self.sound = pygame.mixer.Sound("sound/explosion.ogg")
            self.sound.play()
            self.dead = 1

    def update(self, rdm_nbr):
        """ On met à jour à chaque tour les caractéristiques de l'objet """

        #efface le sprite d'explosion quand le mob est mort
        if self.dead == 1:
            mob_list.remove(self)
            current_level.object_list.remove(self)
            

        #test si le mob est sorti de l'écran pour l'effacer
        if self.rect.y > 800:
            mob_list.remove(self)
            current_level.object_list.remove(self)

        #test pour effacer le mob si il est mort
        if self.lives <= 0:
            self.death()

        #Action du mob en fonction de son type
        if self.comportement == 1:
            self.rect.y += 8

            if random.randint(0, 1000) <= 5:
                bullet = Bullet_mob(1)
                bullet.rect.x = self.rect.centerx - 2
                bullet.rect.y = self.rect.centery
                current_level.object_list.add(bullet)
                bullet_list.add(bullet)

        #Action du mob en fonction de son type
        elif self.comportement == 2:
            self.rect.y += 2
            self.rect.x += 10 * math.sin(self.rect.y / 20) + 0.5

            if random.randint(0, 1000) <= 10:
                bullet = Bullet_mob(1)
                bullet.rect.x = self.rect.centerx - 2
                bullet.rect.y = self.rect.centery
                current_level.object_list.add(bullet)
                bullet_list.add(bullet)

        #Action du mob en fonction de son type
        elif self.comportement == 3:
            self.rect.y += 2
            self.rect.x += 60 * math.sin(self.rect.y / 20) + 0.5

            if random.randint(0, 1000) <= 20:
                bullet = Bullet_mob(1)
                bullet.rect.x = self.rect.centerx - 2
                bullet.rect.y = self.rect.centery
                current_level.object_list.add(bullet)
                bullet_list.add(bullet)

        #Action du mob en fonction de son type
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

        #Action du mob en fonction de son type
        elif self.comportement == 5:
            self.rect.y += 2

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

        #Action du mob en fonction de son type
        elif self.comportement == 6:
            if self.rect.y <= 100:
                self.rect.y += 1

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
                bullet.rect.x = self.rect.centerx - 25
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
        """ fonction qui test les collisions avec le joueur """

        if pygame.sprite.collide_rect(self, player) == True:
            self.death()
            player.hit()


class Bullet(pygame.sprite.Sprite):
    """ Cette classe gère les balles du joueur """

    def __init__(self):
        """ initialisation des caractéristiques de la balle """
        super().__init__()

        #image
        self.image = pygame.Surface([5, 35])
        self.image.fill(yellow)

        #On attribue au sprite la taille de l'image rectangle
        self.rect = self.image.get_rect()

        #On joue le son de la balle créée
        self.sound = pygame.mixer.Sound("sound/bulletsound.ogg")
        self.sound.set_volume(0.4)
        self.sound.play()

    def update(self, rdm_nbr):
        """ fonction qui met à jour la position de la balle """

        self.rect.y -= 30

    def action(self):
        """ fonction qui gère les interactions de la balle avec le niveau """


        
        if bullet.rect.y < -10:
            bullet_list.remove(bullet)
            current_level.object_list.remove(bullet)

        #gestion des collisions de la balle avec les ennemis
        block_hit_list = pygame.sprite.spritecollide(self, mob_list, False)

        for block in block_hit_list:
            self.sound = pygame.mixer.Sound("sound/explosion.ogg")
            self.sound.play()
            block.death()
            bullet_list.remove(bullet)
            current_level.object_list.remove(bullet)
            current_level.score += 1


class Bullet_mob(pygame.sprite.Sprite):
    """ Cette classe gère les balles des enemies """

    def __init__(self, categorie):
        """ initialisation des caractéristique de la balle """
        super().__init__()

        #image en fonction du type de mob qui la tire
        if categorie == 4:
            self.image = pygame.Surface([40, 80])

        else:
            self.image = pygame.Surface([5, 35])
        self.image.fill(red)

        

        #On attribue au sprite la taille de l'image rectangle
        self.rect = self.image.get_rect()

        #On donne à la balle la catégorie correspondant à son tireur 
        self.categorie = categorie

        #On joue le son de la balle créée
        self.sound = pygame.mixer.Sound("sound/bulletsound.ogg")
        self.sound.set_volume(0.2)
        self.sound.play()

    def update(self, rdm_nbr):
        """
            fonction qui met à jour la position de la balle
            selon son type
        """
    
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
        """ fonction qui gère les interactions de la balle avec le niveau """

        #test qui supprime la balle si elle est en dehors de l'écran
        if self.rect.y > window_height:
            bullet_list.remove(self)
            current_level.object_list.remove(self)

        #gestion des collisions de la balle avec le joueur
        if pygame.sprite.collide_rect(self, player) == True:
            self.sound = pygame.mixer.Sound("sound/explosion.ogg")
            self.sound.play()
            player.hit()
            bullet_list.remove(self)
            current_level.object_list.remove(self)


class Icon(pygame.sprite.Sprite):
    """Classe qui gère l'affichage de l'icone de l'horloge"""

    def __init__(self):
        super(Icon, self).__init__()

        self.image = pygame.image.load('image_sprite/clock.png').convert()
        transp = self.image.get_at((0, 0))
        self.image.set_colorkey(transp)
        self.rect = self.image.get_rect()
        self.rect.x = 1100
        self.rect.y = 20


class Icon_2(pygame.sprite.Sprite):
    """Classe qui gère l'affichage de l'icone du score"""

    def __init__(self):
        super(Icon_2, self).__init__()

        self.image = pygame.image.load('image_sprite/skull.png').convert()
        transp = self.image.get_at((0, 0))
        self.image.set_colorkey(transp)
        self.rect = self.image.get_rect()
        self.rect.x = 1100
        self.rect.y = 65


class Star(pygame.sprite.Sprite):
    """ Classe qui gère génération d'étoile du background """

    def __init__(self, rdm_nbr):
        """ initialisation des caractéristiques de l'étoile"""

        super().__init__()

        #image
        self.image = pygame.Surface([4, 4])
        self.image.fill(white)
        self.rect = self.image.get_rect()

        #attribution d'une position aléatoire initiale
        self.rect.x = random.randrange(1280)
        self.rect.y = -40

    def spawn(rdm_nbr):
        """ Fonction qui gère le taux de génération d'étoile """

        #test qui définit si une étoile apparait ou non
        if rdm_nbr <= 50:
            star = Star(rdm_nbr)
            star_list.add(star)
            current_level.object_list.add(star)

    def update(self, rdm_nbr):
        """ Fonction qui met a jour la position de l'étoile """

        self.rect.y += 30

        #si l'étoile sort de l'écran, elle est effacée
        if self.rect.y > window_height:
            star_list.remove(self)
            current_level.object_list.remove(self)


class Level(object):
    """
    L'objet Level sert à gérer:_tout les sprites
                               _la musique
                               _le score
                               _le temps
                               _le hasard
                               _les écrants de victoire et défaite
                               _L'affichage
    

    """
    def __init__(self, player_object):
        """ initialisation des caractéristiques de l'étoile"""

        #fonction qui contient tous les sprites pour
        #les update et les afficher
        self.object_list = pygame.sprite.Group()

        self.player_object = player_object

        #initialisation du score
        self.score = 0
        self.score_txt = "0"

        #Lancement de la musique 
        self.sound = pygame.mixer.Sound("sound/ironmaiden.ogg")
        self.sound.play()

        #initialisation des textes et conversion des scores et temps
        #en texte à afficher
        self.font = pygame.font.SysFont("FreeMono", 50)
        self.text = self.font.render(self.score_txt, True, white)
        self.second = 0
        self.second_str = str(self.second)
        self.minute = 0
        self.minute_str = str(self.minute)
        self.time_str = self.minute_str + ":" + self.second_str
        self.time_txt = self.font.render(self.time_str, True, white)

        #initialisation des icones à afficher
        self.icon = Icon()
        self.object_list.add(self.icon)
        self.icon_2 = Icon_2()
        self.object_list.add(self.icon_2)

        #initialisation des variables de test
        self.boss_spawn = 0
        self.win = 0
        self.end_time = 0

    def win_screen(self):
        """ Fonction qui affiche l'écran de victoire """

        #stoppe l'horloge
        self.end_time = 1

        #affiche le texte de victoire
        self.win_txt = "!!! YOU WIN !!!"
        self.win_text = self.font.render(self.win_txt, True, white)

        #affiche le score final
        self.final_score = \
            str(int((self.score * 1234) / (self.minute * 60 + self.second)))

        self.win_info = "YOUR SCORE : " + self.final_score
        self.win_info_text = self.font.render(self.win_info, True, white)

    def death_screen(self):
        """ Fonction qui affiche l'écran de défaite """

        #stoppe l'horloge
        self.end_time = 1

        #stoppe la musique
        self.sound.fadeout(4000)
        
        #affiche le texte de défaite
        self.loser_txt = "GAME OVER"
        self.loser_text = self.font.render(self.loser_txt, True, white)

    def update(self, rdm_nbr):
        """ fonction qui met à jour le niveau """
        
        #met à jour tous les sprites
        self.object_list.update(rdm_nbr)
        
        #met à jour le texte du score
        self.score_txt = str(self.score)
        self.text = self.font.render(self.score_txt, True, white)

        #met en forme le temps en texte et met à jour le temps
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

        #test si le joueur a fini le jeu
        if self.boss_spawn == 1 and len(mob_list) == 0:
            self.win = 1

        #si le joueur a gagné, on affiche l'écran de victoire
        if self.win == 1:
            self.win_screen()

        #si le joueur a perdu, on affiche l'écran de défaite
        if self.win == 2:
            self.death_screen()

    def draw(self, window):
        """ Fonction qui affiche tous les sprites dans la fenêtre """

        #On passe la fenêtre en black
        window.fill(black)

        #On dessine tous les sprites
        self.object_list.draw(window)

        #On affiche le score et le temps
        window.blit(self.text, (1220 - self.text.get_width() // 2,
                    80 - self.text.get_height() // 2))
        window.blit(self.time_txt, (1220 - self.time_txt.get_width() // 2,
                    40 - self.time_txt.get_height() // 2))

        #On affiche l'écran de victoire si le joueur a gagné
        if self.win == 1:
            window.blit(self.win_text, (650 - self.win_text.get_width() // 2,
                        300 - self.win_text.get_height() // 2))
            window.blit(self.win_info_text,
                        (650 - self.win_info_text.get_width() // 2,
                         400 - self.win_info_text.get_height() // 2))

        #On affiche l'écran de défaite si le joueur a perdu
        if self.win == 2:
            window.blit(self.loser_text,
                        (650 - self.loser_text.get_width() // 2,
                         300 - self.loser_text.get_height() // 2))

    def random(self):
        """ Fonction qui génère un nombre au hasard et qui le retourne"""

        rdm_nbr = random.randint(0, 201)
        return rdm_nbr


class Level_01(Level):
    """ Object fils de Level, c'est le premier niveau """

    def __init__(self, player_object):
        super(Level_01, self).__init__(player_object)
"""
  ///  On initialise ici les paramètres de notre fenêtre

"""

if (__name__ == "__main__"):

        pygame.init()

        #initialisation de la fenêtre pygame
        window_size = window_width, window_height = 1280, 800
        window = pygame.display.set_mode(window_size)
        pygame.mouse.set_visible(0)
        pygame.display.set_caption("The lone spaceship")

        #initialisation du temps
        clock = pygame.time.Clock()
        frames_per_second = 30

        #initialistion des listes de sprites
        bullet_list = pygame.sprite.Group()
        mob_list = pygame.sprite.Group()
        star_list = pygame.sprite.Group()

        #initialisation du joueur
        player = Player()
        player.set_position(400, 700)

        #création d'une liste de niveau et ajout des niveaux
        level_list = []
        level_list.append(Level_01(player))

        #On désigne le niveau dans lequel on se trouve
        current_level_number = 0
        current_level = level_list[current_level_number]
        
        #On place le joueur dans le niveau actuel
        player.set_level(current_level)


        running = True

        """

               ___________GAME LOOP _________

        """

        while running == True:

            #test si on quitte le jeu
            for event in pygame.event.get():
                if (event.type == pygame.QUIT) or \
                (event.type == pygame.KEYDOWN and \
                (event.key == pygame.K_ESCAPE or event.key == pygame.K_q)):

                    running = False

            """ Update """

            #update du nombre au hasard
            rdm_nbr = current_level.random()

            #update du joueur
            player.update(current_level.object_list, event)
            event = None

            #update de tout ce qui se trouve dans le niveau
            current_level.update(rdm_nbr)

            """ Logic """

            #lance les tests des intéractions des balles avec le niveau
            for bullet in bullet_list:
                bullet.action()

            #lance les tests des intéractions des mobs avec le joueur
            for mob in mob_list:
                mob.collide(player)

            #lance la génération de mobs et d'étoiles
            Mob.spawn(rdm_nbr, current_level.score)
            Star.spawn(rdm_nbr)

            """ Draw """

            current_level.draw(window)

            """ Framerate"""

            clock.tick(frames_per_second)

            """Update the screen"""
            
            pygame.display.flip()
            pygame.display.update()

        pygame.quit()
