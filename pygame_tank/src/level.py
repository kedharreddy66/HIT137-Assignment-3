import pygame
import random
from src.enemy import Enemy
from src.collectible import Collectible

class Level:
    def __init__(self, level_number):
        self.level_number = level_number
        self.enemies = pygame.sprite.Group()
        self.collectibles = pygame.sprite.Group()
        self.target_score = level_number * 5
        self.enemy_count = level_number * 3
        self.boss = None
        self.completed = False
        self.enemy_spawn_timer = 0
        self.collectible_spawn_timer = 0
        self.level_start_ticks = pygame.time.get_ticks()

    def spawn_enemy(self):
        x = 800
        y = random.randint(450, 490)
        enemy = Enemy(x, y)
        enemy.speed += self.level_number - 1
        self.enemies.add(enemy)

    def spawn_boss(self):
        x = 800
        y = 450
        boss_size = (50 + (self.level_number * 10), 50 + (self.level_number * 10))
        boss_health = 100 + (self.level_number * 50)
        boss = Enemy(x, y, is_boss=True, size=boss_size, health=boss_health)
        self.enemies.add(boss)
        self.boss = boss

    def spawn_collectible(self):
        x = random.randint(200, 600)
        y = random.randint(350, 450)
        collectible = Collectible(x, y, 'health')
        self.collectibles.add(collectible)

    def initialize(self):
        for _ in range(self.enemy_count):
            self.spawn_enemy()
        for _ in range(2):
            self.spawn_collectible()

    def update(self):
        self.enemies.update()
        self.collectibles.update()

        self.enemy_spawn_timer += 1
        if self.enemy_spawn_timer > max(120 - (self.level_number * 10), 60):
            self.spawn_enemy()
            self.enemy_spawn_timer = 0

        self.collectible_spawn_timer += 1
        if self.collectible_spawn_timer > 300:
            self.spawn_collectible()
            self.collectible_spawn_timer = 0

        elapsed_time = (pygame.time.get_ticks() - self.level_start_ticks) / 1000.0
        if elapsed_time >= 25 and not self.boss:
            self.spawn_boss()

    def draw(self, surface):
        self.enemies.draw(surface)
        self.collectibles.draw(surface)
        for collectible in self.collectibles:
            collectible.display_title(surface)
        for enemy in self.enemies:
            if enemy.is_boss:
                enemy.display_title(surface)

    def check_completion(self):
        if self.boss and self.boss.health <= 0:
            self.completed = True
