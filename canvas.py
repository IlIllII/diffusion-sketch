import pygame


class Canvas:
    def __init__(self, screen):
        self.actively_drawing = False
        self.screen = screen
        self.temp_canvas = pygame.Surface((512, 512))
        self.temp_canvas.fill((255, 255, 255))
        self.screen_copy = screen.copy()
        self.undo_stack = []

    def get_surface_for_drawing(self):
        if not self.actively_drawing:
            self.screen_copy = self.screen.copy()
            self.actively_drawing = True

        self.screen.blit(self.screen_copy, (0, 0))
        self.temp_canvas.fill((255, 255, 255))
        self.temp_canvas.blit(self.screen_copy, (0, 0))
        return self.temp_canvas

    def save_surface_to_screen(self):
        self.actively_drawing = False
        self.screen.blit(self.temp_canvas, (0, 0))
        self.undo_stack.append(self.screen_copy.copy())

    def blit(self):
        if self.actively_drawing:
            self.screen.blit(self.temp_canvas, (0, 0))
        else:
            self.screen.blit(self.screen, (0, 0))

    def reset(self):
        self.screen.fill((255, 255, 255))
        self.temp_canvas.fill((255, 255, 255))
        self.screen_copy = self.screen.copy()
        self.undo_stack = []

    def undo(self):
        if len(self.undo_stack) > 0:
            self.screen.blit(self.undo_stack.pop(), (0, 0))