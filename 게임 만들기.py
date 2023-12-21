import pygame
import sys

# 초기화
pygame.init()

# 게임 창 설정
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("공 튕기기")

# 공 이미지 로드
ball_image = pygame.image.load("ball.png")
ball_rect = ball_image.get_rect()

# 공 초기 위치와 속도 설정
ball_rect.centerx = width // 2
ball_rect.centery = height // 2
ball_speed_x = 5
ball_speed_y = 5

# 게임 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 공 이동
    ball_rect.centerx += ball_speed_x
    ball_rect.centery += ball_speed_y
    
    # 벽과의 충돌 검사
    if ball_rect.left < 0 or ball_rect.right > width:
        ball_speed_x = -ball_speed_x
    if ball_rect.top < 0 or ball_rect.bottom > height:
        ball_speed_y = -ball_speed_y

    # 화면 초기화
    screen.fill((255, 255, 255))
    
    # 공 이미지 그리기
    screen.blit(ball_image, ball_rect)
    
    # 화면 업데이트
    pygame.display.flip()
