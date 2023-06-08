import pygame


class Tool:
    def __init__(self) -> None:
        pass

    def activate(self) -> None:
        pass

    def deactivate(self) -> None:
        pass

    def handle_event(self, event: pygame.event.Event, canvas: pygame.Surface) -> None:
        pass


class LineTool(Tool):
    mouse_down = False
    point1 = (0, 0)

    def __init__(self) -> None:
        super().__init__()
        self.mouse_down = False
        self.point1 = (0, 0)

    def activate(self) -> None:
        self.mouse_down = False
        self.point1 = (0, 0)

    def deactivate(self) -> None:
        pass

    def handle_event(self, event: pygame.event.Event, canvas: pygame.Surface) -> None:
        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.mouse_down = True
            self.point1 = mouse_pos
            pygame.draw.line(canvas, (0, 0, 0), self.point1, self.point1, 3)

        if event.type == pygame.MOUSEMOTION and self.mouse_down:
            pygame.draw.line(canvas, (0, 0, 0), self.point1, mouse_pos, 3)

        if event.type == pygame.MOUSEBUTTONUP:
            self.mouse_down = False
            pygame.draw.line(canvas, (0, 0, 0), self.point1, mouse_pos, 3)


class PenTool(Tool):
    mouse_down = False
    internal_canvas = None

    def __init__(self) -> None:
        super().__init__()
        self.mouse_down = False
        self.internal_canvas = None

    def activate(self) -> None:
        self.mouse_down = False
        self.internal_canvas = None

    def deactivate(self) -> None:
        pass

    def handle_event(self, event: pygame.event.Event, canvas: pygame.Surface) -> None:
        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.internal_canvas = canvas.copy()
            self.draw(canvas, mouse_pos)
            self.mouse_down = True

        if event.type == pygame.MOUSEMOTION and self.mouse_down:
            self.draw(canvas, mouse_pos)

        if event.type == pygame.MOUSEBUTTONUP:
            self.draw(canvas, mouse_pos)
            self.internal_canvas = None
            self.mouse_down = False

    def draw(self, canvas: pygame.event.Event, mouse_pos: tuple) -> None:
        pygame.draw.circle(self.internal_canvas, (0, 0, 0), mouse_pos, 3)
        canvas.blit(self.internal_canvas, (0, 0))
