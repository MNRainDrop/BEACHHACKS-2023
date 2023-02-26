import pygame as p
from display_schedule import display_schedule as ds
from Global import *

# Main Game Driver
def main():
    #initialize pygame
    p.init()
    screen = p.display.set_mode((screenWidth, screenHeight), p.RESIZABLE)
    sched = ds()

    clock = p.time.Clock()
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.VIDEORESIZE:
                width, height = e.size
                if width < 600:
                    width = 600
                if height < 400:
                    height = 400
                screen = p.display.set_mode((width, height), p.RESIZABLE)
            elif e.type == p.MOUSEBUTTONDOWN:
                pos = p.mouse.get_pos()
                sched.changeCurrentScreen(pos)
        sched.draw(screen)

        clock.tick(maxFPS)
        p.display.flip()



if __name__ == "__main__":
    main()