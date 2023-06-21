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
    PolylineTool,
)
from canvas import Canvas



tools = {
    pygame.K_1: PenTool(),
    pygame.K_2: LineTool(),
    pygame.K_3: RectTool(),
    pygame.K_4: CircleTool(),
    pygame.K_5: EraserTool(),
    pygame.K_6: EllipseTool(),
    pygame.K_7: SplineTool(),
    pygame.K_8: PolylineTool(),
}

tool_list = [
    PenTool(),
    LineTool(),
    RectTool(),
    CircleTool(),
    EraserTool(),
    EllipseTool(),
    SplineTool(),
    PolylineTool(),
]

tool_index = 0
active_tool = tool_list[tool_index]


if __name__ == "__main__":
    SCREEN_WIDTH = 512
    SCREEN_HEIGHT = 512
    pygame.init()
    pygame.display.set_caption("Diffusion Sketch!")

    # TODO: remove screen completely and wrap it in the canvas class
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill((255, 255, 255))

    canvas = Canvas(screen)
    active_tool.activate()
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            active_tool.handle_event(event, canvas)
            canvas.blit()

            if event.type == pygame.KEYDOWN:
                if event.key in tools:  # Crashes if actively drawing, probably
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
                
                if event.key == pygame.K_LEFT:
                    tool_index = (tool_index - 1) % len(tools)
                    active_tool = tool_list[tool_index]
                    active_tool.activate()
                if event.key == pygame.K_RIGHT:
                    tool_index = (tool_index + 1) % len(tools)
                    active_tool = tool_list[tool_index]
                    active_tool.activate()
                
                if event.key == pygame.K_UP:
                    active_tool.increase_brush_size()
                if event.key == pygame.K_DOWN:
                    active_tool.decrease_brush_size()

            pygame.display.flip()

    pygame.quit()
