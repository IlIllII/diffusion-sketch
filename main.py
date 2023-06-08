import pygame
from render import render_image, generate_image
from paint_tools import PenTool, LineTool


active_tool = PenTool()
# tools = ["polyline", "eraser", "circle", "rectangle", "fill", "selection", "freehand"]





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
        

            active_tool.handle_event(event, temp_canvas)

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
