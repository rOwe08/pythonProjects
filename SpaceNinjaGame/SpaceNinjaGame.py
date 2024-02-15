import time
import pygame
import random

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("Space Ninja")


def main():
    is_running = True
    print("Space Ninja Game")
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                break
    pygame.quit()


if __name__ == "__main__":
    main()
