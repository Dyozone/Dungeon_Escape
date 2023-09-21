import pygame.event
from camera import *
from player import *
from monster import *
from enum import Enum
from pygame.math import Vector2

monsters = []
player = Player((500, 1000))
coords = [[1000, 1000], [3200, 2000], [5000, 1500], [5000, 3000], [3200, 4300], [576, 3200]]
for i in range(len(coords)):
    monsters.append(Monster(coords[i], 'demon', 'big', ""))
camera = Camera(player, Display.HEIGHT, Display.HEIGHT)
class GameNow(Enum):
    Over = 0
    Playing = 1
    Starting = 2
    Pausing = 3
    Won = 4


class Game:
    STATE = GameNow.Starting
    RESET = False

    @staticmethod
    def reset():
        player.resume_spawn()
        player.reset_stats()
        for monster in monsters:
            monster.resume_spawn()

    @staticmethod
    def start_menu():
        screen.fill('black')
        screen.blit(pygame.transform.scale(Skins.LIBRARY['icon'], (Display.WIDTH, Display.HEIGHT)), (0, 0))
        start_button = Button(10, screen.get_rect().centery, 120, 50, 'white', 'black', 'Start', 32)
        pygame.draw.rect(screen, 'white', start_button.rect, 50)
        screen.blit(start_button.font.render(start_button.content, True, start_button.bg),
                    (start_button.x + 20, start_button.y))
        quit_button = Button(Display.WIDTH - 130, screen.get_rect().centery, 120, 50, 'white', 'black', 'Quit', 32)
        pygame.draw.rect(screen, 'white', quit_button.rect, 50)
        screen.blit(quit_button.font.render(quit_button.content, True, quit_button.bg),
                    (quit_button.x + 40, quit_button.y))
        if start_button.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            Game.RESET = True
            Game.STATE = GameNow.Playing
        elif quit_button.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            Display.exit()
        pygame.display.update()

    @staticmethod
    def pause_menu():
        screen.fill('black')
        screen.blit(pygame.transform.scale(Skins.LIBRARY['icon'], (Display.WIDTH, Display.HEIGHT)), (0, 0))
        continue_button = Button(10, screen.get_rect().centery, 120, 50, 'white', 'black', 'Continue', 32)
        quit_button = Button(Display.WIDTH - 130, screen.get_rect().centery, 120, 50, 'white', 'black', 'Quit', 32)
        pygame.draw.rect(screen, 'white', continue_button.rect, 50)
        screen.blit(continue_button.font.render(continue_button.content, True, continue_button.bg),
                    (continue_button.x, continue_button.y))
        pygame.draw.rect(screen, 'white', quit_button.rect, 50)
        screen.blit(quit_button.font.render(quit_button.content, True, quit_button.bg),
                    (quit_button.x + 40, quit_button.y))
        if continue_button.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            Game.STATE = GameNow.Playing
        elif quit_button.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            Game.QUIT = True
            Display.exit()
        pygame.display.update()

    @staticmethod
    def over_menu():
        screen.fill('black')
        screen.blit(pygame.transform.scale(Skins.LIBRARY['gameover'], (Display.WIDTH, Display.HEIGHT)), (0, 0))
        restart_button = Button(10, screen.get_rect().centery, 120, 50, 'white', 'black', 'Restart', 32)
        quit_button = Button(Display.WIDTH - 130, screen.get_rect().centery, 120, 50, 'white', 'black', 'Quit', 32)
        pygame.draw.rect(screen, 'white', restart_button.rect, 50)
        screen.blit(restart_button.font.render(restart_button.content, True, restart_button.bg),
                    (restart_button.x + 20, restart_button.y))
        pygame.draw.rect(screen, 'white', quit_button.rect, 50)
        screen.blit(quit_button.font.render(quit_button.content, True, quit_button.bg),
                    (quit_button.x + 40, quit_button.y))
        if restart_button.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            Game.RESET = True
            Game.STATE = GameNow.Playing
        elif quit_button.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            Display.exit()
        pygame.display.update()

    @staticmethod
    def victory_menu():
        screen.fill('black')
        screen.blit(pygame.transform.scale(Skins.LIBRARY['icon'], (Display.WIDTH, Display.HEIGHT)), (0, 0))
        restart_button = Button(10, screen.get_rect().centery, 120, 50, 'white', 'black', 'Restart', 32)
        quit_button = Button(Display.WIDTH - 130, screen.get_rect().centery, 120, 50, 'white', 'black', 'Quit', 32)
        text_box = Button(screen.get_rect().centerx - 130, screen.get_rect().centery - screen.get_height()/2, 200, 50, 'white', 'black', 'DUNGEON ESCAPED!', 32)
        pygame.draw.rect(screen, 'white', restart_button.rect, 50)
        screen.blit(restart_button.font.render(restart_button.content, True, restart_button.bg),
                    (restart_button.x + 20, restart_button.y))
        pygame.draw.rect(screen, 'white', quit_button.rect, 50)
        screen.blit(quit_button.font.render(quit_button.content, True, quit_button.bg),
                    (quit_button.x + 40, quit_button.y))
        pygame.draw.rect(screen, 'white', text_box.rect, 50)
        screen.blit(quit_button.font.render(text_box.content, True, text_box.bg),
                    (text_box.x + 40, text_box.y))
        if restart_button.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            Game.RESET = True
            Game.STATE = GameNow.Playing
        elif quit_button.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            Display.exit()
        pygame.display.update()