import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, is_boss=False, size=(30, 30), health=25):
        super().__init__()
        self.is_boss = is_boss
        self.health = health
        self.font = pygame.font.Font(None, 20)

        if self.is_boss:
            self.image = pygame.Surface(size, pygame.SRCALPHA)  # Make boss larger with transparency
            self.draw_boss_shape(size)
        else:
            self.image = pygame.Surface(size, pygame.SRCALPHA)  # Regular enemies
            self.draw_enemy_shape(size)

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 2 if self.is_boss else random.randint(2, 3)
        self.bobbing_direction = 1
        self.bobbing_range = random.randint(5, 15)
        self.original_y = y

    def draw_enemy_shape(self, size):
        # Draw a tank shape for regular enemies
        self.image.fill((0, 0, 0, 0))  # Transparent background
        body_color = (0, 0, 255)  # Blue for the tank body
        cannon_color = (255, 255, 0)  # Yellow for the cannon

        # Draw the tank body
        pygame.draw.rect(self.image, body_color, [5, size[1]//2 - 5, size[0] - 10, 10])
        pygame.draw.circle(self.image, body_color, (10, size[1] - 5), 5)  # Left wheel
        pygame.draw.circle(self.image, body_color, (size[0] - 10, size[1] - 5), 5)  # Right wheel

        # Draw the cannon
        pygame.draw.rect(self.image, cannon_color, [size[0]//2, 5, 10, 5])

    def draw_boss_shape(self, size):
        # Draw a boss shape, such as a large tank
        self.image.fill((0, 0, 0, 0))  # Transparent background
        body_color = (255, 0, 0)  # Red for the boss body
        cannon_color = (0, 255, 0)  # Green for the boss cannon

        # Draw the boss body
        pygame.draw.rect(self.image, body_color, [5, size[1]//2 - 10, size[0] - 10, 20])
        pygame.draw.circle(self.image, body_color, (15, size[1] - 10), 8)  # Left wheel
        pygame.draw.circle(self.image, body_color, (size[0] - 15, size[1] - 10), 8)  # Right wheel

        # Draw the cannon
        pygame.draw.rect(self.image, cannon_color, [size[0]//2 - 5, 5, 15, 7])

    def display_title(self, surface):
        if self.is_boss:
            text = self.font.render("Boss", True, (255, 255, 255))
            surface.blit(text, (self.rect.x, self.rect.y - 20))

    def update(self):
        # Move left
        self.rect.x -= self.speed

        # Add vertical bobbing movement
        self.rect.y += self.bobbing_direction
        if abs(self.rect.y - self.original_y) >= self.bobbing_range:
            self.bobbing_direction *= -1

        if self.rect.right < 0:
            self.kill()

    def take_damage(self):
        self.health -= 25
        if self.health <= 0:
            self.kill()
