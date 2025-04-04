import pygame
import sys
import time

from settings import width, height, display, clock, background, white
from player import Player
from bullet import Bullet
from enemy import Enemy

def game():
    game_over = False

    player_x = width * 0.45
    player_y = height * 0.8
    x_move = 0
    score = 0
    level = 1
    current_speed = 1
    danger_zone = 0
    spawn_condition = 1

    enemys = []
    bullets = []
    num_bullet = 0
    num_enemy = 10
    max_enemy = 10
    min_enemy = 4
    d = int((620 - 10 * max_enemy) / (max_enemy - 1))

    for i in range(max_enemy):
        enemy = Enemy((i + 1) * d + i * 10, d - 20, d, current_speed)
        enemys.append(enemy)

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_RIGHT:
                    x_move = 10
                if event.key == pygame.K_LEFT:
                    x_move = -10
                if event.key == pygame.K_SPACE:
                    num_bullet += 1
                    bullets.append(Bullet(player_x + 45, player_y - 10))
            if event.type == pygame.KEYUP:
                x_move = 0

        if num_enemy == 0:
            level += 1

        player_x += x_move
        display.fill(background)

        for bullet in bullets:
            bullet.draw()
            bullet.move()

        spawn_condition = all(enemy.y != (d - 20) for enemy in enemys)
        if num_enemy <= min_enemy and spawn_condition:
            for i in range(4):
                enemy = Enemy((i + 1) * d + i * 10, d - 20, d, current_speed)
                enemys.append(enemy)
                num_enemy += 1

        danger_zone = any(enemy.y >= height / 2 for enemy in enemys)
        init_score = score

        for enemy in list(enemys):
            enemy.draw()
            enemy.move()
            for bullet in list(bullets):
                if bullet.hit(enemy.x, enemy.y, enemy.d):
                    bullets.remove(bullet)
                    num_bullet -= 1
                    enemys.remove(enemy)
                    num_enemy -= 1
                    score += 1

                    if score != 0 and score % 10 == 0 and not danger_zone and score != init_score:
                        current_speed += 1
                        for e in enemys:
                            e.update_speed(current_speed)
                    break

        for enemy in enemys:
            if enemy.x + d >= width:
                enemy.x_dir = -1
                enemy.shift_down()
            if enemy.x <= 0:
                enemy.x_dir = 1
                enemy.shift_down()

        if enemys and enemys[0].y + 2 * d > height:
            pygame.display.update()
            game_over = True
            time.sleep(5)

        if player_x < 0 or player_x + 100 > width:
            player_x -= x_move

        Player(player_x, player_y)

        font = pygame.font.SysFont("Sylfaen", 15)
        display.blit(font.render(f"SCORE: {score}", True, white), (720, 30))
        display.blit(font.render(f"LEVEL: {level}", True, white), (720, 50))
        display.blit(font.render(f"SPEED: {current_speed}", True, white), (720, 70))

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    game()