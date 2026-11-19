import pygame

pygame.init()

windowHeight = 500
windowLength = 800

screen = pygame.display.set_mode((windowLength, windowHeight))

running = True

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

currentColor = black

def drawSquare(thickness, x, y):
    square = pygame.Rect(x, y, thickness, thickness)
    pygame.draw.rect(screen, currentColor, square, 3)
    screen.fill(currentColor, rect=square)
    return square

screen.fill(white)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 or pygame.mouse.get_pressed()[0]:
            mx, my = pygame.mouse.get_pos()
            
            if mx < windowLength and my < windowHeight:
                drawSquare(30, mx, my)
                print(f"Creating square at {mx}, {my}!")
    
    pygame.display.flip()
    