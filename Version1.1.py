import pygame

pygame.init()

windowHeight = 500
windowLength = 800

screen = pygame.display.set_mode((windowLength, windowHeight))
clock = pygame.time.Clock()
# Need These
running = True
font = pygame.font.SysFont("Arial", 60)
thickness = 10
# Colors
red = (255, 0, 0)
orange = (255, 128, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
cyan = (0, 255, 255)
blue = (0, 0, 255)
purple = (180, 0, 200)
hotpink = (255, 32, 128)
pink = (255, 64, 200)
magenta = (255, 0, 255)
# Colors (row 2)
darkred = (100, 0, 0)
brown = (128, 64, 0)
darkyellow = (160, 160, 0)
darkgreen = (0, 128, 0)
darkcyan = (0, 128, 128)
darkblue = (0, 0, 128)
darkpurple = (90, 0, 100)
darkhotpink = (128, 16, 64)
darkpink = (128, 32, 100)
darkmagenta = (128, 0, 128)
# Colors (row 3)
white = (255, 255, 255)
gray = (128, 128, 128)
black = (0, 0, 0)
# Other Stuff
barGray = (200, 200, 200)
currentColor = black
def drawSquare(x, y):
    global thickness
    square = pygame.Rect(x, y, thickness, thickness)
    pygame.draw.rect(screen, currentColor, square, 3)
    screen.fill(currentColor, rect=square)
    return square

screen.fill(white)
squareSize = 25
# Row Y Positions
row1 = 15
row2 = (row1 + squareSize) + 20
row3 = (row2 + squareSize) + 20
while running:
    topBar = pygame.Rect(0, 0, windowLength, 150)
    pygame.draw.rect(screen, barGray, topBar, 3)
    screen.fill(barGray, rect=topBar)
    
    redBtn = pygame.Rect(50, row1, squareSize, squareSize)
    pygame.draw.rect(screen, red, redBtn, 3)
    screen.fill(red, rect=redBtn)
    
    orangeBtn = pygame.Rect(100, row1, squareSize, squareSize)
    pygame.draw.rect(screen, orange, orangeBtn, 3)
    screen.fill(orange, rect=orangeBtn)
    
    yellowBtn = pygame.Rect(150, row1, squareSize, squareSize)
    pygame.draw.rect(screen, yellow, yellowBtn, 3)
    screen.fill(yellow, rect=yellowBtn)
    
    greenBtn = pygame.Rect(200, row1, squareSize, squareSize)
    pygame.draw.rect(screen, green, greenBtn, 3)
    screen.fill(green, rect=greenBtn)
    
    cyanBtn = pygame.Rect(250, row1, squareSize, squareSize)
    pygame.draw.rect(screen, cyan, cyanBtn, 3)
    screen.fill(cyan, rect=cyanBtn)
    
    blueBtn = pygame.Rect(300, row1, squareSize, squareSize)
    pygame.draw.rect(screen, blue, blueBtn, 3)
    screen.fill(blue, rect=blueBtn)
    
    purpleBtn = pygame.Rect(350, row1, squareSize, squareSize)
    pygame.draw.rect(screen, purple, purpleBtn, 3)
    screen.fill(purple, rect=purpleBtn)
    
    magentaBtn = pygame.Rect(400, row1, squareSize, squareSize)
    pygame.draw.rect(screen, magenta, magentaBtn, 3)
    screen.fill(magenta, rect=magentaBtn)
    
    pinkBtn = pygame.Rect(450, row1, squareSize, squareSize)
    pygame.draw.rect(screen, pink, pinkBtn, 3)
    screen.fill(pink, rect=pinkBtn)
    
    hotPinkBtn = pygame.Rect(500, row1, squareSize, squareSize)
    pygame.draw.rect(screen, hotpink, hotPinkBtn, 3)
    screen.fill(hotpink, rect=hotPinkBtn)
    
    darkRedBtn = pygame.Rect(50, row2, squareSize, squareSize)
    pygame.draw.rect(screen, darkred, darkRedBtn, 3)
    screen.fill(darkred, rect=darkRedBtn)
    
    brownBtn = pygame.Rect(100, row2, squareSize, squareSize)
    pygame.draw.rect(screen, brown, brownBtn, 3)
    screen.fill(brown, rect=brownBtn)
    
    darkYellowBtn = pygame.Rect(150, row2, squareSize, squareSize)
    pygame.draw.rect(screen, darkyellow, darkYellowBtn, 3)
    screen.fill(darkyellow, rect=darkYellowBtn)
    
    darkGreenBtn = pygame.Rect(200, row2, squareSize, squareSize)
    pygame.draw.rect(screen, darkgreen, darkGreenBtn, 3)
    screen.fill(darkgreen, rect=darkGreenBtn)
    
    darkCyanBtn = pygame.Rect(250, row2, squareSize, squareSize)
    pygame.draw.rect(screen, darkcyan, darkCyanBtn, 3)
    screen.fill(darkcyan, rect=darkCyanBtn)
    
    darkBlueBtn = pygame.Rect(300, row2, squareSize, squareSize)
    pygame.draw.rect(screen, darkblue, darkBlueBtn, 3)
    screen.fill(darkblue, rect=darkBlueBtn)
    
    darkPurpleBtn = pygame.Rect(350, row2, squareSize, squareSize)
    pygame.draw.rect(screen, darkpurple, darkPurpleBtn, 3)
    screen.fill(darkpurple, rect=darkPurpleBtn)
    
    darkMagentaBtn = pygame.Rect(400, row2, squareSize, squareSize)
    pygame.draw.rect(screen, darkmagenta, darkMagentaBtn, 3)
    screen.fill(darkmagenta, rect=darkMagentaBtn)
    
    darkPinkBtn = pygame.Rect(450, row2, squareSize, squareSize)
    pygame.draw.rect(screen, darkpink, darkPinkBtn, 3)
    screen.fill(darkpink, rect=darkPinkBtn)
    
    darkHotPinkBtn = pygame.Rect(500, row2, squareSize, squareSize)
    pygame.draw.rect(screen, darkhotpink, darkHotPinkBtn, 3)
    screen.fill(darkhotpink, rect=darkHotPinkBtn)
    
    blackBtn = pygame.Rect(50, row3, squareSize, squareSize)
    pygame.draw.rect(screen, black, blackBtn, 3)
    screen.fill(black, rect=blackBtn)
    
    grayBtn = pygame.Rect(100, row3, squareSize, squareSize)
    pygame.draw.rect(screen, gray, grayBtn, 3)
    screen.fill(gray, rect=grayBtn)
    
    whiteBtn = pygame.Rect(150, row3, squareSize, squareSize)
    pygame.draw.rect(screen, white, whiteBtn, 3)
    screen.fill(white, rect=whiteBtn)
    
    
    
    increaseBtn = pygame.Rect(575, 90, 40, 40)
    pygame.draw.rect(screen, white, increaseBtn, 3)
    screen.fill(white, rect=increaseBtn)
    
    plus = font.render("+", True, black)
    plusSurface = plus.get_rect(center=(595, 110))
    screen.blit(plus, plusSurface)
    
    decreaseBtn = pygame.Rect(650, 90, 40, 40)
    pygame.draw.rect(screen, white, decreaseBtn, 3)
    screen.fill(white, rect=decreaseBtn)
    
    minus = font.render("-", True, black)
    minusSurface = minus.get_rect(center=(670, 110))
    screen.blit(minus, minusSurface)
    
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
                elif orangeBtn.collidepoint(mx, my):
                    currentColor = orange
                    print("Color is now orange!")
                elif yellowBtn.collidepoint(mx, my):
                    currentColor = yellow
                    print("Color is now yellow!")
                elif greenBtn.collidepoint(mx, my):
                    currentColor = green
                    print("Color is now green!")
                elif cyanBtn.collidepoint(mx, my):
                    currentColor = cyan
                    print("Color is now cyan!")
                elif blueBtn.collidepoint(mx, my):
                    currentColor = blue
                    print("Color is now blue!")
                elif purpleBtn.collidepoint(mx, my):
                    currentColor = purple
                    print("Color is now purple!")
                elif magentaBtn.collidepoint(mx, my):
                    currentColor = magenta
                    print("Color is now magenta!")
                elif pinkBtn.collidepoint(mx, my):
                    currentColor = pink
                    print("Color is now pink!")
                elif hotPinkBtn.collidepoint(mx, my):
                    currentColor = hotpink
                    print("Color is now hot pink!")
                elif darkRedBtn.collidepoint(mx, my):
                    currentColor = darkred
                    print("Color is now dark red!")
                elif brownBtn.collidepoint(mx, my):
                    currentColor = brown
                    print("Color is now brown!")
                elif darkYellowBtn.collidepoint(mx, my):
                    currentColor = darkyellow
                    print("Color is now dark yellow!")
                elif darkGreenBtn.collidepoint(mx, my):
                    currentColor = darkgreen
                    print("Color is now dark green!")
                elif darkCyanBtn.collidepoint(mx, my):
                    currentColor = darkcyan
                    print("Color is now dark cyan!")
                elif darkBlueBtn.collidepoint(mx, my):
                    currentColor = darkblue
                    print("Color is now dark blue!")
                elif darkPurpleBtn.collidepoint(mx, my):
                    currentColor = darkpurple
                    print("Color is now dark purple!")
                elif darkMagentaBtn.collidepoint(mx, my):
                    currentColor = darkmagenta
                    print("Current Color is now dark magenta!")
                elif darkPinkBtn.collidepoint(mx, my):
                    currentColor = darkpink
                    print("Color is now dark pink!")
                elif darkHotPinkBtn.collidepoint(mx, my):
                    currentColor = darkhotpink
                    print("Color is now dark hot pink!")
                elif blackBtn.collidepoint(mx, my):
                    currentColor = black
                    print("Color is now black!")
                elif grayBtn.collidepoint(mx, my):
                    currentColor = gray
                    print("Color is now gray!")
                elif whiteBtn.collidepoint(mx, my):
                    currentColor = white
                    print("Color is now white!")
                elif increaseBtn.collidepoint(mx, my):
                    thickness += 1
                    print(f"Thickness is now {thickness}!")
                elif decreaseBtn.collidepoint(mx, my):
                    if thickness > 1:
                        thickness -= 1
                        print(f"Thickness is now {thickness}!")
                    else:
                        print("Thickness too small. Cannot decrease.")
                elif topBar.collidepoint(mx, my):
                    pass
                else:
                    drawSquare(mx, my)
                    print(f"Creating square at {mx}, {my}!")
                    print(f"Creating square at {mx}, {my}!")
    clock.tick(1000)
    pygame.display.flip()
    