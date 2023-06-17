import pygame


class Tool:
    def __init__(self) -> None:
        self.brush_size = 3
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
            pygame.draw.line(
                canvas, (0, 0, 0), self.point1, self.point1, self.brush_size
            )

        if event.type == pygame.MOUSEMOTION and self.mouse_down:
            pygame.draw.line(canvas, (0, 0, 0), self.point1, mouse_pos, self.brush_size)

        if event.type == pygame.MOUSEBUTTONUP:
            self.mouse_down = False
            pygame.draw.line(canvas, (0, 0, 0), self.point1, mouse_pos, self.brush_size)


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
        pygame.draw.circle(self.internal_canvas, (0, 0, 0), mouse_pos, self.brush_size)
        canvas.blit(self.internal_canvas, (0, 0))


class RectTool(Tool):
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
            left = min(self.point1[0], mouse_pos[0])
            top = min(self.point1[1], mouse_pos[1])
            width = abs(self.point1[0] - mouse_pos[0])
            height = abs(self.point1[1] - mouse_pos[1])
            pygame.draw.rect(
                canvas,
                (0, 0, 0),
                pygame.Rect(left, top, width, height),
                self.brush_size,
            )

        if event.type == pygame.MOUSEMOTION and self.mouse_down:
            left = min(self.point1[0], mouse_pos[0])
            top = min(self.point1[1], mouse_pos[1])
            width = abs(self.point1[0] - mouse_pos[0])
            height = abs(self.point1[1] - mouse_pos[1])
            pygame.draw.rect(
                canvas,
                (0, 0, 0),
                pygame.Rect(left, top, width, height),
                self.brush_size,
            )

        if event.type == pygame.MOUSEBUTTONUP:
            self.mouse_down = False
            left = min(self.point1[0], mouse_pos[0])
            top = min(self.point1[1], mouse_pos[1])
            width = abs(self.point1[0] - mouse_pos[0])
            height = abs(self.point1[1] - mouse_pos[1])
            pygame.draw.rect(
                canvas,
                (0, 0, 0),
                pygame.Rect(left, top, width, height),
                self.brush_size,
            )


class CircleTool(Tool):
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
            radius = 0
            pygame.draw.circle(canvas, (0, 0, 0), self.point1, radius, self.brush_size)

        if event.type == pygame.MOUSEMOTION and self.mouse_down:
            distance_x = mouse_pos[0] - self.point1[0]
            distance_y = mouse_pos[1] - self.point1[1]
            radius = int((distance_x**2 + distance_y**2) ** 0.5)
            pygame.draw.circle(canvas, (0, 0, 0), self.point1, radius, self.brush_size)

        if event.type == pygame.MOUSEBUTTONUP:
            self.mouse_down = False
            distance_x = mouse_pos[0] - self.point1[0]
            distance_y = mouse_pos[1] - self.point1[1]
            radius = int((distance_x**2 + distance_y**2) ** 0.5)
            pygame.draw.circle(canvas, (0, 0, 0), self.point1, radius, self.brush_size)


class EraserTool(Tool):
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
        pygame.draw.circle(
            self.internal_canvas, (255, 255, 255), mouse_pos, self.brush_size
        )
        canvas.blit(self.internal_canvas, (0, 0))


class EllipseTool(Tool):
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
            radius = 0
            pygame.draw.ellipse(
                canvas,
                (0, 0, 0),
                pygame.Rect(self.point1[0], self.point1[1], 0, 0),
                self.brush_size,
            )

        if event.type == pygame.MOUSEMOTION and self.mouse_down:
            distance_x = mouse_pos[0] - self.point1[0]
            distance_y = mouse_pos[1] - self.point1[1]
            radius = int((distance_x**2 + distance_y**2) ** 0.5)
            distance_x = distance_x if distance_x > 0 else -distance_x
            distance_y = distance_y if distance_y > 0 else -distance_y
            pygame.draw.ellipse(
                canvas,
                (0, 0, 0),
                pygame.Rect(self.point1[0] - 0.5 * distance_x, self.point1[1] - 0.5 * distance_y, distance_x, distance_y),
                self.brush_size,
            )

        if event.type == pygame.MOUSEBUTTONUP:
            self.mouse_down = False
            distance_x = mouse_pos[0] - self.point1[0]
            distance_y = mouse_pos[1] - self.point1[1]
            radius = int((distance_x**2 + distance_y**2) ** 0.5)
            distance_x = distance_x if distance_x > 0 else -distance_x
            distance_y = distance_y if distance_y > 0 else -distance_y
            pygame.draw.ellipse(
                canvas,
                (0, 0, 0),
                pygame.Rect(self.point1[0] - 0.5 * distance_x, self.point1[1] - 0.5 * distance_y, distance_x, distance_y),
                self.brush_size,
            )
