import pygame

from roguelike.engine import FRAME_DURATION, MAX_FRAME_SKIP


class Engine:

    def __init__(self):
        self._pygame = pygame
        self._running = False
        self._last_tick = 0

    def start(self):
        """
        Starts the engine for the simulation.
        """
        self._running = True
        self._pygame.init()
        self._step()

    def stop(self):
        """
        Stops the engine and ends the simulation.
        """
        self._running = False

    def _step(self):
        """
        Method for game loop.
        """
        while self._running:
            for event in self._pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False
                if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                    pass
            current_time = self._pygame.time.get_ticks()
            delta = current_time - self._last_tick
            if delta > MAX_FRAME_SKIP:
                delta = MAX_FRAME_SKIP
            self._update(delta)
            self._render(delta / FRAME_DURATION)
            self._last_tick = current_time

    def _update(self, delta):
        """

        :param delta:
        :type delta: float
        """
        while delta >= FRAME_DURATION:
            delta -= FRAME_DURATION

    def _render(self, interpolation):
        """

        :param interpolation:
        :type interpolation: float
        """

    @staticmethod
    def create():
        """
        Static factory method.

        :return: A new engine instance.
        :rtype: Engine
        """
        return Engine()
