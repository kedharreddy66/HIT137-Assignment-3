import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        
        # Create the tank surface with increased height
        self.image = pygame.Surface((80, 60), pygame.SRCALPHA)  # Adjusted height
        self.original_image = self.image.copy()  # Save the original image for flashing
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        # Player attributes
        self.speed = 5
        self.jump_strength = 15
        self.gravity = 0.8
        self.velocity_y = 0
        self.health = 100  # Initial health set to 100
        self.max_health = 100  # Max health for scaling
        self.lives = 3
        self.on_ground = False
        self.shoot_cooldown = 0
        self.flash_duration = 0
        self.grace_period = 60  # 60 frames (1 second if running at 60 FPS)
        self.collision_cooldown = 0  # Cooldown for taking damage after a collision

        # Construct the tank after setting up the attributes
        self.construct_tank()

    def construct_tank(self):
        # Draw the main body of the tank (rectangle)
        body_color = (0, 100, 0)  # Dark green
        pygame.draw.rect(self.original_image, body_color, [10, 30, 60, 25])  # Adjusted (x, y, width, height)

        # Draw the turret (rectangle)
        turret_color = (50, 205, 50)  # Lighter green
        pygame.draw.rect(self.original_image, turret_color, [45, 20, 15, 10])  # Adjusted (x, y, width, height)

        # Draw the cannon (rectangle)
        cannon_color = (50, 205, 50)  # Same as turret
        pygame.draw.rect(self.original_image, cannon_color, [60, 15, 20, 5])  # Adjusted (x, y, width, height)

        # Draw wheels/treads (circles)
        wheel_color = (0, 0, 0)  # Black
        for i in range(3):
            pygame.draw.circle(self.original_image, wheel_color, (20 + i * 20, 55), 5)  # Adjusted wheel positions
        
        self.image = self.original_image.copy()

    def update(self, keys_pressed):
        if self.grace_period > 0:
            self.grace_period -= 1

        if self.collision_cooldown > 0:
            self.collision_cooldown -= 1

        if keys_pressed[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys_pressed[pygame.K_RIGHT]:
            self.rect.x += self.speed

        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1  # Reduce cooldown over time

        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y

        if self.rect.bottom >= 500:  # Ground level at y = 500
            self.rect.bottom = 500
            self.velocity_y = 0
            self.on_ground = True

        # Handle flashing effect if the player was hit
        if self.flash_duration > 0:
            self.image.fill((255, 0, 0, 128), special_flags=pygame.BLEND_RGBA_MULT)
            self.flash_duration -= 1
        else:
            self.image = self.original_image.copy()

    def draw(self, surface):
        # Draw the player onto the given surface
        surface.blit(self.image, self.rect)
        self.draw_health_bar(surface)

    def draw_health_bar(self, surface):
        # Health bar size and position
        bar_width = 60
        bar_height = 10
        health_ratio = self.health / self.max_health
        health_bar_width = int(bar_width * health_ratio)

        # Draw the health bar above the tank
        bar_x = self.rect.x + 10
        bar_y = self.rect.y - 15

        # Background of the health bar (gray)
        pygame.draw.rect(surface, (169, 169, 169), (bar_x, bar_y, bar_width, bar_height))
        # Foreground of the health bar (green to red based on health)
        pygame.draw.rect(surface, (255 * (1 - health_ratio), 255 * health_ratio, 0), (bar_x, bar_y, health_bar_width, bar_height))

    def take_damage(self, amount):
        # Only take damage if the collision cooldown is over
        if self.collision_cooldown == 0:
            if self.health > 0:
                self.health -= amount
                self.flash_duration = 15  # Set the duration for the flash effect when hit
                self.collision_cooldown = 30  # Set cooldown to 30 frames to prevent immediate further collisions
                print(f"Player health reduced to {self.health}")
            if self.health < 0:
                self.health = 0
