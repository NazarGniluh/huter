import json

import pygame

import Patron
import Reketa
import Astero

pygame.init()
def start_game():
    def read_data():
        global settings
        with open("settings.json", "r", encoding="utf-8") as file:
            settings = json.load(file)
    read_data()
    window = pygame.display.set_mode((500, 500))
    fps = pygame.time.Clock()

    fonks = pygame.image.load('kosmoc.png')
    fonks = pygame.transform.scale(fonks, (500, 500))


    raketa = Reketa.Reketa(200, 440, 50, 50, 5, settings["skin"])




    asteroud = []

    asteroud.append(Astero.Astero(10, -50, 80, 80, 5, "1626166154_5-kartinkin-com-p-meteorit-piksel-art-art-krasivo-6-PhotoRoom.png-PhotoRoom.png"))
    asteroud.append(Astero.Astero(60, -50, 80, 80, 5, "1626166154_5-kartinkin-com-p-meteorit-piksel-art-art-krasivo-6-PhotoRoom.png-PhotoRoom.png"))
    asteroud.append(Astero.Astero(134, -50, 80, 80, 5, "1626166154_5-kartinkin-com-p-meteorit-piksel-art-art-krasivo-6-PhotoRoom.png-PhotoRoom.png"))
    asteroud.append(Astero.Astero(238, -50, 80, 80, 5, "1626166154_5-kartinkin-com-p-meteorit-piksel-art-art-krasivo-6-PhotoRoom.png-PhotoRoom.png"))






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
                return

        raketa.move()

        for a in asteroud:
            a.down(window)



        window.blit(fonks, (0, 0))
        raketa.render(window)


        for a in asteroud:
            a.render(window)


        pygame.display.flip()
        fps.tick(60)
