import random

import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT,K_ESCAPE

pygame.init()

FPS = pygame.time.Clock()

screen = width,heigth = 1920, 1080

BLACK = 0, 0, 0
WHITE = 255, 255, 255
EGGPLANT = 97, 64, 81
PURPULE = 128, 0, 128
CROCUS = 145, 114, 236
RED = 255, 0, 0

font = pygame.font.SysFont('verdana', 20)

main_surface = pygame.display.set_mode(screen)


# player = pygame.Surface((20, 20))
# player.fill(WHITE)
player = pygame.image.load('player.png').convert_alpha()
player_rect = player.get_rect()
player_spead = 8

def creat_enemy():
   
   # enemy = pygame.Surface((20, 20))
   # enemy.fill(RED)
   enemy = pygame.image.load('enemy.png').convert_alpha()
   enemy_rect = pygame.Rect(width, random.randint(0, heigth), *enemy.get_size())
   enemy_speed = random.randint(2, 5)
   return [enemy, enemy_rect, enemy_speed]

def creat_lend_lease_usa():
   
   # lend_lease_usa = pygame.Surface((20, 20))
   # lend_lease_usa.fill(CROCUS)
   lend_lease_usa = pygame.image.load('bonus.png').convert_alpha()
   lend_lease_usa_rect = pygame.Rect(random.randint(0, width), 0, *lend_lease_usa.get_size())
   lend_lease_usa_speed = random.randint(5, 8)
   return [lend_lease_usa, lend_lease_usa_rect, lend_lease_usa_speed]

bg = pygame.transform.scale(pygame.image.load('background.png').convert(), screen) 
bgX = 0
bgX2 = bg.get_width()
bg_speed = 3
 
CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 1500)

CREATE_LEND_LEASE_USA = pygame.USEREVENT + 2
pygame.time.set_timer(CREATE_LEND_LEASE_USA, 2500)

scores = 0 
enemies = [] 
lend_lease_usaes = []

is_working=True

while is_working: 
   
   FPS.tick(60)
   
   for event in pygame.event.get():
      if event.type == QUIT:
         is_working = False
         
      if event.type == CREATE_ENEMY: 
         enemies.append(creat_enemy())
         
      if event.type == CREATE_LEND_LEASE_USA: 
         lend_lease_usaes.append(creat_lend_lease_usa())
          
      
   preesed_keys = pygame.key.get_pressed()    
   # main_surface.fill(BLACK)
   # main_surface.blit(bg,(0, 0))
   
   bgX -= bg_speed
   bgX2 -= bg_speed
   
   if bgX <- bg.get_width():
       bgX = bg.get_width()
      
   if bgX2 <- bg.get_width():
       bgX2 = bg.get_width()
         
   
   main_surface.blit(bg,(bgX, 0))
   main_surface.blit(bg,(bgX2, 0))
   
   main_surface.blit(player,player_rect)
   
   main_surface.blit(font.render(str(scores),True,PURPULE),(width -30, 0))
   
   for lend_lease_usa in lend_lease_usaes:
        lend_lease_usa[1] = lend_lease_usa[1].move(0, lend_lease_usa[2])
        main_surface.blit(lend_lease_usa[0], lend_lease_usa[1])

        if lend_lease_usa[1].top > heigth:
            lend_lease_usaes.pop(lend_lease_usaes.index(lend_lease_usa))

        if player_rect.colliderect(lend_lease_usa[1]):
            lend_lease_usaes.pop(lend_lease_usaes.index(lend_lease_usa))
            scores += 1
            
   
   for enemy in enemies:
      enemy[1] = enemy[1].move(-enemy[2], 0)
      main_surface.blit(enemy[0], enemy[1])
      
      if enemy[1].left < 0:
         enemies.pop(enemies.index(enemy))
         
      if player_rect.colliderect(enemy[1]):
         is_working = False
         
   if  preesed_keys[K_ESCAPE]:
       is_working = False
      
      
   if  preesed_keys[K_DOWN] and not player_rect.bottom >= heigth:  
      player_rect = player_rect.move(0, player_spead)
      
   if  preesed_keys[K_UP]and not player_rect.top <= 0:  
      player_rect = player_rect.move(0, -player_spead)
      
   if  preesed_keys[K_RIGHT]and not player_rect.right >= width:
      player_rect = player_rect.move(player_spead, 0)
      
   if  preesed_keys[K_LEFT]and not player_rect.left <= 0:  
      player_rect = player_rect.move(-player_spead, 0)
      
   # print(len(enemies))
      
      
      
   
   #main_surface.fill((155, 155, 155)) 
   pygame.display.flip()      