#github-link: https://github.com/kedharreddy66/HIT137-Assignment-3.git

import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.image = pygame.Surface((10, 5))  # Small rectangle for the projectile
        self.image.fill((255, 0, 0))  # Red color for visibility
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        
        # Projectile attributes
        self.speed = 10
        self.direction = direction  # Direction is 1 for right, -1 for left

    def update(self):
        # Move the projectile
        self.rect.x += self.speed * self.direction

        # Remove the projectile if it goes off-screen (assuming screen width is 800)
        if self.rect.right < 0 or self.rect.left > 800:
            self.kill()
