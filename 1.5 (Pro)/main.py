# Flappy Bird of Reality Game
# Source Code

import random
import pygame
import sys
import os
from pygame.locals import *
# from pygame.locals import *
import time
from tkinter import *
from plyer import notification

# Global Variables
FPS = 32
SCREENWIDTH = 287  # 288
SCREENHEIGHT = 511
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GROUNDY = SCREENHEIGHT * 0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = './gallery/bird/bird1.png'
BACKGROUND = './gallery/assets/bg_startup.jpg'
BACKGROUND_SECOND = './gallery/assets/bg_game1.jpg'
BACKGROUND_THIRD = './gallery/assets/bg_game2.jpg'
BACKGROUND_FOUR = './gallery/assets/bg_game3.jpg'
BACKGROUND_FIVE = './gallery/assets/bg_game4.jpg'
# PIPE = './gallery/pipe.png'

def welcomeScreen():
    """
    Shows welcome images on the screen
    """
    GAME_SOUNDS['on'].play()
    time.sleep(3.9)
    GAME_SOUNDS['Yay'].play(-1)
    GAME_SOUNDS['hello'].stop()
    GAME_SOUNDS['hello2'].stop()
    GAME_SOUNDS['hello3'].stop()
    GAME_SOUNDS['hello4'].stop()
    playerx = int(SCREENWIDTH / 9)
    playery = int((SCREENHEIGHT - GAME_SPRITES['player'].get_height()) / 3)
    messagex = int((SCREENWIDTH - GAME_SPRITES['message'].get_width()) / 2)
    gameIcon = pygame.image.load('./gallery/assets/icon.png')
    pygame.display.set_icon(gameIcon)
    messagey = int(SCREENHEIGHT * 0.01)
    basex = 0

    while True:
        for event in pygame.event.get():
            # if user clicks on cross button, close the game
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                GAME_SOUNDS['off'].play()
                GAME_SOUNDS['hello'].stop()
                GAME_SOUNDS['Yay'].stop()
                time.sleep(3.4)
                pygame.quit()
                sys.exit()

            # If the user presses space or up key, start the game for them
            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                GAME_SOUNDS['Yay'].stop()
                GAME_SOUNDS['hello'].play(-1)
                return
            else:
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))
                SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))
                SCREEN.blit(GAME_SPRITES['message'], (messagex, messagey))
                SCREEN.blit(GAME_SPRITES['bassee'], (basex, GROUNDY))
                pygame.display.update()
                FPSCLOCK.tick(FPS)
                
def welcomeScreen_second():
    """
    Shows welcome images on the screen
    """
    GAME_SOUNDS['Yay'].play(-1)
    GAME_SOUNDS['hello'].stop()
    GAME_SOUNDS['hello2'].stop()
    GAME_SOUNDS['hello3'].stop()
    GAME_SOUNDS['hello4'].stop()
    playerx = int(SCREENWIDTH / 9)
    playery = int((SCREENHEIGHT - GAME_SPRITES['player'].get_height()) / 3)
    messagex = int((SCREENWIDTH - GAME_SPRITES['message'].get_width()) / 2)
    gameIcon = pygame.image.load('./gallery/assets/icon.png')
    pygame.display.set_icon(gameIcon)
    messagey = int(SCREENHEIGHT * 0.01)
    basex = 0

    while True:
        for event in pygame.event.get():
            # if user clicks on cross button, close the game
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                GAME_SOUNDS['off'].play()
                GAME_SOUNDS['hello'].stop()
                GAME_SOUNDS['Yay'].stop()
                time.sleep(3.4)
                pygame.quit()
                sys.exit()

            # If the user presses space or up key, start the game for them
            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                GAME_SOUNDS['Yay'].stop()
                GAME_SOUNDS['hello2'].play(-1)
                return
            else:
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))
                SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))
                SCREEN.blit(GAME_SPRITES['message'], (messagex, messagey))
                SCREEN.blit(GAME_SPRITES['bassee'], (basex, GROUNDY))
                pygame.display.update()
                FPSCLOCK.tick(FPS)
                
def welcomeScreen_three():
    """
    Shows welcome images on the screen
    """
    GAME_SOUNDS['Yay'].play(-1)
    GAME_SOUNDS['hello'].stop()
    GAME_SOUNDS['hello2'].stop()
    GAME_SOUNDS['hello3'].stop()
    GAME_SOUNDS['hello4'].stop()
    playerx = int(SCREENWIDTH / 9)
    playery = int((SCREENHEIGHT - GAME_SPRITES['player'].get_height()) / 3)
    messagex = int((SCREENWIDTH - GAME_SPRITES['message'].get_width()) / 2)
    gameIcon = pygame.image.load('./gallery/assets/icon.png')
    pygame.display.set_icon(gameIcon)
    messagey = int(SCREENHEIGHT * 0.01)
    basex = 0

    while True:
        for event in pygame.event.get():
            # if user clicks on cross button, close the game
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                GAME_SOUNDS['off'].play()
                GAME_SOUNDS['hello'].stop()
                GAME_SOUNDS['Yay'].stop()
                time.sleep(3.4)
                pygame.quit()
                sys.exit()

            # If the user presses space or up key, start the game for them
            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                GAME_SOUNDS['Yay'].stop()
                GAME_SOUNDS['hello3'].play(-1)
                return
            else:
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))
                SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))
                SCREEN.blit(GAME_SPRITES['message'], (messagex, messagey))
                SCREEN.blit(GAME_SPRITES['bassee'], (basex, GROUNDY))
                pygame.display.update()
                FPSCLOCK.tick(FPS)
                
def welcomeScreen_four():
    """
    Shows welcome images on the screen
    """
    GAME_SOUNDS['Yay'].play(-1)
    GAME_SOUNDS['hello'].stop()
    GAME_SOUNDS['hello2'].stop()
    GAME_SOUNDS['hello3'].stop()
    GAME_SOUNDS['hello4'].stop()
    playerx = int(SCREENWIDTH / 9)
    playery = int((SCREENHEIGHT - GAME_SPRITES['player'].get_height()) / 3)
    messagex = int((SCREENWIDTH - GAME_SPRITES['message'].get_width()) / 2)
    gameIcon = pygame.image.load('./gallery/assets/icon.png')
    pygame.display.set_icon(gameIcon)
    messagey = int(SCREENHEIGHT * 0.01)
    basex = 0

    while True:
        for event in pygame.event.get():
            # if user clicks on cross button, close the game
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                GAME_SOUNDS['off'].play()
                GAME_SOUNDS['hello'].stop()
                GAME_SOUNDS['Yay'].stop()
                time.sleep(3.4)
                pygame.quit()
                sys.exit()

            # If the user presses space or up key, start the game for them
            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                GAME_SOUNDS['Yay'].stop()
                GAME_SOUNDS['hello4'].play(-1)
                return
            else:
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))
                SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))
                SCREEN.blit(GAME_SPRITES['message'], (messagex, messagey))
                SCREEN.blit(GAME_SPRITES['bassee'], (basex, GROUNDY))
                pygame.display.update()
                FPSCLOCK.tick(FPS)


def mainGame():
    score = 0
    playerx = int(SCREENWIDTH / 5)
    playery = int(SCREENWIDTH / 2)
    basex = 0

    # Create 2 pipes for blitting on the screen
    newPipe1 = getRandomPipe()
    newPipe2 = getRandomPipe()

    # my List of upper pipes
    upperPipes = [
        {'x': SCREENWIDTH + 200, 'y': newPipe1[0]['y']},
        {'x': SCREENWIDTH + 200 + (SCREENWIDTH / 2), 'y': newPipe2[0]['y']},
    ]
    # my List of lower pipes
    lowerPipes = [
        {'x': SCREENWIDTH + 200, 'y': newPipe1[1]['y']},
        {'x': SCREENWIDTH + 200 + (SCREENWIDTH / 2), 'y': newPipe2[1]['y']},
    ]

    pipeVelX = -4

    playerVelY = -14
    playerMaxVelY = 8
    playerAccY = 1

    playerFlapAccv = -9.5  # velocity while flapping
    playerFlapped = False  # It is true only when the bird is flapping

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                GAME_SOUNDS['off'].play()
                GAME_SOUNDS['hello'].stop()
                GAME_SOUNDS['Yay'].stop()
                time.sleep(3.4)
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if playery > 0:
                    playerVelY = playerFlapAccv
                    playerFlapped = True
                    GAME_SOUNDS['wing'].play()

        crashTest = isCollide(playerx, playery, upperPipes,
                              lowerPipes)
        # This function will return true if the player is crashed
        if crashTest:
            return

            # check for score
        playerMidPos = playerx + GAME_SPRITES['player'].get_width() / 2
        for pipe in upperPipes:
            pipeMidPos = pipe['x'] + GAME_SPRITES['pipe'][0].get_width() / 2
            if pipeMidPos <= playerMidPos < pipeMidPos + 4:
                score += 5
                GAME_SOUNDS['point'].play()
                print(f"Your Score is {score}")
                with open(f"Hiscore.flap") as f:
                    check = f.read()
                    if score > int(check):
                        with open(f"Hiscore.flap", "w") as f:
                            f.write(str(score))
                            check = score
                    

        if playerVelY < playerMaxVelY and not playerFlapped:
            playerVelY += playerAccY

        if playerFlapped:
            playerFlapped = False
        playerHeight = GAME_SPRITES['player'].get_height()
        playery = playery + min(playerVelY, GROUNDY - playery - playerHeight)

        # move pipes to the left
        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
            upperPipe['x'] += pipeVelX
            lowerPipe['x'] += pipeVelX

        # Add a new pipe when the first is about to cross the leftmost part of the screen
        if 0 < upperPipes[0]['x'] < 5:
            newpipe = getRandomPipe()
            upperPipes.append(newpipe[0])
            lowerPipes.append(newpipe[1])

        # if the pipe is out of the screen, remove it
        if upperPipes[0]['x'] < -GAME_SPRITES['pipe'][0].get_width():
            upperPipes.pop(0)
            lowerPipes.pop(0)

        # Lets blit our sprites now
        SCREEN.blit(GAME_SPRITES['background_second'], (0, 0))
        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
            SCREEN.blit(GAME_SPRITES['pipe'][0],
                        (upperPipe['x'], upperPipe['y']))
            SCREEN.blit(GAME_SPRITES['pipe'][1],
                        (lowerPipe['x'], lowerPipe['y']))

        SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))
        SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))
        myDigits = [int(x) for x in list(str(score))]
        width = 0
        for digit in myDigits:
            width += GAME_SPRITES['numbers'][digit].get_width()
        Xoffset = (SCREENWIDTH - width) / 2

        for digit in myDigits:
            SCREEN.blit(GAME_SPRITES['numbers'][digit],
                        (Xoffset, SCREENHEIGHT * 0.12))
            Xoffset += GAME_SPRITES['numbers'][digit].get_width()
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def mainGame_two():
    score = 0
    playerx = int(SCREENWIDTH / 5)
    playery = int(SCREENWIDTH / 2)
    basex = 0

    # Create 2 pipes for blitting on the screen
    newPipe1 = getRandomPipe()
    newPipe2 = getRandomPipe()

    # my List of upper pipes
    upperPipes = [
        {'x': SCREENWIDTH + 200, 'y': newPipe1[0]['y']},
        {'x': SCREENWIDTH + 200 + (SCREENWIDTH / 2), 'y': newPipe2[0]['y']},
    ]
    # my List of lower pipes
    lowerPipes = [
        {'x': SCREENWIDTH + 200, 'y': newPipe1[1]['y']},
        {'x': SCREENWIDTH + 200 + (SCREENWIDTH / 2), 'y': newPipe2[1]['y']},
    ]

    pipeVelX = -4

    playerVelY = -14
    playerMaxVelY = 8
    playerAccY = 1

    playerFlapAccv = -9.5  # velocity while flapping
    playerFlapped = False  # It is true only when the bird is flapping

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                GAME_SOUNDS['off'].play()
                GAME_SOUNDS['hello2'].stop()
                GAME_SOUNDS['Yay'].stop()
                time.sleep(3.4)
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if playery > 0:
                    playerVelY = playerFlapAccv
                    playerFlapped = True
                    GAME_SOUNDS['wing'].play()

        crashTest = isCollide(playerx, playery, upperPipes,
                              lowerPipes)  # This function will return true if the player is crashed
        if crashTest:
            return

            # check for score
        playerMidPos = playerx + GAME_SPRITES['player'].get_width() / 2
        for pipe in upperPipes:
            pipeMidPos = pipe['x'] + GAME_SPRITES['pipe'][0].get_width() / 2
            if pipeMidPos <= playerMidPos < pipeMidPos + 4:
                score += 5
                GAME_SOUNDS['point'].play()
                print(f"Your Score is {score}")
                with open(f"Hiscore.flap") as f:
                    check = f.read()
                    if score > int(check):
                        with open(f"Hiscore.flap", "w") as f:
                            f.write(str(score))

        if playerVelY < playerMaxVelY and not playerFlapped:
            playerVelY += playerAccY

        if playerFlapped:
            playerFlapped = False
        playerHeight = GAME_SPRITES['player'].get_height()
        playery = playery + min(playerVelY, GROUNDY - playery - playerHeight)

        # move pipes to the left
        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
            upperPipe['x'] += pipeVelX
            lowerPipe['x'] += pipeVelX

        # Add a new pipe when the first is about to cross the leftmost part of the screen
        if 0 < upperPipes[0]['x'] < 5:
            newpipe = getRandomPipe()
            upperPipes.append(newpipe[0])
            lowerPipes.append(newpipe[1])

        # if the pipe is out of the screen, remove it
        if upperPipes[0]['x'] < -GAME_SPRITES['pipe'][0].get_width():
            upperPipes.pop(0)
            lowerPipes.pop(0)

        # Lets blit our sprites now
        SCREEN.blit(GAME_SPRITES['background_third'], (0, 0))
        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
            SCREEN.blit(GAME_SPRITES['pipe'][0],
                        (upperPipe['x'], upperPipe['y']))
            SCREEN.blit(GAME_SPRITES['pipe'][1],
                        (lowerPipe['x'], lowerPipe['y']))

        SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))
        SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))
        myDigits = [int(x) for x in list(str(score))]
        width = 0
        for digit in myDigits:
            width += GAME_SPRITES['numbers'][digit].get_width()
        Xoffset = (SCREENWIDTH - width) / 2

        for digit in myDigits:
            SCREEN.blit(GAME_SPRITES['numbers'][digit],
                        (Xoffset, SCREENHEIGHT * 0.12))
            Xoffset += GAME_SPRITES['numbers'][digit].get_width()
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def mainGame_three():
    score = 0
    playerx = int(SCREENWIDTH / 5)
    playery = int(SCREENWIDTH / 2)
    basex = 0

    # Create 2 pipes for blitting on the screen
    newPipe1 = getRandomPipe()
    newPipe2 = getRandomPipe()

    # my List of upper pipes
    upperPipes = [
        {'x': SCREENWIDTH + 200, 'y': newPipe1[0]['y']},
        {'x': SCREENWIDTH + 200 + (SCREENWIDTH / 2), 'y': newPipe2[0]['y']},
    ]
    # my List of lower pipes
    lowerPipes = [
        {'x': SCREENWIDTH + 200, 'y': newPipe1[1]['y']},
        {'x': SCREENWIDTH + 200 + (SCREENWIDTH / 2), 'y': newPipe2[1]['y']},
    ]

    pipeVelX = -4

    playerVelY = -14
    playerMaxVelY = 8
    playerAccY = 1

    playerFlapAccv = -9.5  # velocity while flapping
    playerFlapped = False  # It is true only when the bird is flapping

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                GAME_SOUNDS['off'].play()
                GAME_SOUNDS['hello3'].stop()
                GAME_SOUNDS['Yay'].stop()
                time.sleep(3.4)
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if playery > 0:
                    playerVelY = playerFlapAccv
                    playerFlapped = True
                    GAME_SOUNDS['wing'].play()

        crashTest = isCollide(playerx, playery, upperPipes,
                              lowerPipes)  # This function will return true if the player is crashed
        if crashTest:
            return

            # check for score
        playerMidPos = playerx + GAME_SPRITES['player'].get_width() / 2
        for pipe in upperPipes:
            pipeMidPos = pipe['x'] + GAME_SPRITES['pipe'][0].get_width() / 2
            if pipeMidPos <= playerMidPos < pipeMidPos + 4:
                score += 5
                GAME_SOUNDS['point'].play()
                print(f"Your Score is {score}")
                with open(f"Hiscore.flap") as f:
                    check = f.read()
                    if score > int(check):
                        with open(f"Hiscore.flap", "w") as f:
                            f.write(str(score))

        if playerVelY < playerMaxVelY and not playerFlapped:
            playerVelY += playerAccY

        if playerFlapped:
            playerFlapped = False
        playerHeight = GAME_SPRITES['player'].get_height()
        playery = playery + min(playerVelY, GROUNDY - playery - playerHeight)

        # move pipes to the left
        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
            upperPipe['x'] += pipeVelX
            lowerPipe['x'] += pipeVelX

        # Add a new pipe when the first is about to cross the leftmost part of the screen
        if 0 < upperPipes[0]['x'] < 5:
            newpipe = getRandomPipe()
            upperPipes.append(newpipe[0])
            lowerPipes.append(newpipe[1])

        # if the pipe is out of the screen, remove it
        if upperPipes[0]['x'] < -GAME_SPRITES['pipe'][0].get_width():
            upperPipes.pop(0)
            lowerPipes.pop(0)

        # Lets blit our sprites now
        SCREEN.blit(GAME_SPRITES['background_four'], (0, 0))
        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
            SCREEN.blit(GAME_SPRITES['pipe'][0],
                        (upperPipe['x'], upperPipe['y']))
            SCREEN.blit(GAME_SPRITES['pipe'][1],
                        (lowerPipe['x'], lowerPipe['y']))

        SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))
        SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))
        myDigits = [int(x) for x in list(str(score))]
        width = 0
        for digit in myDigits:
            width += GAME_SPRITES['numbers'][digit].get_width()
        Xoffset = (SCREENWIDTH - width) / 2

        for digit in myDigits:
            SCREEN.blit(GAME_SPRITES['numbers'][digit],
                        (Xoffset, SCREENHEIGHT * 0.12))
            Xoffset += GAME_SPRITES['numbers'][digit].get_width()
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def mainGame_four():
    score = 0
    playerx = int(SCREENWIDTH / 5)
    playery = int(SCREENWIDTH / 2)
    basex = 0

    # Create 2 pipes for blitting on the screen
    newPipe1 = getRandomPipe()
    newPipe2 = getRandomPipe()

    # my List of upper pipes
    upperPipes = [
        {'x': SCREENWIDTH + 200, 'y': newPipe1[0]['y']},
        {'x': SCREENWIDTH + 200 + (SCREENWIDTH / 2), 'y': newPipe2[0]['y']},
    ]
    # my List of lower pipes
    lowerPipes = [
        {'x': SCREENWIDTH + 200, 'y': newPipe1[1]['y']},
        {'x': SCREENWIDTH + 200 + (SCREENWIDTH / 2), 'y': newPipe2[1]['y']},
    ]

    pipeVelX = -4

    playerVelY = -14
    playerMaxVelY = 8
    playerAccY = 1

    playerFlapAccv = -9.5  # velocity while flapping
    playerFlapped = False  # It is true only when the bird is flapping

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                GAME_SOUNDS['off'].play()
                GAME_SOUNDS['hello4'].stop()
                GAME_SOUNDS['Yay'].stop()
                time.sleep(3.4)
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if playery > 0:
                    playerVelY = playerFlapAccv
                    playerFlapped = True
                    GAME_SOUNDS['wing'].play()

        crashTest = isCollide(playerx, playery, upperPipes,
                              lowerPipes)  # This function will return true if the player is crashed
        if crashTest:
            return

            # check for score
        playerMidPos = playerx + GAME_SPRITES['player'].get_width() / 2
        for pipe in upperPipes:
            pipeMidPos = pipe['x'] + GAME_SPRITES['pipe'][0].get_width() / 2
            if pipeMidPos <= playerMidPos < pipeMidPos + 4:
                score += 5
                GAME_SOUNDS['point'].play()
                print(f"Your Score is {score}")
                with open(f"Hiscore.flap") as f:
                    check = f.read()
                    if score > int(check):
                        with open(f"Hiscore.flap", "w") as f:
                            f.write(str(score))

        if playerVelY < playerMaxVelY and not playerFlapped:
            playerVelY += playerAccY

        if playerFlapped:
            playerFlapped = False
        playerHeight = GAME_SPRITES['player'].get_height()
        playery = playery + min(playerVelY, GROUNDY - playery - playerHeight)

        # move pipes to the left
        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
            upperPipe['x'] += pipeVelX
            lowerPipe['x'] += pipeVelX

        # Add a new pipe when the first is about to cross the leftmost part of the screen
        if 0 < upperPipes[0]['x'] < 5:
            newpipe = getRandomPipe()
            upperPipes.append(newpipe[0])
            lowerPipes.append(newpipe[1])

        # if the pipe is out of the screen, remove it
        if upperPipes[0]['x'] < -GAME_SPRITES['pipe'][0].get_width():
            upperPipes.pop(0)
            lowerPipes.pop(0)

        # Lets blit our sprites now
        SCREEN.blit(GAME_SPRITES['background_five'], (0, 0))
        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
            SCREEN.blit(GAME_SPRITES['pipe'][0],
                        (upperPipe['x'], upperPipe['y']))
            SCREEN.blit(GAME_SPRITES['pipe'][1],
                        (lowerPipe['x'], lowerPipe['y']))

        SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))
        SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))
        myDigits = [int(x) for x in list(str(score))]
        width = 0
        for digit in myDigits:
            width += GAME_SPRITES['numbers'][digit].get_width()
        Xoffset = (SCREENWIDTH - width) / 2

        for digit in myDigits:
            SCREEN.blit(GAME_SPRITES['numbers'][digit],
                        (Xoffset, SCREENHEIGHT * 0.12))
            Xoffset += GAME_SPRITES['numbers'][digit].get_width()
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def isCollide(playerx, playery, upperPipes, lowerPipes):
    if playery > GROUNDY - 35 or playery < 0:
        GAME_SOUNDS['hello'].stop()
        GAME_SOUNDS['Yay'].stop()
        GAME_SOUNDS['hello2'].stop()
        GAME_SOUNDS['hello3'].stop()
        GAME_SOUNDS['hello4'].stop()
        GAME_SOUNDS['hit'].play()
        return True

    for pipe in upperPipes:
        pipeHeight = GAME_SPRITES['pipe'][0].get_height()
        if playery < pipeHeight + pipe['y'] and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width():
            GAME_SOUNDS['hello'].stop()
            GAME_SOUNDS['Yay'].stop()
            GAME_SOUNDS['hello2'].stop()
            GAME_SOUNDS['hello3'].stop()
            GAME_SOUNDS['hello4'].stop()
            GAME_SOUNDS['hit'].play()
            return True
        

    for pipe in lowerPipes:
        if (playery + GAME_SPRITES['player'].get_height() > pipe['y']) and abs(playerx - pipe['x']) < \
                GAME_SPRITES['pipe'][0].get_width():
            GAME_SOUNDS['hello'].stop()
            GAME_SOUNDS['Yay'].stop()
            GAME_SOUNDS['hello2'].stop()
            GAME_SOUNDS['hello3'].stop()
            GAME_SOUNDS['hello4'].stop()
            GAME_SOUNDS['hit'].play()
            return True

    return False


def getRandomPipe():
    """
    Generate positions of two pipes(one bottom straight and one top rotated ) for blitting on the screen
    """
    pipeHeight = GAME_SPRITES['pipe'][0].get_height()
    offset = SCREENHEIGHT / 3
    y2 = offset + random.randrange(0, int(SCREENHEIGHT -
                                          GAME_SPRITES['base'].get_height() - 1.1 * offset))
    pipeX = SCREENWIDTH + 24
    y1 = pipeHeight - y2 + offset
    pipe = [
        {'x': pipeX, 'y': -y1},  # upper Pipe
        {'x': pipeX, 'y': y2}  # lower Pipe
    ]
    return pipe

def gameloop():
    # sprite = pygame.sprite.Sprite()
    # sprite.image = GAME_SPRITES['base']
    # sprite.rect = GAME_SPRITES['base'].get_rect()
    screen_text = font.render("Highest Score is "+ score_check, True, (0, 0, 0))
    SCREEN.blit(screen_text, [10, 70])
    
if __name__ == "__main__":
    with open(f"Hiscore.flap") as f:
        score_check = f.read()
    # This will be the main point from where our game will start
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('Flappy Bird+ (Reality)')
    pygame.display.update()
    font = pygame.font.Font('./font/RobotoSlab-VariableFont_wght.ttf', 22)
    # GAME_SOUNDS['on'].play()
    GAME_SPRITES['numbers'] = (
        pygame.image.load('./gallery/numbers/0.png').convert_alpha(),
        pygame.image.load('./gallery/numbers/1.png').convert_alpha(),
        pygame.image.load('./gallery/numbers/2.png').convert_alpha(),
        pygame.image.load('./gallery/numbers/3.png').convert_alpha(),
        pygame.image.load('./gallery/numbers/4.png').convert_alpha(),
        pygame.image.load('./gallery/numbers/5.png').convert_alpha(),
        pygame.image.load('./gallery/numbers/6.png').convert_alpha(),
        pygame.image.load('./gallery/numbers/7.png').convert_alpha(),
        pygame.image.load('./gallery/numbers/8.png').convert_alpha(),
        pygame.image.load('./gallery/numbers/9.png').convert_alpha(),
    )

    GAME_SPRITES['message'] = pygame.image.load(
        './gallery/assets/bg_startup_message.png').convert_alpha()
    GAME_SPRITES['bassee'] = pygame.image.load(
        './gallery/assets/base.png').convert_alpha()
    GAME_SPRITES['base'] = pygame.image.load('./gallery/assets/base_simple.png').convert_alpha()
    GAME_SPRITES['pipe'] = (pygame.transform.rotate(pygame.image.load('./gallery/assets/pipe1.png').convert_alpha(), 180),
                            pygame.image.load(
                                './gallery/assets/pipe.png').convert_alpha()
                            )

    # Game sounds
    GAME_SOUNDS['die'] = pygame.mixer.Sound('./gallery/audio/effects/error.wav')
    GAME_SOUNDS['hit'] = pygame.mixer.Sound('./gallery/audio/effects/hit.wav')
    GAME_SOUNDS['point'] = pygame.mixer.Sound('./gallery/audio/effects/point.wav')
    GAME_SOUNDS['wing'] = pygame.mixer.Sound('./gallery/audio/effects/wing.wav')
    GAME_SOUNDS['off'] = pygame.mixer.Sound('./gallery/audio/effects/logoff.wav')
    GAME_SOUNDS['on'] = pygame.mixer.Sound('./gallery/audio/effects/logon.wav')
    GAME_SOUNDS['Yay'] = pygame.mixer.Sound('./gallery/audio/background/hello_startup.mp3')
    GAME_SOUNDS['hello'] = pygame.mixer.Sound('./gallery/audio/background/hello_game.mp3')
    GAME_SOUNDS['hello2'] = pygame.mixer.Sound('./gallery/audio/background/hello_game2.mp3')
    GAME_SOUNDS['hello3'] = pygame.mixer.Sound('./gallery/audio/background/hello_game3.mp3')
    GAME_SOUNDS['hello4'] = pygame.mixer.Sound('./gallery/audio/background/hello_game4.mp3')

    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
    GAME_SPRITES['background_second'] = pygame.image.load(BACKGROUND_SECOND).convert()
    GAME_SPRITES['background_third'] = pygame.image.load(BACKGROUND_THIRD).convert()
    GAME_SPRITES['background_four'] = pygame.image.load(BACKGROUND_FOUR).convert()
    GAME_SPRITES['background_five'] = pygame.image.load(BACKGROUND_FIVE).convert()
    GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()


##    notification.notify(
##    title="Recommended for Gamers",
##    message="Use Headphones for Best Performance of Background Music",
##    app_icon="icon.ico",
##    timeout=1900
##    )

    while True:
        '''
        window=Tk()
    window.geometry("200x50")
    window.title("Flappy Bird+ (Reality)")
    window.configure(bg="#00d5ff")
    window.iconbitmap("./gallery/icon.png")
    window.resizable(0,0)
    main_til = Label(window, text="BYE", font=("System", 18), bg="#00d5ff")
    main_til.pack(pady=20)
    '''
        welcomeScreen()
        mainGame()
        welcomeScreen_second()
        mainGame_two()
        welcomeScreen_three()
        mainGame_three()
        welcomeScreen_four()
        mainGame_four()

        
