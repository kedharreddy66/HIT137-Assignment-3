#github-link: https://github.com/kedharreddy66/HIT137-Assignment-3.git

import pygame

class Collectible(pygame.sprite.Sprite):
    def __init__(self, x, y, type='health'):
        super().__init__()
        self.type = type
        self.image = pygame.Surface((25, 25), pygame.SRCALPHA)  # Adjusted size
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.font = pygame.font.Font(None, 16)

        # Draw the collectible based on its type (only health now)
        self.draw_heart()

    def draw_heart(self):
        # Draw a simple heart shape for the health pack
        self.image.fill((0, 0, 0, 0))  # Transparent background
        red = (255, 0, 0)
        # Draw the heart using circles and a polygon
        pygame.draw.circle(self.image, red, (6, 10), 6)
        pygame.draw.circle(self.image, red, (18, 10), 6)
        points = [(0, 10), (12, 24), (24, 10)]
        pygame.draw.polygon(self.image, red, points)

    def display_title(self, surface):
        title = "Health"
        text = self.font.render(title, True, (255, 255, 255))
        surface.blit(text, (self.rect.x, self.rect.y - 15))

    def apply_effect(self, player):
        if self.type == 'health':
            player.health = min(player.health + 25, player.max_health)

    def update(self):
        pass
