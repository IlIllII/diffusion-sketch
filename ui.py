import pygame

class UI:
    def __init__(self) -> None:
        self.ui = None
        self.ui_elements = []
    
    def help_elements(self):
        font = pygame.font.SysFont("Arial", 20)
        tool_help = font.render("Use left and right arrow keys to change tools", True, (0, 0, 0))
        brush_size_help = font.render("Use up and down arrow keys to change brush size", True, (0, 0, 0))
        clear_help = font.render("Press 'c' to clear drawing", True, (0, 0, 0))
        undo_help = font.render("Press 'u' to undo", True, (0, 0, 0))
        save_help = font.render("Press 's' to generate AI art", True, (0, 0, 0))
        quit_help = font.render("Press ESCAPE to quit", True, (0, 0, 0))

        return [
            tool_help,
            brush_size_help,
            clear_help,
            undo_help,
            save_help,
            quit_help
        ]

    def drawing_elements(self, brush_size, current_tool):
        font = pygame.font.SysFont("Arial", 20)
        brush_ui = font.render(f"Brush Size: {brush_size}", True, (0, 0, 0))
        tool_ui = font.render(f"Tool: {current_tool}", True, (0, 0, 0))
        help_text = font.render("Hold 'h' for help", True, (0, 0, 0))

        return [
            brush_ui,
            tool_ui,
            help_text
        ]

    def draw_elements(self, at, elements):
        pos = at
        for element in elements:
            self.ui.blit(element, pos)
            pos = (pos[0], pos[1] + 30)

    def get_ui(self, screen, brush_size, current_tool, display_help):
        if not self.ui:
            self.ui = screen.copy()
        
        self.ui.blit(screen, (0, 0))

        if display_help:
            pygame.draw.rect(self.ui, (255, 255, 255), (31, 31, 450, 450), 0, 20)
            pygame.draw.rect(self.ui, (0, 0, 0), (31, 31, 450, 450), 2, 20)
            self.draw_elements((40, 40), self.help_elements())
        else:
            self.draw_elements((20, 15), self.drawing_elements(brush_size, current_tool))

        return self.ui

    
    
    
