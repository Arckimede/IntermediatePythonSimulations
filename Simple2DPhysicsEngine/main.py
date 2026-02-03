import pygame
from body import Body
from world import World
from constraints import DistanceConstraint

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

world = World(WIDTH, HEIGHT)

# Create bodies
b1 = Body((400, 200), 20, 1)
b2 = Body((450, 200), 20, 1)

world.add_body(b1)
world.add_body(b2)

# Add constraint (rod)
constraint = DistanceConstraint(b1, b2, 100)
world.add_constraint(constraint)

running = True

while running:
    dt = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    world.step(dt)

    screen.fill((30, 30, 30))

    # Draw constraint
    pygame.draw.line(
        screen,
        (255, 255, 255),
        b1.position.astype(int),
        b2.position.astype(int),
        2
    )

    # Draw bodies
    for body in world.bodies:
        pygame.draw.circle(
            screen,
            (200, 200, 255),
            body.position.astype(int),
            body.radius
        )

    pygame.display.flip()

pygame.quit()
