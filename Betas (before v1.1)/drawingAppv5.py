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
blue = (0, 0, 255)
barGray = (200, 200, 200)
currentColor = black
font = pygame.font.SysFont("Arial", 60)

thickness = 10
def drawSquare(x, y):
    global thickness
    square = pygame.Rect(x, y, thickness, thickness)
    pygame.draw.rect(screen, currentColor, square, 3)
    screen.fill(currentColor, rect=square)
    return square

screen.fill(white)
while running:
    topBar = pygame.Rect(0, 0, windowLength, 150)
    pygame.draw.rect(screen, barGray, topBar, 3)
    screen.fill(barGray, rect=topBar)
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
    
    eraserBtn = pygame.Rect(450, 50, 50, 50)
    pygame.draw.rect(screen, white, eraserBtn, 3)
    screen.fill(white, rect=eraserBtn)
    
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
    screen.blit(size, (600, 25))
    
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
                    
                if eraserBtn.collidepoint(mx, my):
                    currentColor = white
                    print("Color is now white!")
                    
                if increaseBtn.collidepoint(mx, my):
                    thickness += 1
                if decreaseBtn.collidepoint(mx, my):
                    thickness -= 1
                else:
                    drawSquare(mx, my)
                    print(f"Creating square at {mx}, {my}!")
                    print(f"Creating square at {mx}, {my}!")
    clock.tick(240)
    pygame.display.flip()