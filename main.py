import pygame
from render import render_image, generate_image
from paint_tools import PenTool, LineTool, RectTool, CircleTool, EraserTool, EllipseTool, SplineTool, Canvas


active_tool = LineTool()
# tools = ["polyline", "eraser", "circle", "rectangle", "fill", "selection", "freehand"]

tools = {
    pygame.K_1: PenTool(),
    pygame.K_2: LineTool(),
    pygame.K_3: RectTool(),
    pygame.K_4: CircleTool(),
    pygame.K_5: EraserTool(),
    pygame.K_6: EllipseTool(),
    pygame.K_7: SplineTool(),
}



# class Canvas:
#     def __init__(self, screen, undo_stack):
#         self.actively_drawing = False
#         self.screen = screen
#         self.temp_canvas = pygame.Surface((512, 512))
#         self.temp_canvas.fill((255, 255, 255))
#         self.screen_copy = screen.copy()
#         self.active_tool = LineTool()
#         self.active_tool.activate(self.temp_canvas, self.screen, self.screen_copy)
    
#     def get_surface_for_drawing(self):
#         if not actively_drawing:
#             self.screen_copy = self.screen.copy()
#             self.actively_drawing = True
        
#         self.screen.blit(self.screen_copy, (0, 0))
#         self.temp_canvas.fill((255, 255, 255))
#         self.temp_canvas.blit(self.screen_copy, (0, 0))
#         return self.temp_canvas

#     def end_undoable_draw(self):
#         self.actively_drawing = False
#         self.screen.blit(self.temp_canvas, (0, 0))
#         undo_stack.append(self.screen_copy.copy())


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Diffusion Sketch!")
    screen = pygame.display.set_mode((512, 512))
    temp_canvas = pygame.Surface((512, 512))
    screen.fill((255, 255, 255))
    temp_canvas.fill((255, 255, 255))
    pygame.display.flip()
    screen_copy = screen.copy()
    canvas = Canvas(screen)
    active_tool.activate()

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
