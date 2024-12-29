import pygame

from matrix import Matrix

# Initialize Pygame
pygame.init()

# Set up the screen dimensions
screen_width = 620
screen_height = 620

# Create the screen object
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the screen caption
pygame.display.set_caption("2048")

m = Matrix(screen, 14)

# Main loop
running = True
auto = False

while running:

    screen.fill((242, 253, 255))

    m.display()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
            elif event.key == pygame.K_LEFT:
                if not m.check_collisions("l"):
                    m.add_new_tile()
            elif event.key == pygame.K_RIGHT:
                if not m.check_collisions("r"):
                    m.add_new_tile()
            elif event.key == pygame.K_UP:
                if not m.check_collisions("u"):
                    m.add_new_tile()
            elif event.key == pygame.K_DOWN:
                if not m.check_collisions("d"):
                    m.add_new_tile()
            elif event.key == pygame.K_a and auto == False:
                auto = True
            elif event.key == pygame.K_a and auto == True:
                auto = False

    if auto:
        if not m.check_collisions("u"):
            m.add_new_tile()
        pygame.display.update()
        # pygame.time.delay(5)
        if not m.check_collisions("r"):
            m.add_new_tile()
        pygame.display.update()
        # pygame.time.delay(5)
            

    if m.check_loss():
        pygame.time.delay(10000)
        running = False

    pygame.display.update()

# Quit Pygame
pygame.quit()
