import pygame
import sys

# 게임 화면 크기 설정
screen_width = 800
screen_height = 600

# 색깔 설정
BLACK = (0, 0, 0)

# # 총알 클래스
# class Bullet(pygame.sprite.Sprite):
#     def __init__(self, x, y):
#         super().__init__()
#         self.image = pygame.Surface((10, 20))
#         self.image.fill(WHITE)
#         self.rect = self.image.get_rect()
#         self.rect.centerx = x
#         self.rect.bottom = y
#         self.speedy = -10

#     def update(self):
#         self.rect.y += self.speedy
#         if self.rect.bottom < 0:
#             self.kill()

# 게임 초기화
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

# 플레이어 설정
fighter = pygame.image.load("player.png")
fighter_rect = fighter.get_rect()
fighter_rect.centerx = screen_width // 2
fighter_rect.bottom = screen_height - 10

# 총알 그룹
# bullets = pygame.sprite.Group()

# 게임 루프
running = True
while running:
    clock.tick(24)

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_SPACE:
        #         # 스페이스 바를 누르면 총알 생성
        #         bullet = Bullet(fighter_rect.centerx, fighter_rect.top)
        #         bullets.add(bullet)

    # 플레이어 이동 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        fighter_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        fighter_rect.x += 5

    # 총알 업데이트
    # bullets.update()

    # 화면 그리기
    screen.fill(BLACK)
    screen.blit(fighter, fighter_rect)
    # bullets.draw(screen)
    pygame.display.flip()

# 게임 종료
pygame.quit()
sys.exit()
