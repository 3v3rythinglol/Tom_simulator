import pygame

pygame.init()

tomL = pygame.image.load('dateien/tomL.png')
tomR = pygame.image.load('dateien/tomR.png')
flash = pygame.image.load('dateien/flash.png')
icon = pygame.image.load('dateien/icon.png')
f = False
fs = True
xf = False
xxf = False
x = 100
y = 100
fx = 0
f2x = 0
fy = 0
f2y = 0
fxx = 0
fyy = 0
j = 100
L = True
ld = False
lu = False
rd = False
ru = False
run = True

wn = pygame.display.set_mode((500, 500))
pygame.display.set_icon(icon)
pygame.display.set_caption('tom kann nicht flashen.exe')

while run:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
    
    wn.fill((255, 255, 255))

    #direktion for tom
    if L:
        wn.blit(tomL, (x, y))
    else:
        wn.blit(tomR, (x, y))

    #movement for tom
    if keys[pygame.K_d] and x < 450:
        x += 1
        L = False
    if keys[pygame.K_a] and x > 0:
        x -= 1
        L = True
    if keys[pygame.K_w] and y < 450:
        y -= 1
    if keys[pygame.K_s] and y > 0:
        y +=1

    # toms flash
    if keys[pygame.K_e] and f == False:
        f = True

    #flash physiks
    if f:
        wn.blit(flash, (fx, fy))

    if f and fs:
        fx = x + 30
        fy = y + 50

    if pygame.mouse.get_pressed() == (1, 0, 0) and fs and f:
        fs = False
        if L == True:
            ld = True
        if L == False:
            ru = True
    if pygame.mouse.get_pressed() == (0, 0, 1) and fs and f:
        fs = False
        if L == True:
            lu = True
        if L == False:
            rd = True

    if lu:
        f2x += 0.005
        fx -= 2
        fx += f2x
        f2y += 0.005
        fx -= f2y
        xf = True
    if ld:
        f2x += 0.02
        fx -= 2
        fx += f2x
        f2y += 0.02
        fy += f2y
        xf = True
    if ru:
        f2x += 0.02
        fx += 2
        fx -= f2x
        f2y += 0.02
        fy -= f2y
        xf = True
    if rd:
        f2x += 0.02
        fx += 2
        fx -= f2x
        f2y += 0.02
        fy += f2y
        xf = True

    if xf == True:
        j -= 1
        if j < 0:
            ld = False
            lu = False
            rd = False
            ru = False
            f = False
            fs = True
            xxf = True
            xf = False
            j = 100
            f2y = 0
            f2x = 0
    if xxf == True:
        for i in range(200):
            pygame.time.delay(10)
            wn.fill((255, 255, 0))
            pygame.display.update()
        xxf = False

    if f:
        wn.blit(flash, (fx, fy))

    pygame.display.update()