from View import View
from Garden import Garden
from HUD import HUD
from Menu import Menu
from End import End
import pygame

def update(graphic_elements):
    for g in graphic_elements:
        if isinstance(g, Garden):
            g.update()

    return graphic_elements

def eventListener(event, elements):
    mx, my = pygame.mouse.get_pos()
    if isinstance(elements[0], Garden):
        garden = elements[0]
        hud = elements[1]

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if event.button == 1:
                if mx >= 896:
                    hud.buy(mx, my)
                elif mx < 896:
                    garden.putTower()

        #Delete the tower that is holding
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            if garden.holding != None:
                # The method will detect that garden.holding is not None and will refund
                hud.refund()
            else:
                garden.removeTower()

        if event.type == pygame.USEREVENT:
            end = End()
            end.score = hud.get_level() + 1
            elements.remove(garden)
            elements.remove(hud)
            elements.append(end)

    elif isinstance(elements[0], End):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if mx >= 120 and mx <= 462 and my >= 642 and my <= 738:
                if len(elements[0].pseudo):
                    file = open("scoreboard", "a", encoding = "utf-8")
                    file.write((" " * (10 - len(elements[0].pseudo))) + elements[0].pseudo + " : " + str(elements[0].score) + "\n")
                    file.close()

                #Start game
                menu = Menu()
                elements = [menu]

            elif mx >= 536 and mx <= 878 and my >= 642 and my <= 738:
                if len(elements[0].pseudo):
                    file = open("scoreboard", "a", encoding = "utf-8")
                    file.write((" " * (10 - len(elements[0].pseudo))) + elements[0].pseudo + " : " + str(elements[0].score) + "\n")
                    file.close()
                View.crashed = True

        elif event.type == pygame.KEYDOWN:
            if event.key == 8:
                elements[0].pseudo = elements[0].pseudo[:-1]
            else:
                if len(elements[0].pseudo) < 10:
                    if event.key == 32 or (event.key > 96 and event.key < 123):
                        elements[0].pseudo += chr(event.key)
    else:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            menu = elements[0]
            if menu.page == "Menu":
                if mx >= 295 and mx <= 728 and my >= 350 and my <= 472:
                    #Start game
                    garden = Garden()
                    hud = HUD(garden, 10, 10)#10000) pour test des trucs
                    garden.HUD = hud

                    elements = [garden, hud]

                elif mx >= 341 and mx <= 683 and my >= 492 and my <= 588:
                    menu.page = "Rules"
                    
                elif mx >= 341 and mx <= 683 and my >= 608 and my <= 704:
                    menu.page = "Credits"

            elif menu.page == "Rules":
                if mx >= 295 and mx <= 728 and my >= 608 and my <= 730:
                    menu.page = "Menu"

            elif menu.page == "Credits":
                if mx >= 295 and mx <= 728 and my >= 608 and my <= 730:
                    menu.page = "Menu"

    return elements

#Main

menu = Menu()

view = View([menu], update, eventListener)
