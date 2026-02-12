import pygame

pygame.init()

pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mi Primer juego")


ejecutando = True

while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
    pantalla.fill((255, 255, 255))
    pygame.draw.rect(pantalla, (0, 255, 0), (100, 100, 200, 150))
    pygame.draw.circle(pantalla, (255, 0, 0), (400, 300), 50)

    pygame.display.update()
pygame.quit()