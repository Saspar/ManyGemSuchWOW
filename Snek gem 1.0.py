#Snek Gem

# if suund == suund 0/1/2/3 (0=yles, 1=parem, 2=vasak jne..)
import pygame
from random import randint
import sys

pygame.init()

screen = pygame.display.set_mode((600, 400))

length = 20
snek = [[15, 10], [15, 11], [15, 12]]

snek_dir = 0
# suund 0/1/2/3 (0=yles, 1=parem, 2=alla, 3=vasak)

score = 0
snekfood = [randint(0, 30), randint(0, 20)]

start = False

while True:
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snek_dir != 1:
                start = True
                snek_dir = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snek_dir != 3:
                start = True
                snek_dir = 2

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and snek_dir != 0:
                start = True
                snek_dir = 1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snek_dir != 2:
                start = True
                snek_dir = 3

    screen.fill ([0, 0, 0])
    
    #yles
    if snek_dir == 0:
        snek.pop()
        snek.insert(0, [snek[0][0], snek[0][1]-1])
    #alla
    elif snek_dir == 1:
        snek.pop()
        snek.insert(0, [snek[0][0], snek[0][1]+1])
    #parem
    elif snek_dir == 2:
        snek.pop()
        snek.insert(0, [snek[0][0]+1, snek[0][1]])
    #vasak
    elif snek_dir == 3:
        snek.pop()
        snek.insert(0, [snek[0][0]-1, snek[0][1]])

    for part in snek:
        
        screen.fill([0, 200, 0], [part[0]*length, part[1]*length, length, length])

    screen.fill([200, 0, 0], [snekfood[0]*length, snekfood[1]*length, length, length])
    
    if snek[0] == snekfood:
        score += 10
        print (score)
        snekfood = [randint(0, 29), randint(0, 19)]
        snek.append(snek[-1])

    if snek[0][0] < 0:
        snek[0][0] = 29

    elif snek [0][0] > 29:
        snek [0][0] = 0

    elif snek [0][1] < 0:
        snek [0][1] = 19

    elif snek [0][1] > 19:
        snek [0][1] = 0

    if snek [0] in snek [1:]:
        print('Game Over!')
        score -=score
        pygame.quit()
        sys.exit
    
    pygame.display.flip()
    pygame.time.wait (120)
