import pygame
import math
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drawing App")

# Colors
colorWHITE = (255, 255, 255)
colorBLACK = (0, 0, 0)
colorRED = (255, 0, 0)
colorGREEN = (0, 255, 0)
colorBLUE = (0, 0, 255)

# Initial parameters
screen.fill(colorBLACK)
LMBpressed = False
RMBpressed = False
THICKNESS = 5
mode = "brush"  # brush, rect, circle, square, r_triangle, e_triangle, rhombus
prevX = prevY = 0
startX = startY = 0
rect = pygame.Rect(0, 0, 0, 0)
circle = pygame.Rect(0, 0, 0, 0)
square = pygame.Rect(0, 0, 0, 0)
rhombus = []
rects = []
circles = []
squares = []
r_triangles = []
r_triangle = []
e_triangles = []
e_triangle = []
rhombuses = []
drawing_surface = screen.copy()
curr_color = colorRED
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

done = False
while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_1:
        mode = "brush"
      elif event.key == pygame.K_2:
        mode = "rect"
      elif event.key == pygame.K_3:
        mode = "circle"
      elif event.key == pygame.K_4:
        mode = "square"
      elif event.key == pygame.K_5:
        mode = "r_triangle"
      elif event.key == pygame.K_6:
        mode = "e_triangle"
      elif event.key == pygame.K_7:
        mode = "rhombus"
      elif event.key in (pygame.K_EQUALS, pygame.K_PLUS, pygame.K_KP_PLUS):
        THICKNESS += 1
      elif event.key in (pygame.K_MINUS, pygame.K_KP_MINUS):
        THICKNESS = max(1, THICKNESS - 1)
      elif event.key == pygame.K_c:
        screen.fill(colorBLACK)
        rects.clear()
        circles.clear()
        r_triangles.clear()
        squares.clear()
        e_triangles.clear()
        rhombuses.clear()
        drawing_surface = screen.copy()
      elif event.key == pygame.K_r:
        curr_color = colorRED
      elif event.key == pygame.K_g:
        curr_color = colorGREEN
      elif event.key == pygame.K_b:
        curr_color = colorBLUE

    elif event.type == pygame.MOUSEBUTTONDOWN:
      if event.button == 1:
        LMBpressed = True
        prevX, prevY = event.pos
        if mode == "rect":
          startX, startY = event.pos
          rect = pygame.Rect(startX, startY, 0, 0)
        elif mode == "circle":
          startX, startY = event.pos
          circle = pygame.Rect(startX, startY, 0, 0)
        elif mode == "square":
          startX, startY = event.pos
          square = pygame.Rect(startX, startY, 0, 0)
        elif mode == "r_triangle":
          startX, startY = event.pos
          r_triangle = [(startX, startY), (startX, startY), (startX, startY)]
        elif mode == "e_triangle":
          startX, startY = event.pos
          e_triangle = [(startX, startY), (startX, startY), (startX, startY)]
        elif mode == "rhombus":
          startX, startY = event.pos
          rhombus = [(startX, startY), (startX, startY), (startX, startY), (startX, startY)]
      elif event.button == 3:
        RMBpressed = True
        prevX, prevY = event.pos

    elif event.type == pygame.MOUSEMOTION:
      currX, currY = event.pos
      if LMBpressed and mode == "brush":
        pygame.draw.line(drawing_surface, curr_color, (prevX, prevY), (currX, currY), THICKNESS)
        prevX, prevY = currX, currY
      elif LMBpressed and mode == "rect":
        rect.x = min(startX, currX)
        rect.y = min(startY, currY)
        rect.width = abs(currX - startX)
        rect.height = abs(currY - startY)
      elif LMBpressed and mode == "circle":
        radius = max(abs(currX - startX), abs(currY - startY)) // 2
        circle.x = startX - radius
        circle.y = startY - radius
        circle.width = circle.height = radius * 2
      elif LMBpressed and mode == "square":
        square.x = min(startX, currX)
        square.y = min(startY, currY)
        square.width = abs(currX - startX)
        square.height = abs(currX - startX)
      elif LMBpressed and mode == "r_triangle":
        r_triangle = [(currX, currY), (startX, startY), (startX, currY)]
      elif LMBpressed and mode == "e_triangle":
        side = abs(currX - startX)
        height = (math.sqrt(3) / 2) * side
        e_triangle = [
            (startX, startY),
            (startX + side, startY),
            (startX + side / 2, startY - height)
        ]
      elif LMBpressed and mode == "rhombus":
        centerX = (startX + currX) // 2
        centerY = (startY + currY) // 2
        width = abs(currX - startX)
        height = abs(currY - startY)
        rhombus = [
          (centerX - width // 2, centerY),
          (centerX, centerY - height // 2),
          (centerX + width // 2, centerY),
          (centerX, centerY + height // 2)
        ]
      elif RMBpressed:
        pygame.draw.line(drawing_surface, colorBLACK, (prevX, prevY), (currX, currY), THICKNESS)
        prevX, prevY = currX, currY

    elif event.type == pygame.MOUSEBUTTONUP:
      if event.button == 1:
        LMBpressed = False
        if mode == "rect":
          rects.append((rect.copy(), curr_color))
        elif mode == "circle":
          circles.append((circle.copy(), curr_color))
        elif mode == "square":
          squares.append((square.copy(), curr_color))
        elif mode == "r_triangle" and len(r_triangle) == 3:
          r_triangles.append((r_triangle.copy(), curr_color))
        elif mode == "e_triangle" and len(e_triangle) == 3:
          e_triangles.append((e_triangle.copy(), curr_color))
        elif mode == "rhombus" and len(rhombus) == 4:
          rhombuses.append((rhombus.copy(), curr_color))
      elif event.button == 3:
        RMBpressed = False

  # Redraw screen
  screen.blit(drawing_surface, (0, 0))
  for r, color in rects:
    pygame.draw.rect(screen, color, r, THICKNESS)
  for c, color in circles:
    pygame.draw.ellipse(screen, color, c, THICKNESS)
  for s, color in squares:
    pygame.draw.rect(screen, color, s, THICKNESS)
  for r, color in r_triangles:
    pygame.draw.polygon(screen, color, r, THICKNESS)
  for e, color in e_triangles:
    pts = [(int(x), int(y)) for x, y in e]
    pygame.draw.polygon(screen, color, pts, THICKNESS)
  for rh, color in rhombuses:
    pygame.draw.polygon(screen, color, rh, THICKNESS)

  # Draw current shape preview
  if LMBpressed and mode == "rect":
    pygame.draw.rect(screen, curr_color, rect, THICKNESS)
  elif LMBpressed and mode == "circle":
    pygame.draw.ellipse(screen, curr_color, circle, THICKNESS)
  elif LMBpressed and mode == "square":
    pygame.draw.rect(screen, curr_color, square, THICKNESS)
  elif LMBpressed and mode == "r_triangle" and len(r_triangle) == 3:
    pygame.draw.polygon(screen, curr_color, r_triangle, THICKNESS)
  elif LMBpressed and mode == "e_triangle" and len(e_triangle) == 3:
    pts = [(int(x), int(y)) for x, y in e_triangle]
    pygame.draw.polygon(screen, curr_color, pts, THICKNESS)
  elif LMBpressed and mode == "rhombus" and len(rhombus) == 4:
    pygame.draw.polygon(screen, curr_color, rhombus, THICKNESS)

  # HUD
  color_label = 'R' if curr_color == colorRED else 'G' if curr_color == colorGREEN else 'B'
  text = font.render(f"Mode: {mode} | Size: {THICKNESS} | Color: {color_label}", True, colorWHITE)
  screen.blit(text, (10, 10))

  pygame.display.flip()
  clock.tick(60)

pygame.quit()