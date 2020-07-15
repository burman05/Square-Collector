import pygame

# Keyboard Constants
from pygame.locals import *
# Import Coin
from getcoin import Coin



# Create Screen
pygame.display.init()

# Set Dimensions of the display
# Get "Surface Object" to Draw on
screen = pygame.display.set_mode((800, 600))

# Pygame works based on these Surface Objects
# Rendered sprites are placed on Surface in rectangular areas

# Create Rectangle For Player
player = pygame.Rect(400, 300, 30, 30)

# define speed variables for Player
speed_x = 0
speed_y = 0
# define Colors
WHITE = pygame.Color(255, 255, 255)
BLACK = pygame.Color(0, 0, 0)
BLUE = pygame.Color(0,255,255)
RED = pygame.Color(255, 0, 0)

# Clock for FPS
clock = pygame.time.Clock()

# Add Movement Functions
def move_up():
  global speed_y
  speed_y = 10

def move_right():
  global speed_x
  speed_x = 10

def move_down():
  global speed_y
  speed_y = -10

def move_left():
  global speed_x
  speed_x = -10

# Funciton called every loop to move player
def movement_loop():
  global speed_x, speed_y, player
  player.centerx += speed_x

  # Remember that Y is reversed!
  player.centery -= speed_y

  speed_x = 0
  speed_y = 0

## Add Coins
# add a Score
score = 0

# add a list to keep track of the coins
list_of_coins = []

# Spawn 100 coins
for i in range(100):
  list_of_coins.append(Coin())

# Check Collision For Each Coin
def collision_loop():
  global list_of_coins
  global player
  global score

  # For each coin in game
  for coin in list_of_coins:
    # If collided rectangles and is not already hidden
    if player.colliderect(coin.rect) and         coin.isHidden == False:
      # Hide and add 1 to score
      coin.isHidden = True
      score += 1

def render_coin_loop(screen):
  global list_of_coins
  global YELLOW
  
  for coin in list_of_coins:
    if coin.isHidden == False:
      screen.fill(BLACK, coin.rect)

## SHOW TEXT ON SCREEN
pygame.font.init()
FONT = pygame.font.SysFont("freeserif", 36)

# Loop Forever! In Main
def main():

  global FONT, score
  while True:
    
    # detect events
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        exit(0)
    
    # Another Way to Get Keyboard Input
    # Pump Events (Prepare "key" structure)
    pygame.event.pump()
    key = pygame.key.get_pressed()

    # Defined by pygame.locals
    if key[K_UP]:
      move_up()
    if key[K_RIGHT]:
      move_right()
    if key[K_DOWN]:
      move_down()
    if key[K_LEFT]:
      move_left()

    # call movement function
    movement_loop()

    # call collision function
    collision_loop()

    # Tick Clock (60 FPS)
    clock.tick(60)

    # Fill screen with blue
    screen.fill(BLUE)
    screen.fill(RED, player)

        # render coins
    render_coin_loop(screen)

    # Render Score
    screen.blit(
      FONT.render("Score: " + str(score), True, BLACK),
      (20, 80)
    )

    # Get Time
    seconds = int(pygame.time.get_ticks() / 1000)
    screen.blit(
      FONT.render("Time: " + str(seconds), True, BLACK),
      (640, 80)
    )
    pygame.display.flip()

main()