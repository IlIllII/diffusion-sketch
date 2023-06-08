import pygame
from render import render_image, generate_image

dragging = False
first_point = (0, 0)
second_point = (0, 0)
lines = []
dragging_line = None


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

    def draw(self, canvas, mouse_pos):
        pygame.draw.circle(self.internal_canvas, (0, 0, 0), mouse_pos, 3)
        canvas.blit(self.internal_canvas, (0, 0))


active_tool = PenTool()
tools = ["polyline", "eraser", "circle", "rectangle", "fill", "selection", "freehand"]


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Diffusion Sketch!")
    screen = pygame.display.set_mode((512, 512))
    temp_canvas = pygame.Surface((512, 512))
    screen.fill((255, 255, 255))
    temp_canvas.fill((255, 255, 255))
    pygame.display.flip()
    active_tool.activate()
    screen_copy = screen.copy()

    button_down = False
    actively_drawing = False

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                actively_drawing = True
                screen_copy = screen.copy()

            if event.type == pygame.MOUSEBUTTONUP:
                actively_drawing = False
                screen.blit(temp_canvas, (0, 0))

            if actively_drawing:
                screen.blit(screen_copy, (0, 0))
                temp_canvas.fill((255, 255, 255))
                temp_canvas.blit(screen_copy, (0, 0))

            actively_drawing = active_tool.handle_event(event, temp_canvas)

            if actively_drawing:
                screen.blit(temp_canvas, (0, 0))
            else:
                screen.blit(screen, (0, 0))

            pygame.display.flip()

            # if event.type == pygame.MOUSEMOTION:
            #     if dragging:
            #         second_point = pygame.mouse.get_pos()
            #         dragging_line = (first_point, second_point)
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if active_tool is not None:
            #         active_tool.draw(screen)
            #     if dragging:
            #         lines.append(dragging_line)
            #         dragging = False
            #     else:
            #         dragging = True
            #         first_point = pygame.mouse.get_pos()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if len(lines) > 0:
                        lines.pop()
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_s:
                    pygame.image.save(screen, "screenshot.png")
                    print("Screenshot saved!")
                    generate_image()

                if event.key == pygame.K_c:
                    screen.fill((255, 255, 255))
                    lines = []
                    pygame.display.flip()

                if event.key == pygame.K_t:
                    pygame.draw.circle(screen, (0, 0, 0), pygame.mouse.get_pos(), 10)

        # screen.fill((255, 255, 255))

        # for line in lines:
        # pygame.draw.line(screen, (0, 0, 0), line[0], line[1], 3)

        # if dragging_line:
        # pygame.draw.line(screen, (0, 0, 0), dragging_line[0], dragging_line[1])

        # pygame.display.flip()

    pygame.quit()
