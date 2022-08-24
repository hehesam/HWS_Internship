import pygame

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)

WIDTH = 20
HEIGHT = 20

MARGIN = 5

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(10):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(10):
        grid[row].append(0)  # Append a cell

# Set row 1, cell 5 to one. (Remember rows and
# column numbers start at zero.)
grid[1][5] = 1

pygame.init()

size = (255, 255)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Array Backed Grid")

done = False

clock = pygame.time.Clock()

while not done :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)

            if grid[row][column] == 0 :
                grid[row][column] = 1
            else:
                grid[row][column] = 0


            print("Click", pos, "Grid coordinates : ", row, column)

    screen.fill(BLACK)

    for row in range(10):
        for column in range(10):
            color = WHITE
            if grid[row][column] == 1 :
                color = GREEN
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])

    clock.tick(60)

    pygame.display.flip()


pygame.quit()