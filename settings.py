import os
import pygame
import sys
import pygame.display


class Skins:
    LIBRARY = {}

    @staticmethod
    def load():
        sprite_paths = []
        ui_paths = []
        item_paths = []
        assets = []
        keys = []
        for root, dirs, files in os.walk("imgs"):
            for name in files:
                if root == 'imgs\\tile' or name == 'desktop.ini':
                    continue
                elif root == 'imgs\\ui':
                    ui_paths.append(os.path.join(root, name))
                elif root == 'imgs\\item':
                    item_paths.append(os.path.join(root, name))
                else:
                    sprite_paths.append(os.path.join(root, name))

        for image in sprite_paths:
            assets.append(pygame.transform.scale_by(pygame.image.load(image), 4).convert_alpha())

        for image in ui_paths:
            assets.append(pygame.transform.scale_by(pygame.image.load(image), 2).convert_alpha())

        for image in item_paths:
            assets.append(pygame.transform.scale_by(pygame.image.load(image), 0.5).convert_alpha())

        paths = sprite_paths + ui_paths + item_paths

        for path in paths:
            keys.append((path[5:len(path) - 4].replace('\\', '_')).replace(' ', '_'))

        for file in range(len(paths)):
            Skins.LIBRARY[keys[file]] = assets[file]



class Display:
    TITLE = "Dungeon Escape"
    CONTROL_FPS: 60
    SCALE = 5
    WIDTH = 640
    HEIGHT = 480

    @staticmethod
    def setup():
        pygame.init()
        pygame.display.set_icon(Skins.LIBRARY['icon'])
        pygame.display.set_caption(Display.TITLE)
        pygame.event.set_allowed([pygame.QUIT])

    @staticmethod
    def exit(action=pygame.QUIT):
        if action == pygame.QUIT:
            pygame.quit()
            sys.exit()




clock = pygame.time.Clock()

screen = pygame.display.set_mode([Display.WIDTH, Display.HEIGHT])
Skins.load()
Display.setup()

class Tiles:
    LIBRARY = {}
    KEYS = []
    SIZE = 64

    @staticmethod
    def load():
        paths = []
        assets = []
        for root, dirs, files in os.walk("imgs\\tile"):
            for name in files:
                if name == 'desktop.ini':
                    continue
                paths.append(os.path.join(root, name))

        for image in paths:
            assets.append(pygame.transform.scale_by(pygame.image.load(image), 4).convert_alpha())

        for path in paths:
            Tiles.KEYS.append((path[10:len(path) - 4].replace('\\', '_')).replace(' ', '_'))

        for file in range(len(paths)):
            Tiles.LIBRARY[Tiles.KEYS[file]] = assets[file]


class Button:
    def __init__(self, x, y, width, height, fg, bg, content, fontsize):
        self.font = pygame.font.SysFont('arial', fontsize)
        self.content = content
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.fg = fg
        self.bg = bg
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
