import pygame
from ui import UI


class Canvas:
    def __init__(self, screen):
        # TODO: Perform targed blits to reduce number of screens
        self.actively_drawing = False
        self.final_screen = screen
        self.screen = self.final_screen.copy()
        self.temp_canvas = screen.copy()
        self.temp_canvas.fill((255, 255, 255))
        self.screen_copy = screen.copy()
        self.undo_stack = []
        self.ui = screen.copy()

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

        # TODO: extract ui drawing code
        ui_canvas = self.get_ui()
        mouse_pos = pygame.mouse.get_pos()
        pygame.draw.line(
            ui_canvas,
            (0, 0, 0),
            (mouse_pos[0], mouse_pos[1] + 10),
            (mouse_pos[0], mouse_pos[1] - 10),
            3,
        )
        pygame.draw.line(
            ui_canvas,
            (0, 0, 0),
            (mouse_pos[0] + 10, mouse_pos[1]),
            (mouse_pos[0] - 10, mouse_pos[1]),
            3,
        )


        self.final_screen.blit(ui_canvas, (0, 0))

    def reset(self):
        self.screen.fill((255, 255, 255))
        self.temp_canvas.fill((255, 255, 255))
        self.screen_copy = self.screen.copy()
        self.undo_stack = []

    def undo(self):
        if len(self.undo_stack) > 0:
            self.screen.blit(self.undo_stack.pop(), (0, 0))

    def get_ui(self):
        self.ui.blit(self.screen, (0, 0))
        return self.ui
    
    def blit_ui(self, display_help, brush_size, current_tool):
        ui = UI()
        self.ui = ui.get_ui(self.final_screen, brush_size, current_tool, display_help)
        self.final_screen.blit(self.ui, (0, 0))
