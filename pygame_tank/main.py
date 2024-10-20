#github-link: https://github.com/kedharreddy66/HIT137-Assignment-3.git

import pygame
import sys
import random
from src.player import Player
from src.projectile import Projectile
from src.level import Level

# Initialize Pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tank Battle")

clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
heading_font = pygame.font.Font(None, 48)

def start_menu():
    while True:
        window.fill((0, 0, 0))
        
        # Game Title (SYD 212)
        syd_title = heading_font.render("SYD 212", True, (255, 0, 0))  # Red color for emphasis
        syd_title_rect = syd_title.get_rect(center=(WIDTH // 2, 50))  # Positioned at the top center
        window.blit(syd_title, syd_title_rect)
        
        # Game Subtitle
        game_title = heading_font.render("Tank Battle", True, (0, 255, 0))
        title_rect = game_title.get_rect(center=(WIDTH // 2, 100))
        window.blit(game_title, title_rect)
        
        # Instructions
        instructions = [
            "Instructions:",
            "1. Use the arrow keys to move left and right.",
            "2. Press SPACE to jump.",
            "3. Press CTRL to shoot.",
            "4. Avoid enemy attacks and collect power-ups.",
            "5. Defeat the boss to advance levels!"
        ]
        for i, line in enumerate(instructions):
            instruction_text = font.render(line, True, (255, 255, 255))
            window.blit(instruction_text, (50, 200 + i * 30))
        
        # Play Button
        play_button_text = heading_font.render("Press ENTER to Play", True, (0, 255, 0))
        play_button_rect = play_button_text.get_rect(center=(WIDTH // 2, 500))
        window.blit(play_button_text, play_button_rect)
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return


def game_over_screen():
    while True:
        window.fill((0, 0, 0))
        text = font.render("Game Over! Press R to Restart or Q to Quit", True, (255, 255, 255))
        window.blit(text, (WIDTH // 2 - 200, HEIGHT // 2 - 20))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

def main():
    score = 0
    current_level = 1

    player = Player(100, 450)

    projectiles = pygame.sprite.Group()

    level = Level(current_level)
    level.initialize()

    running = True
    while running:
        keys_pressed = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and player.shoot_cooldown == 0:
                    projectile = Projectile(player.rect.right, player.rect.centery, 1)
                    projectiles.add(projectile)
                    player.shoot_cooldown = 10
                if event.key == pygame.K_SPACE and player.on_ground:
                    player.velocity_y = -player.jump_strength
                    player.on_ground = False

        player.update(keys_pressed)

        projectiles.update()

        level.update()

        for projectile in projectiles:
            hit_enemies = pygame.sprite.spritecollide(projectile, level.enemies, False)
            for enemy in hit_enemies:
                enemy.take_damage()
                if enemy.is_boss and enemy.health <= 0:
                    score += 10
                else:
                    score += 1
                projectile.kill()

        if player.grace_period == 0 and pygame.sprite.spritecollideany(player, level.enemies):
            player.take_damage(25)
            if player.health <= 0:
                if game_over_screen():
                    player = Player(100, 450)
                    score = 0
                    current_level = 1
                    level = Level(current_level)
                    level.initialize()
                else:
                    running = False

        collected_items = pygame.sprite.spritecollide(player, level.collectibles, True)
        for item in collected_items:
            item.apply_effect(player)

        level.check_completion()
        if level.completed:
            current_level += 1
            if current_level > 3:
                print("You've completed all levels! Congratulations!")
                running = False
            else:
                print(f"Level {current_level} completed! Loading next level...")
                level = Level(current_level)
                level.initialize()

        window.fill((135, 206, 235))

        game_heading = heading_font.render("Tank Battle", True, (255, 0, 0))
        heading_rect = game_heading.get_rect(center=(WIDTH // 2, 30))
        window.blit(game_heading, heading_rect)

        player.draw(window)
        projectiles.draw(window)
        level.draw(window)

        heading_text = heading_font.render("Player Health", True, (0, 0, 0))
        window.blit(heading_text, (10, 50))
        health_text = font.render(f"{player.health}", True, (255, 0, 0))
        window.blit(health_text, (10, 100))

        # Display score and current level at the rightmost side of the screen
        score_text = font.render(f"Score: {score} | Level: {current_level}", True, (0, 0, 0))
        score_rect = score_text.get_rect(topright=(WIDTH - 20, 50))
        window.blit(score_text, score_rect)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

# Run the start menu
start_menu()

# Start the main game loop
main()
