import pygame
from pygame.locals import *

MILLISECONDS = 1000
FRAME_RATE = 60
FRAME_DURATION = MILLISECONDS / FRAME_RATE
MAX_FRAME_SKIP = 5


class Engine:

    def __init__(self):
        self._running = False
        self._currentTick = 0
        self._lastTick = 0
        self._delta = 0
        self._pygame = pygame

    def stop(self):
        self._running = False

    def main(self):
        while self._running:
            for event in self._pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False
                elif event.type == pygame.KEYDOWN:
                    pass
            self._pygame.display.flip()

    def start(self):
        self._running = True
        self._pygame.init()
        screen = self._pygame.display.set_mode((640, 480))
        self._pygame.display.set_caption('ECS Python')
        background = self._pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        clock = self._pygame.time.Clock()
        self._lastTick = self._pygame.time.get_ticks()
        self.main()
