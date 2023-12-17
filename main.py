import pygame

import Reketa
import Astero

pygame.init()

window = pygame.display.set_mode((500, 500))
fps = pygame.time.Clock()

fonks = pygame.image.load('galaxy.jpg')
fonks = pygame.transform.scale(fonks, (500, 500))


raketa = Reketa.Reketa(200, 440, 50, 50, 5, "rocket.png" )
aster = Astero.Astero((250, 350, 30, 20, 5, "asteroid.png")



asteroud = []
asteroud.append(Astero(50, 0, 50, 50, 10, "asteroid.png"))
asteroud.append(Astero(50, 0, 50, 50, 10, "asteroid.png"))

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



    for asteroud in 
    pygame.display.flip()
    fps.tick(60)
