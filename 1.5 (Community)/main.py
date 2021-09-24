# Flappy Bird of Reality Game
# Starts Here
# Dwijottam Dutta

import random
import pygame
import sys
from pygame.locals import *
import time
from plyer import notification

# Global Variables
FPS = 32
SCREENWIDTH = 287  # 287
SCREENHEIGHT = 511
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GROUNDY = SCREENHEIGHT * 0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = './gallery/bird1.png'
BACKGROUND = './gallery/background1.png'
BACKGROUND_SECOND = './gallery/background1-1.png'

notification.notify(
    title="Recommended for Community Users",
    message="Use Headphones for Best Performance of Background Music",
    app_icon="icon.ico",
    timeout=10
)


def welcomeScreen():
    """
    Shows welcome images on the screen
    """
    GAME_SOUNDS['Yay'].play(-1)
    GAME_SOUNDS['hello'].stop()
    playerx = int(SCREENWIDTH / 9)
    playery = int((SCREENHEIGHT - GAME_SPRITES['player'].get_height()) / 3)
    messagex = int((SCREENWIDTH - GAME_SPRITES['message'].get_width()) / 2)
    gameIcon = pygame.image.load('./gallery/icon.png')
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


def welcomeScreen_two():
    """
    Shows welcome images on the screen
    """
    GAME_SOUNDS['Yay'].play(-1)
    GAME_SOUNDS['hello'].stop()
    playerx = int(SCREENWIDTH / 9)
    playery = int((SCREENHEIGHT - GAME_SPRITES['player'].get_height()) / 3)
    messagex = int((SCREENWIDTH - GAME_SPRITES['message'].get_width()) / 2)
    gameIcon = pygame.image.load('./gallery/icon.png')
    pygame.display.set_icon(gameIcon)
    messagey = int(SCREENHEIGHT * 0.01)
    basex = 0
    while True:
        for event in pygame.event.get():
            # if user clicks on cross button, close the game
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                GAME_SOUNDS['off'].play()
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
                SCREEN.blit(GAME_SPRITES['background_second'], (0, 0))
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

    playerFlapAccv = -8  # velocity while flapping
    playerFlapped = False  # It is true only when the bird is flapping

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
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
                print(f"Your Score is {score}")
                GAME_SOUNDS['point'].play()

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
        SCREEN.blit(GAME_SPRITES['background'], (0, 0))
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
                w = open("Hiscore.flap", "w")
                w.write("~ ~ ~ ~ ~ WELCOME to Flappy Bird+ of Reality ~ ~ ~ ~ ~\n")
                w.write("   \n")
                w.write("Congratulations !\n")
                w.write("Your Highest Score is ")
                w.write(str(score))
                # print(hiscore)

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


def isCollide(playerx, playery, upperPipes, lowerPipes):
    if playery > GROUNDY - 35 or playery < 0:
        GAME_SOUNDS['hello'].stop()
        GAME_SOUNDS['Yay'].stop()
        GAME_SOUNDS['hit'].play()
        return True

    for pipe in upperPipes:
        pipeHeight = GAME_SPRITES['pipe'][0].get_height()
        if playery < pipeHeight + pipe['y'] and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width():
            GAME_SOUNDS['hello'].stop()
            GAME_SOUNDS['Yay'].stop()
            GAME_SOUNDS['hit'].play()
            return True

    for pipe in lowerPipes:
        if (playery + GAME_SPRITES['player'].get_height() > pipe['y']) and abs(playerx - pipe['x']) < \
                GAME_SPRITES['pipe'][0].get_width():
            GAME_SOUNDS['hello'].stop()
            GAME_SOUNDS['Yay'].stop()
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


if __name__ == "__main__":
    # This will be the main point from where our game will start
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('Flappy Bird+ (Reality)')
    GAME_SPRITES['numbers'] = (
        pygame.image.load('./gallery/0.png').convert_alpha(),
        pygame.image.load('./gallery/1.png').convert_alpha(),
        pygame.image.load('./gallery/2.png').convert_alpha(),
        pygame.image.load('./gallery/3.png').convert_alpha(),
        pygame.image.load('./gallery/4.png').convert_alpha(),
        pygame.image.load('./gallery/5.png').convert_alpha(),
        pygame.image.load('./gallery/6.png').convert_alpha(),
        pygame.image.load('./gallery/7.png').convert_alpha(),
        pygame.image.load('./gallery/8.png').convert_alpha(),
        pygame.image.load('./gallery/9.png').convert_alpha(),
    )

    GAME_SPRITES['message'] = pygame.image.load(
        './gallery/Background_basic.png').convert_alpha()
    GAME_SPRITES['bassee'] = pygame.image.load(
        './gallery/base.png').convert_alpha()
    GAME_SPRITES['base'] = pygame.image.load('./gallery/base_simple.png').convert_alpha()
    GAME_SPRITES['pipe'] = (pygame.transform.rotate(pygame.image.load('./gallery/pipe1.png').convert_alpha(), 180),
                            pygame.image.load(
                                './gallery/pipe.png').convert_alpha()
                            )

    # Game sounds
    GAME_SOUNDS['die'] = pygame.mixer.Sound('./gallery/error.wav')
    GAME_SOUNDS['hit'] = pygame.mixer.Sound('./gallery/hit.wav')
    GAME_SOUNDS['point'] = pygame.mixer.Sound('./gallery/point.wav')
    GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('./gallery/swoosh.wav')
    GAME_SOUNDS['wing'] = pygame.mixer.Sound('./gallery/wing.wav')
    GAME_SOUNDS['off'] = pygame.mixer.Sound('./gallery/logoff.wav')
    GAME_SOUNDS['on'] = pygame.mixer.Sound('./gallery/logon.wav')
    GAME_SOUNDS['Yay'] = pygame.mixer.Sound('./gallery/hello_startup.mp3')
    GAME_SOUNDS['hello'] = pygame.mixer.Sound('./gallery/hello_game.mp3')

    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
    GAME_SPRITES['background_second'] = pygame.image.load(BACKGROUND_SECOND).convert()
    GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()

    while True:
        welcomeScreen()  # Welcome Screen
        mainGame()
        welcomeScreen_two()
        mainGame_two()
