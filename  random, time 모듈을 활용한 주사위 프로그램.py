import pygame
import sys
import random
from time import sleep
from pygame.locals import *
import time

# Pygame 초기화
pygame.init()
clock = pygame.time.Clock()

# 화면 크기 설정
screen_width = 400
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Falling Images Example")
WHITE = (100, 100, 100)
BLACK = (0, 0, 0)

# 이미지 로드
bug = pygame.image.load("bug1.png")
bug1 = pygame.image.load("bug2.png")
fighter = pygame.image.load("player.png")
bar = pygame.image.load("bar.png")
c = pygame.image.load("c.png")
boss = pygame.image.load("boss.png")
ball = pygame.image.load("ball.png")
cat = pygame.image.load("cat.png")

# 이미지 크기 설정
bug_width = 45
bug_height = 37
bug = pygame.transform.scale(bug, (bug_width, bug_height))
bug1_width = 45
bug1_height = 37
bug1 = pygame.transform.scale(bug1, (bug1_width, bug1_height))
bug1_rect = bug1.get_rect()
fighter_width = 60
fighter_height = 55
fighter = pygame.transform.scale(fighter, (fighter_width, fighter_height))
bar_width = 10
bar_height = 20
bar = pygame.transform.scale(bar, (bar_width, bar_height))
bar_rect = bar.get_rect()
c_width = 5
c_height = 5
c = pygame.transform.scale(c, (c_width, c_height))
ball_width = 30
ball_height = 30
ball = pygame.transform.scale(ball, (ball_width, ball_height))
ball_rect = ball.get_rect()

# 이미지 객체 리스트 생성
images = []

# 이미지 떨어지는 속도 설정
bugSpeed = 2

# 총알 과부화
overload = False

bugCount = 0

lossBug = 0

laserOn = False

# 총알 그룹
bullets = pygame.sprite.Group()

bugWOW = True

turn = False

# bug 죽음
deth = False 
# False면 죽지않음, True면 죽음

Up = False

redBug = False

z = random.randint(1, 5)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 20))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = -10
    def update(self):
        global imgX, imgBottom, deth, bugCount, bugWOW, ball_rect, ballPos, Up

        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()
        if imgX < self.rect.x < imgX + bug_width and imgBottom > self.rect.y:
            bugCount += 1
            self.kill()
            deth = True
        if ball_rect.bottom > self.rect.top and ball_rect.left < self.rect.x < ball_rect.right:
            Up = True
            self.kill()

def writeMessage(text):
    global gamePad, running

    if text == "chughahaeii!!!":
        gamePad = pygame.display.set_mode((screen_width, screen_height))
        textfont = pygame.font.Font("KBO Dia Gothic_bold.ttf", 30)
        text = textfont.render(text, True, (255, 255, 255))
        textpos = text.get_rect()
        textpos.center = (screen_width / 2, screen_height - 70)
        gamePad.blit(text, textpos)
        screen.blit(cat, (-40, 0))
        running = False
    else:
        gamePad = pygame.display.set_mode((screen_width, screen_height))
        textfont = pygame.font.Font("KBO Dia Gothic_bold.ttf", 80)
        text = textfont.render(text, True, (255, 0, 0))
        textpos = text.get_rect()
        textpos.center = (screen_width / 2, screen_height / 2)
        gamePad.blit(text, textpos)

    pygame.display.update()
    sleep(2)

def writeScore(bugCount):
    global text, text1, bugSpeed

    font = pygame.font.Font("KBO Dia Gothic_bold.ttf", 15)
    text = font.render("제거한 벌ㄹㅔ:" + str(bugCount), True, (255, 255, 255))
    # bugSpeed = 5
    text1 = font.render("놓인 벌ㄹㅔ 3 / " + str(lossBug), True, (255, 255, 255))
    # bugSpeed = 5

def crash():
    global bugCount, lossBug, bar_width, a, b, bugSpeed, x, y

    writeMessage("전투기 파괴!")
    bugCount = 0
    lossBug = 0
    bar_width = 10
    bugSpeed = 2
    b = ball_rect.centerx = random.randint(0, screen_width - ball_width)
    a = ball_rect.centery = 60
    x = random.randint(0, screen_width - bug_width)
    y = -bug_height * 2

def loss():
    global bugCount, lossBug, bar_width, a, b, bugSpeed, x, y

    writeMessage("저런")
    bugCount = 0
    lossBug = 0
    bar_width = 10
    bugSpeed = 2
    b = ball_rect.centerx = random.randint(0, screen_width - ball_width)
    a = ball_rect.centery = 60

# 이미지 떨어질 위치 무작위 설정
def randomize_image_position():
    x = random.randint(0, screen_width - bug_width)
    y = -bug_height * 2
    return x, y

# 이미지 초기 위치 설정

# bug
x, y = randomize_image_position()
images.append(pygame.Rect(x, y, bug_width, bug_height))

# fighter
fighter_rect = fighter.get_rect()
fighter_rect.centerx = screen_width // 2
fighter_rect.bottom = screen_height - 40

# ball_rect.centerx = screen_width // 2
# ball_rect.centery = screen_height // 2
a = ball_rect.centery = 60
b = ball_rect.centerx = screen_width // 2
ball_speed_x = random.randint(1,4)
ball_speed_y = 4

def event():
    global bar_width, running

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if overload:
                # 스페이스 바를 누르면 총알 생성
                    bullet = Bullet(fighter_rect.centerx, fighter_rect.top)
                    bullets.add(bullet)
                    bar_width += 10

# 플레이어 이동 처리
def movePlayer():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        fighter_rect.x -= 7
    if keys[pygame.K_RIGHT]:
        fighter_rect.x += 7
    if fighter_rect.x <= 0:
        fighter_rect.x = 0
    if fighter_rect.x >= screen_width - fighter_width:
        fighter_rect.x = screen_width - fighter_width

# bullet 과부화
def overFlow():
    global bar_width, overload

    if bar_width >= 10:
        bar_width -= 0.3
        overload = True
    if bar_width >= fighter_width - 5:
        overload = False
    elif bar_width < fighter_width - 5:
        overload = True

def Ball():
    global ball_rect, ball_speed_y, ball_speed_x, Up, turn
    # 공 이동
    ball_rect.centerx += ball_speed_x
    ball_rect.centery += ball_speed_y

    if Up:
        ball_rect.y -= 100
        if screen_width // 2 < ball_rect.x:
            ball_rect.x -= 10
        else:
            ball_rect.x += 10
        Up = False

    if ball_rect.left < 0 or ball_rect.right > screen_width:
        ball_speed_x = -ball_speed_x
    if ball_rect.top < 0:
        ball_speed_y = -ball_speed_y
        ball_rect.y = 1
    if ball_rect.bottom > screen_height:
        ball_speed_y = -ball_speed_y

    # ball이랑 fighter랑 맞으면 꺼
    if ball_rect.bottom > fighter_rect.top and fighter_rect.left < ball_rect.x < fighter_rect.right:
        turn = True
        crash()

# 이미지 그리기
def draw():
    global imgX, imgBottom, deth, bugSpeed, bugCount, text, text1, lossBug, turn, z
    screen.fill(WHITE)
    # z = random.randint(1,2)
    # 이미지 그리기 및 이동)
    if bugWOW:
        for img in images:
            if redBug:
                if z == 1:
                    screen.blit(bug1, img)
                else:
                    screen.blit(bug, img)
            else:
                screen.blit(bug, img)
            img.move_ip(0, bugSpeed)

            # 이미지가 화면 아래로 벗어날 경우 다시 무작위 위치로 이동
            if img.top > screen_height:
                img.x, img.y = randomize_image_position()
                lossBug += 1
                if lossBug == 4:
                    loss()
                    lossBug = 0
                    bugSpeed = 2
                z = random.randint(1, 5)

            # bug가 플레이어에 닿으면 다시 무작위 위치로 이동
            if img.bottom > fighter_rect.top + 20 and fighter_rect.x - bug_width < img.x < fighter_rect.x + fighter_width:
                img.x, img.y = randomize_image_position()
                crash()
                bugSpeed = 2
                z = random.randint(1, 5)
            
            # bug가 총알에 닿으면 다시 무작위 위치로 이동
            if deth:
                img.x, img.y = randomize_image_position()
                bugSpeed += 0.2
                deth = False
                z = random.randint(1, 5)

            # 공이 플레이어에 닿으면 다시 무작위 위치로 이동
            if turn:
                img.x, img.y = randomize_image_position()
                turn = False
                z = random.randint(1, 5)

            imgX = img.x
            imgBottom = img.bottom
            bullets.update()
    if not(bugWOW):
        imgBottom = 0

    screen.blit(fighter, fighter_rect)
    screen.blit(bar, bar_rect)
    if bugCount >= 20:
        screen.blit(ball, ball_rect)
    screen.blit(text, (5, 10))
    screen.blit(text1, (280, 10))
    bullets.draw(screen)
    pygame.display.flip()

next_print_time = time.time() + 1
# 게임 루프
running = True
while running:
    clock.tick(60)

    current_time = time.time()

    if bugCount >= 20:
        Ball()
    if bugCount >= 10:
        redBug = True
    else:
        redBug = False
    if bugCount == 50:
        writeMessage( "chughahaeii!!!")

    writeScore(bugCount)

    event()

    overFlow()

    # 총알 업데이트
    bullets.update()

    movePlayer()
    # print(bugSpeed)
    bar = pygame.transform.scale(bar, (bar_width, bar_height))

    # bar 위치
    bar_rect.x = fighter_rect.x
    bar_rect.y = fighter_rect.bottom + 10

    if bugSpeed >= 10:
        bugSpeed = 10

    draw() 

    # 화면 업데이트
    pygame.display.update()

# Pygame 종료
pygame.quit()