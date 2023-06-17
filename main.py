import pygame
from render import render_image, generate_image
from paint_tools import PenTool, LineTool, RectTool, CircleTool, EraserTool, EllipseTool


active_tool = EllipseTool()
# tools = ["polyline", "eraser", "circle", "rectangle", "fill", "selection", "freehand"]

tools = {
    pygame.K_1: PenTool(),
    pygame.K_2: LineTool(),
    pygame.K_3: RectTool(),
    pygame.K_4: CircleTool(),
    pygame.K_5: EraserTool(),
    pygame.K_6: EllipseTool(),
    
}

undo_stack = []


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
                undo_stack.append(screen_copy.copy())

            if actively_drawing:
                screen.blit(screen_copy, (0, 0))
                temp_canvas.fill((255, 255, 255))
                temp_canvas.blit(screen_copy, (0, 0))
        

            active_tool.handle_event(event, temp_canvas)

            if actively_drawing:
                screen.blit(temp_canvas, (0, 0))
            else:
                screen.blit(screen, (0, 0))

            pygame.display.flip()





            if event.type == pygame.KEYDOWN:
                
                if event.key in tools and not actively_drawing:
                    active_tool.deactivate()
                    active_tool = tools[event.key]
                    active_tool.activate()
                    print(f"Tool changed to {active_tool.__class__.__name__}")


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
                    undo_stack = []
                    pygame.display.flip()

                if event.key == pygame.K_t:
                    pygame.draw.circle(screen, (0, 0, 0), pygame.mouse.get_pos(), 10)
                
                if event.key == pygame.K_u:
                    if len(undo_stack) > 0:
                        screen.blit(undo_stack.pop(), (0, 0))
                        pygame.display.flip()


    pygame.quit()
