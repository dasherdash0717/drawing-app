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
    redBtn = pygame.Rect(50, 50, 50, 50)
    pygame.draw.rect(screen, red, redBtn, 3)
    screen.fill(red, rect=redBtn)
    
    greenBtn = pygame.Rect(150, 50, 50, 50)
    pygame.draw.rect(screen, green, greenBtn, 3)
    screen.fill(green, rect=greenBtn)
    
    blueBtn = pygame.Rect(250, 50, 50, 50)
    pygame.draw.rect(screen, blue, blueBtn, 3)
    screen.fill(blue, rect=blueBtn)
    
    blackBtn = pygame.Rect(350, 50, 50, 50)
    pygame.draw.rect(screen, black, blackBtn, 3)
    screen.fill(black, rect=blackBtn)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 or pygame.mouse.get_pressed()[0]:
            mx, my = pygame.mouse.get_pos()
            
            if mx < windowLength and my < windowHeight:
                if redBtn.collidepoint(mx, my):
                    currentColor = red
                    print("Color is now red!")
                    
                if greenBtn.collidepoint(mx, my):
                    currentColor = green
                    print("Color is now green!")
                    
                if blueBtn.collidepoint(mx, my):
                    currentColor = blue
                    print("Color is now blue!")
                    
                if blackBtn.collidepoint(mx, my):
                    currentColor = black
                    print("Color is now black!")
                    
                else:
                    drawSquare(30, mx, my)
                    print(f"Creating square at {mx}, {my}!")
                    print(f"Creating square at {mx}, {my}!")
    
    pygame.display.flip()