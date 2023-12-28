import pygame

import Patron
import Reketa
import Astero

pygame.init()

window = pygame.display.set_mode((500, 500))
fps = pygame.time.Clock()

fonks = pygame.image.load('galaxy.jpg')
fonks = pygame.transform.scale(fonks, (500, 500))


raketa = Reketa.Reketa(200, 440, 50, 50, 5, "rocket.png" )




asteroud = []

asteroud.append(Astero.Astero(10, -50, 50, 50, 5, "asteroid.png"))
asteroud.append(Astero.Astero(60, -50, 50, 50, 5, "asteroid.png"))
asteroud.append(Astero.Astero(134, -50, 50, 50, 5, "asteroid.png"))

game = True
while game:


    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            print(x, y)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()

    raketa.move()



    window.blit(fonks, (0, 0))
    raketa.render(window)

    for Astero in asteroud:
        Astero.render(window)


    pygame.display.flip()
    fps.tick(60)
