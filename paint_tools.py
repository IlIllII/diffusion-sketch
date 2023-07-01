import pygame

from canvas import Canvas

_brush_size = 3

class Tool:
    brush_size = 3

    def __init__(self) -> None:
        pass

    @classmethod
    def increase_brush_size(cls) -> None:
        Tool.brush_size += 1

    @classmethod
    def decrease_brush_size(cls) -> None:
        Tool.brush_size -= 1
        if Tool.brush_size < 1:
            Tool.brush_size = 1

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

    def draw(self, canvas: Canvas, mouse_pos: tuple) -> None:
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

    def handle_event(self, event: pygame.event.Event, canvas: Canvas) -> None:
        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.mouse_down = True
            self.point1 = mouse_pos
            radius = 0
            pygame.draw.circle(
                canvas.get_surface_for_drawing(),
                (0, 0, 0),
                self.point1,
                radius,
                self.brush_size,
            )

        if event.type == pygame.MOUSEMOTION and self.mouse_down:
            distance_x = mouse_pos[0] - self.point1[0]
            distance_y = mouse_pos[1] - self.point1[1]
            radius = int((distance_x**2 + distance_y**2) ** 0.5)
            pygame.draw.circle(
                canvas.get_surface_for_drawing(),
                (0, 0, 0),
                self.point1,
                radius,
                self.brush_size,
            )

        if event.type == pygame.MOUSEBUTTONUP:
            self.mouse_down = False
            distance_x = mouse_pos[0] - self.point1[0]
            distance_y = mouse_pos[1] - self.point1[1]
            radius = int((distance_x**2 + distance_y**2) ** 0.5)
            pygame.draw.circle(
                canvas.get_surface_for_drawing(),
                (0, 0, 0),
                self.point1,
                radius,
                self.brush_size,
            )
            canvas.save_surface_to_screen()


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

    def draw(self, canvas: Canvas, mouse_pos: tuple) -> None:
        pygame.draw.circle(
            self.internal_canvas, (255, 255, 255), mouse_pos, self.brush_size
        )
        canvas.get_surface_for_drawing().blit(self.internal_canvas, (0, 0))


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

    def handle_event(self, event: pygame.event.Event, canvas: Canvas) -> None:
        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.mouse_down = True
            self.point1 = mouse_pos
            radius = 0
            pygame.draw.ellipse(
                canvas.get_surface_for_drawing(),
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
                canvas.get_surface_for_drawing(),
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
                canvas.get_surface_for_drawing(),
                (0, 0, 0),
                pygame.Rect(
                    self.point1[0] - 0.5 * distance_x,
                    self.point1[1] - 0.5 * distance_y,
                    distance_x,
                    distance_y,
                ),
                self.brush_size,
            )
            canvas.save_surface_to_screen()


class PolylineTool(Tool):
    mouse_down = False
    points = []

    def __init__(self) -> None:
        super().__init__()
        self.mouse_down = False
        self.points = []
        self.actively_drawing = False
        self.temp_canvas = None

    def activate(self) -> None:
        self.mouse_down = False
        self.points = []

    def deactivate(self) -> None:
        pass

    def handle_event(self, event: pygame.event.Event, canvas: Canvas) -> None:
        mouse_pos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if not self.actively_drawing:
                self.internal_canvas = canvas.get_surface_for_drawing().copy()
            self.actively_drawing = True
            self.points.append(mouse_pos)
            self.draw(canvas, mouse_pos)

        if event.type == pygame.MOUSEMOTION and self.actively_drawing:
            self.draw(canvas, mouse_pos)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            pygame.draw.lines(
                canvas.get_surface_for_drawing(),
                (0, 0, 0),
                False,
                self.points,
                self.brush_size,
            )
            self.points = []
            self.actively_drawing = False
            canvas.save_surface_to_screen()

    def draw(self, canvas: Canvas, mouse_pos: tuple) -> None:
        if len(self.points) > 1:
            pygame.draw.lines(
                self.internal_canvas, (0, 0, 0), False, self.points, self.brush_size
            )
        if not self.temp_canvas:
            self.temp_canvas = self.internal_canvas.copy()
        self.temp_canvas.blit(self.internal_canvas, (0, 0))
        if len(self.points) > 0:
            pygame.draw.line(
                self.temp_canvas, (0, 0, 0), self.points[-1], mouse_pos, self.brush_size
            )

        canvas.get_surface_for_drawing().blit(self.temp_canvas, (0, 0))


class SplineTool(Tool):
    mouse_down = False
    points = []

    def __init__(self) -> None:
        super().__init__()
        self.mouse_down = False
        self.points = []
        self.actively_drawing = False
        self.temp_canvas = None

    def activate(self) -> None:
        self.mouse_down = False
        self.points = []

    def deactivate(self) -> None:
        pass

    def handle_event(self, event: pygame.event.Event, canvas: Canvas) -> None:
        mouse_pos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if not self.actively_drawing:
                self.internal_canvas = canvas.get_surface_for_drawing().copy()
            self.actively_drawing = True
            self.points.append(mouse_pos)
            self.draw(canvas, mouse_pos)

        if event.type == pygame.MOUSEMOTION and self.actively_drawing:
            self.draw(canvas, mouse_pos)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            canvas.get_surface_for_drawing()  # Hack to reset the temp canvas
            if len(self.points) >= 4:
                vertices = self.get_bspline_vertices()
                pygame.draw.lines(
                    canvas.get_surface_for_drawing(),
                    (0, 0, 0),
                    False,
                    vertices,
                    self.brush_size,
                )
            self.points = []
            self.actively_drawing = False
            canvas.save_surface_to_screen()

    def draw(self, canvas: Canvas, mouse_pos: tuple) -> None:
        if len(self.points) > 1:
            pygame.draw.lines(
                self.internal_canvas, (0, 0, 0), False, self.points, self.brush_size
            )
        if not self.temp_canvas:
            self.temp_canvas = self.internal_canvas.copy()
        self.temp_canvas.blit(self.internal_canvas, (0, 0))
        if len(self.points) > 0:
            pygame.draw.line(
                self.temp_canvas, (0, 0, 0), self.points[-1], mouse_pos, self.brush_size
            )

        canvas.get_surface_for_drawing().blit(self.temp_canvas, (0, 0))

    def get_bspline_vertices(self):
        segments = 100
        if len(self.points) < 4:
            raise Exception("Splines must have at least four control points.")
        self.points = [self.points[0]] + self.points + [self.points[-1]]
        vertices = []
        for i in range(len(self.points) - 3):
            control_points = self.points[i : i + 4]
            for t in range(segments):
                t = t / segments
                B0 = (1 / 6) * (1 - t) ** 3
                B1 = (1 / 6) * (3 * t**3 - 6 * t**2 + 4)
                B2 = (1 / 6) * (-3 * t**3 + 3 * t**2 + 3 * t + 1)
                B3 = (1 / 6) * (t**3)
                bernstein_basis = [B0, B1, B2, B3]
                vertex = [
                    dot4D(bernstein_basis, control_point)
                    for control_point in zip(*control_points)
                ]
                vertices.append(vertex)
        return vertices


def dot4D(v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v, w))
