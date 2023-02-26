import pygame as p
import schedule as sched
from Global import *

class display_schedule():
    def __init__(self) -> None:
        self.x = screenWidth
        self.y = screenHeight
        self.font = p.font.Font('Roboto-Regular.ttf', 24)
        # currentScreen shows the display
        # 0 for today
        # 1 for week
        # 3 for month (will be implemented later)
        # 4 for school
        # 5 for hobbies
        # 6 for work
        self.currentScreen = 0
        self.times = ["Today", "Week", "Month"]
        self.categories = ["School", "Hobbies", "Work"]

    def changeCurrentScreen(self, pos):
        if pos[0] >= 50 * self.x/screenWidth and pos[0] <= 250 * self.x/screenWidth:
            if pos[1] >= 250 * self.y/screenHeight and pos[1] <= 300 * self.y/screenHeight:
                self.currentScreen = 0
            if pos[1] >= 350 * self.y/screenHeight and pos[1] <= 400 * self.y/screenHeight:
                self.currentScreen = 1
            if pos[1] >= 450 * self.y/screenHeight and pos[1] <= 500 * self.y/screenHeight:
                self.currentScreen = 2

    def draw(self, screen):
        self.x, self.y = screen.get_size()
        self.drawBackground(screen)
        for i in range(0,3):
            if i == self.currentScreen:
                color = "#83adf7"
            else:
                color = "#FFFFFF"
            self.drawButton(screen, self.times[i], 50 * (self.x/screenWidth), 250 + (i*100) * (self.y/screenHeight), color)
        self.drawCurrentScreen(screen)
    
    def drawButton(self, screen, text, x, y, color):
        rect = p.Rect(x, y, 200 * self.x/screenWidth, 50 * self.y/screenHeight)
        p.draw.rect(screen, p.Color(color), rect)
        text = self.font.render(text, True, p.Color("#000000"))
        textRect = text.get_rect()
        textRect.center = (rect.x + rect.width//2, rect.y + rect.height//2)
        screen.blit(text, textRect)
        

    def drawBackground(self, screen):
        screen.fill(p.Color("#424242"))
        rect = p.Rect(0,0, 300 * (self.x/screenWidth), self.y)
        p.draw.rect(screen, p.Color("#212121"), rect)
        rect = p.Rect(0,0, self.x , 150 * (self.y/screenHeight))
        p.draw.rect(screen, p.Color("#121212"), rect)

    def drawCurrentScreen(self, screen):
        font = p.font.Font('Roboto-Regular.ttf', 48)
        rect = p.Rect(350 * (self.x/screenWidth), 200 * (self.y/screenHeight), 300 * (self.x/screenWidth), 55* (self.y/screenHeight))
        text = font.render("" + self.times[self.currentScreen] + "'s Tasks", True, p.Color("#FFFFFF") )
        textRect = text.get_rect()
        textRect.center = (rect.x + rect.width//2, rect.y + rect.height//2)
        screen.blit(text, textRect)