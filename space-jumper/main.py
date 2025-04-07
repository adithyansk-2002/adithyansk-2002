import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
GRAVITY = 0.5
JUMP_STRENGTH = -12
PLATFORM_SPEED = 2

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Jumper")
clock = pygame.time.Clock()

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 10
        self.velocity_y = 0
        self.velocity_x = 0
        self.jumping = False

    def update(self):
        # Apply gravity
        self.velocity_y += GRAVITY
        self.rect.y += self.velocity_y

        # Move horizontally
        self.rect.x += self.velocity_x

        # Keep player on screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            self.velocity_y = 0
            self.jumping = False

# Platform class
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width):
        super().__init__()
        self.image = pygame.Surface((width, 20))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Star class
class Star(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Create sprite groups
all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()
stars = pygame.sprite.Group()

# Create player
player = Player()
all_sprites.add(player)

# Create initial platforms
platform_positions = [
    (100, 400, 200),
    (400, 300, 200),
    (200, 200, 200),
    (500, 100, 200)
]

for x, y, width in platform_positions:
    platform = Platform(x, y, width)
    platforms.add(platform)
    all_sprites.add(platform)

# Create stars
for _ in range(5):
    x = random.randint(0, WIDTH - 20)
    y = random.randint(0, HEIGHT - 20)
    star = Star(x, y)
    stars.add(star)
    all_sprites.add(star)

# Game variables
score = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    # Keep loop running at the right speed
    clock.tick(FPS)

    # Process input/events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not player.jumping:
                player.velocity_y = JUMP_STRENGTH
                player.jumping = True
            if event.key == pygame.K_ESCAPE:
                running = False

    # Get pressed keys
    keys = pygame.key.get_pressed()
    player.velocity_x = 0
    if keys[pygame.K_LEFT]:
        player.velocity_x = -5
    if keys[pygame.K_RIGHT]:
        player.velocity_x = 5

    # Update
    all_sprites.update()

    # Check for platform collisions
    if player.velocity_y > 0:  # Falling
        hits = pygame.sprite.spritecollide(player, platforms, False)
        if hits:
            player.rect.bottom = hits[0].rect.top
            player.velocity_y = 0
            player.jumping = False

    # Check for star collisions
    star_hits = pygame.sprite.spritecollide(player, stars, True)
    for _ in star_hits:
        score += 10
        # Create new star
        x = random.randint(0, WIDTH - 20)
        y = random.randint(0, HEIGHT - 20)
        star = Star(x, y)
        stars.add(star)
        all_sprites.add(star)

    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # Draw score
    score_text = font.render(f'Score: {score}', True, WHITE)
    screen.blit(score_text, (10, 10))

    # Flip the display
    pygame.display.flip()

pygame.quit()
sys.exit() 