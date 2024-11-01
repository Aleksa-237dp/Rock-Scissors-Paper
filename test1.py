import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Счетчик очков")

font = pygame.font.Font(None, 36)
score = 0

def draw_text(screen, text, x, y):
    text_surface = font.render(text, True, (255, 255, 255))
    screen.blit(text_surface, (x, y))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                score += 1

    screen.fill((0, 0, 0))
    draw_text(screen, f"Очки: {score}", 10, 10)
    pygame.display.flip()

pygame.quit()