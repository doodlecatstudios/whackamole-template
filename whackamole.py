import pygame
import random


screen = pygame.display.set_mode((640, 512))


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        mole_row, mole_col = 0, 0
        screen.fill("light green")
        pygame.display.set_caption("Whack-a-mole")
        draw_grid()
        screen.blit(mole_image, mole_image.get_rect(topleft=(0, 0)))
        pygame.display.flip()
        clock.tick(60)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    row = y // 32
                    col = x // 32
                    print(row, col)
                    print(mole_row, mole_col)
                    if mole_col == row and mole_row == col:
                        mole_row = (random.randrange(0, 20, ))
                        mole_col = (random.randrange(0, 16, ))
                        screen.fill("light green")
                        draw_grid()
                        screen.blit(mole_image, mole_image.get_rect(topleft=(mole_row*32, mole_col*32)))
                        pygame.display.flip()

    finally:
        pygame.quit()



def draw_grid():
    #draw horizontal lines
    for i in range(1, 640):
        pygame.draw.line(
            screen,
            (100, 200, 200),
            (0, i*32), #start
            (640, i*32), #end
            2
        )
    #draw vertical lines
    for i in range(1, 512):
        pygame.draw.line(
            screen,
            (100, 200, 200),
            (i*32, 0), #start
            (i*32, 512), #end
            2
        )




if __name__ == "__main__":
    main()
