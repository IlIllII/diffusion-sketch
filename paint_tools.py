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


class Tool:
    def __init__(self) -> None:
        self.brush_size = 3

    def activate(self) -> None:
        pass

    def deactivate(self) -> None:
        pass

    def handle_event(self, event: pygame.event.Event, canvas: Canvas) -> None:
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

    def handle_event(self, event: pygame.event.Event, canvas: Canvas) -> None:
        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.mouse_down = True
            self.point1 = mouse_pos
            pygame.draw.line(
                canvas.get_surface_for_drawing(),
                (0, 0, 0),
                self.point1,
                self.point1,
                self.brush_size,
            )

        if event.type == pygame.MOUSEMOTION and self.mouse_down:
            pygame.draw.line(
                canvas.get_surface_for_drawing(),
                (0, 0, 0),
                self.point1,
                mouse_pos,
                self.brush_size,
            )

        if event.type == pygame.MOUSEBUTTONUP:
            self.mouse_down = False
            pygame.draw.line(
                canvas.get_surface_for_drawing(),
                (0, 0, 0),
                self.point1,
                mouse_pos,
                self.brush_size,
            )
            canvas.save_surface_to_screen()
            # self.stop_drawing()

        # self.screen.blit(self.canvas, (0, 0))


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

    def handle_event(self, event: pygame.event.Event, canvas: Canvas) -> None:
        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.internal_canvas = canvas.get_surface_for_drawing().copy()
            self.draw(canvas, mouse_pos)
            self.mouse_down = True

        if event.type == pygame.MOUSEMOTION and self.mouse_down:
            self.draw(canvas, mouse_pos)

        if event.type == pygame.MOUSEBUTTONUP:
            self.draw(canvas, mouse_pos)
            self.internal_canvas = None
            self.mouse_down = False
            canvas.save_surface_to_screen()

    def draw(self, canvas: pygame.event.Event, mouse_pos: tuple) -> None:
        pygame.draw.circle(self.internal_canvas, (0, 0, 0), mouse_pos, self.brush_size)
        canvas.get_surface_for_drawing().blit(self.internal_canvas, (0, 0))


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

    def handle_event(self, event: pygame.event.Event, canvas: Canvas) -> None:
        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.mouse_down = True
            self.point1 = mouse_pos
            left = min(self.point1[0], mouse_pos[0])
            top = min(self.point1[1], mouse_pos[1])
            width = abs(self.point1[0] - mouse_pos[0])
            height = abs(self.point1[1] - mouse_pos[1])
            pygame.draw.rect(
                canvas.get_surface_for_drawing(),
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
                canvas.get_surface_for_drawing(),
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
                canvas.get_surface_for_drawing(),
                (0, 0, 0),
                pygame.Rect(left, top, width, height),
                self.brush_size,
            )
            canvas.save_surface_to_screen()


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
                pygame.Rect(
                    self.point1[0] - 0.5 * distance_x,
                    self.point1[1] - 0.5 * distance_y,
                    distance_x,
                    distance_y,
                ),
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
                pygame.Rect(
                    self.point1[0] - 0.5 * distance_x,
                    self.point1[1] - 0.5 * distance_y,
                    distance_x,
                    distance_y,
                ),
                self.brush_size,
            )


class SplineTool(Tool):
    mouse_down = False
    points = []

    def __init__(self) -> None:
        super().__init__()
        self.mouse_down = False
        self.point1 = (0, 0)

    def activate(self) -> None:
        self.mouse_down = False
        self.points = []

    def deactivate(self) -> None:
        pass

    def handle_event(self, event: pygame.event.Event, canvas: pygame.Surface) -> None:
        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.points.append(mouse_pos)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            pygame.draw.lines(canvas, (0, 0, 0), False, self.points, self.brush_size)
            self.points = []
