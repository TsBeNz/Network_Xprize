#--------------------------------------------------------------------Ex1
from github import Button
import pygame as pg

pg.init()
run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
btn = Button(20,20,100,100,(255,0,0)) # สร้าง Object จากคลาส Button ขึ้นมา

font = pg.font.Font('freesansbold.ttf', 32) # fontand fontsize
text = font.render('Tang FRAB6', True,(0,0,0), (255, 255, 255)) # (text,is smooth?,letter color,background color)
textRect = text.get_rect() # text size
textRect.center = (win_x // 2, win_y // 2)

W=0
A=0
S=0
D=0

while(run):
    screen.fill((255, 255, 255))
    screen.blit(text, textRect)

    if btn.isMouseOn():
        btn.color = (100,100,100)
        if pg.mouse.get_pressed()[0] == 1 :
            btn.color = (120,20,220)
    else:
        btn.color = (255,0,0)
    btn.draw(screen)


    pg.display.update()
    # for event in pg.event.get():
    #     if event.type == pg.QUIT:
    #         pg.quit()
    #         run = False
#--------------------------------------------------------------------Ex1
    if W==1 :
        btn.y -= 1
    if A==1:
        btn.x -= 1
    if S==1:
        btn.y += 1
    if D==1:
        btn.x += 1

#--------------------------------------------------------------------Ex2
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

        if event.type == pg.KEYDOWN and event.key == pg.K_w:
            W = 1
        if event.type == pg.KEYUP and event.key == pg.K_w:
            W = 0

        if event.type == pg.KEYDOWN and event.key == pg.K_a:
            A = 1
        if event.type == pg.KEYUP and event.key == pg.K_a:
            A = 0

        if event.type == pg.KEYDOWN and event.key == pg.K_s:
            S = 1
        if event.type == pg.KEYUP and event.key == pg.K_s:
            S = 0

        if event.type == pg.KEYDOWN and event.key == pg.K_d:
            D = 1
        if event.type == pg.KEYUP and event.key == pg.K_d:
            D = 0
        # if event.type == pg.KEYDOWN and event.key == pg.K_d: #ปุ่มถูกกดลงและเป็นปุ่ม D
        #     print("Key D down")
        # if event.type == pg.KEYUP and event.key == pg.K_o: #ปุ่มถูกปล่อยและเป็นปุ่ม O
        #     print("Key O up")
        if event.type == pg.QUIT:
            pg.quit()
            run = False
