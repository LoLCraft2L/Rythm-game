import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Change Hotkey")

# Set up the clock
clock = pygame.time.Clock()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define square properties
square_size = 50
square_color = BLACK
square_visible = {pygame.K_f: True, pygame.K_g: True, pygame.K_h: True, pygame.K_j: True, pygame.K_k: True}
square_positions = {
    pygame.K_f: (75, 125),
    pygame.K_g: (150, 125),
    pygame.K_h: (225, 125),
    pygame.K_j: (300, 125),
    pygame.K_k: (375, 125)
}

# Default hotkeys
hotkeys = [pygame.K_f, pygame.K_g, pygame.K_h, pygame.K_j, pygame.K_k]

# Function to draw the squares
def draw_squares():
    for hotkey in hotkeys:
        if square_visible[hotkey]:
            pygame.draw.rect(screen, square_color, (square_positions[hotkey][0], square_positions[hotkey][1], square_size, square_size))

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Change hotkey
            if event.key in square_visible:
                hotkey_index = hotkeys.index(event.key)
                hotkeys[hotkey_index] = event.key
                print(f"Hotkey {hotkey_index + 1} changed to {pygame.key.name(event.key)}")
            else:
                print("Press a key to change one of the hotkeys.")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Toggle square visibility
            if event.button == 1:
                for hotkey in hotkeys:
                    if square_positions[hotkey][0] < event.pos[0] < square_positions[hotkey][0] + square_size and \
                            square_positions[hotkey][1] < event.pos[1] < square_positions[hotkey][1] + square_size:
                        square_visible[hotkey] = not square_visible[hotkey]

    # Clear the screen
    screen.fill(WHITE)

    # Draw the squares
    draw_squares()

    # Display the changes
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()