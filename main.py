import pygame
from render import render_image, generate_image
from paint_tools import (
    PenTool,
    LineTool,
    RectTool,
    CircleTool,
    EraserTool,
    EllipseTool,
    SplineTool,
    Canvas,
)


active_tool = SplineTool()

tools = {
    pygame.K_1: PenTool(),
    pygame.K_2: LineTool(),
    pygame.K_3: RectTool(),
    pygame.K_4: CircleTool(),
    pygame.K_5: EraserTool(),
    pygame.K_6: EllipseTool(),
    pygame.K_7: SplineTool(),
}


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Diffusion Sketch!")

    # TODO: remove screen completely and wrap it in the canvas class
    screen = pygame.display.set_mode((512, 512))
    screen.fill((255, 255, 255))

    canvas = Canvas(screen)
    active_tool.activate()
    pygame.display.flip()

    button_down = False
    actively_drawing = False

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            active_tool.handle_event(event, canvas)
            canvas.blit()

            if event.type == pygame.KEYDOWN:
                if event.key in tools and not actively_drawing:
                    active_tool.deactivate()
                    active_tool = tools[event.key]
                    active_tool.activate()
                    print(f"Tool changed to {active_tool.__class__.__name__}")

                if event.key == pygame.K_BACKSPACE:
                    pass
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_s:
                    pygame.image.save(screen, "screenshot.png")
                    print("Screenshot saved!")
                    generate_image()

                if event.key == pygame.K_c:
                    canvas.reset()

                if event.key == pygame.K_t:
                    pygame.draw.circle(screen, (0, 0, 0), pygame.mouse.get_pos(), 10)

                if event.key == pygame.K_u:
                    canvas.undo()

            pygame.display.flip()

    pygame.quit()
