import pygame

pygame.init()

windowHeight = 500
windowLength = 800

screen = pygame.display.set_mode((windowLength, windowHeight))
clock = pygame.time.Clock()
running = True

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
orange = (255, 128, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
purple = (180, 0, 200)
barGray = (200, 200, 200)
currentColor = black
font = pygame.font.SysFont("Arial", 60)
sFont = pygame.font.SysFont("Arial", 30)
thickness = 10
thicknessAmp = 1
def drawSquare(x, y):
    global thickness
    square = pygame.Rect(x, y, thickness, thickness)
    pygame.draw.rect(screen, currentColor, square, 3)
    screen.fill(currentColor, rect=square)
    return square
def fill(x, y):
    filling = True
    drawing = False
    print("Fill Placeholder")
    
screen.fill(white)
squareSize = 25
drawing = True
filling = False
while running:
    topBar = pygame.Rect(0, 0, windowLength, 150)
    pygame.draw.rect(screen, barGray, topBar, 3)
    screen.fill(barGray, rect=topBar)
    
    redBtn = pygame.Rect(50, 62.5, squareSize, squareSize)
    pygame.draw.rect(screen, red, redBtn, 3)
    screen.fill(red, rect=redBtn)
    
    orangeBtn = pygame.Rect(100, 62.5, squareSize, squareSize)
    pygame.draw.rect(screen, orange, orangeBtn, 3)
    screen.fill(orange, rect=orangeBtn)
    
    yellowBtn = pygame.Rect(150, 62.5, squareSize, squareSize)
    pygame.draw.rect(screen, yellow, yellowBtn, 3)
    screen.fill(yellow, rect=yellowBtn)
    
    greenBtn = pygame.Rect(200, 62.5, squareSize, squareSize)
    pygame.draw.rect(screen, green, greenBtn, 3)
    screen.fill(green, rect=greenBtn)
    
    blueBtn = pygame.Rect(250, 62.5, squareSize, squareSize)
    pygame.draw.rect(screen, blue, blueBtn, 3)
    screen.fill(blue, rect=blueBtn)
    
    purpleBtn = pygame.Rect(300, 62.5, squareSize, squareSize)
    pygame.draw.rect(screen, purple, purpleBtn, 3)
    screen.fill(purple, rect=purpleBtn)
    
    blackBtn = pygame.Rect(350, 62.5, squareSize, squareSize)
    pygame.draw.rect(screen, black, blackBtn, 3)
    screen.fill(black, rect=blackBtn)
    
    eraserBtn = pygame.Rect(400, 62.5, squareSize, squareSize)
    pygame.draw.rect(screen, white, eraserBtn, 3)
    screen.fill(white, rect=eraserBtn)
    
    fillBtn = pygame.Rect(450, 62.5 - squareSize, squareSize, squareSize)
    pygame.draw.rect(screen, white, fillBtn, 3)
    screen.fill(white, rect=fillBtn)
    
    fillIcon = sFont.render("f", True, black)
    screen.blit(fillIcon, (457.5, 62.5 - squareSize))
    
    increaseBtn = pygame.Rect(575, 90, 40, 40)
    pygame.draw.rect(screen, white, increaseBtn, 3)
    screen.fill(white, rect=increaseBtn)
    
    plus = font.render("+", True, black)
    screen.blit(plus, (577, 77.5))
    
    decreaseBtn = pygame.Rect(650, 90, 40, 40)
    pygame.draw.rect(screen, white, decreaseBtn, 3)
    screen.fill(white, rect=decreaseBtn)
    
    minus = font.render("-", True, black)
    screen.blit(minus, (660, 77.5))
    
    size = font.render(str(thickness), True, black)
    sizeSurface = size.get_rect(center=(630, 55))
    screen.blit(size, sizeSurface)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 or pygame.mouse.get_pressed()[0]:
            mx, my = pygame.mouse.get_pos()
            
            if mx < windowLength and my < windowHeight:
                if redBtn.collidepoint(mx, my):
                    currentColor = red
                    print("Color is now red!")
                if orangeBtn.collidepoint(mx, my):
                    currentColor = orange
                    print("Color is now orange!")
                if yellowBtn.collidepoint(mx, my):
                    currentColor = yellow
                    print("Color is now yellow!")
                if greenBtn.collidepoint(mx, my):
                    currentColor = green
                    print("Color is now green!")
                    
                if blueBtn.collidepoint(mx, my):
                    currentColor = blue
                    print("Color is now blue!")
                    
                if purpleBtn.collidepoint(mx, my):
                    currentColor = purple
                    print("Color is now purple!")
                if blackBtn.collidepoint(mx, my):
                    currentColor = black
                    print("Color is now black!")
                    
                if eraserBtn.collidepoint(mx, my):
                    currentColor = white
                    print("Color is now white!")
                    
                if increaseBtn.collidepoint(mx, my):
                    thickness += thicknessAmp
                    print("Line Thickness is now " + str(thickness) + "!")
                if decreaseBtn.collidepoint(mx, my):
                    thickness -= thicknessAmp
                    print("Line Thickness is now " + str(thickness) + "!")
                if fillBtn.collidepoint(mx, my):
                    fill(mx, my)
                else:
                    if drawing:
                        drawSquare(mx, my)
                        print(f"Creating square at {mx}, {my}!")
                        print(f"Creating square at {mx}, {my}!")
    clock.tick(240)
    pygame.display.flip()