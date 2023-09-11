import pygame
import random
import pytmx
from settings import *

screen = pygame.display.set_mode((640, 480))

Tiles.load()


class Puddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.empty = False
        self.time = 1000
        self.time_left = self.time
        self.states = [Tiles.LIBRARY['resources_oil_lake'], Tiles.LIBRARY['resources_hole_hole']]
        self.rect = self.states[self.empty].get_rect(topleft=(self.x, self.y))

    def drain(self):
        if self.time_left > 0:
            self.time_left -= 10
        else:
            self.empty = True

    def draw(self, camera):
        screen.blit(self.states[self.empty], (self.x + camera.offset.x, self.y + camera.offset.y))


class Map:
    def __init__(self, filename):
        self.tmx_data = pytmx.load_pygame(filename, pixelalpha=True)
        self.size = self.tmx_data.width * self.tmx_data.tilewidth, self.tmx_data.height * self.tmx_data.tileheight
        self.surface = self.render()
        self.paths = [[384.0, 512.0, 2816.0, 2240.0], [384.0, 512.0, 2816.0, 2240.0], [384.0, 512.0, 2816.0, 2240.0],
                      [384.0, 512.0, 2816.0, 2240.0], [3200.0, 1792.0, 1280.0, 768.0], [3200.0, 1792.0, 1280.0, 768.0],
                      [3200.0, 1792.0, 1280.0, 768.0], [3200.0, 1792.0, 1280.0, 768.0],
                      [4480.0, 1280.0, 2432.0, 3968.0],
                      [4480.0, 1280.0, 2432.0, 3968.0], [4480.0, 1280.0, 2432.0, 3968.0],
                      [4480.0, 1280.0, 2432.0, 3968.0],
                      [3200.0, 4288.0, 1280.0, 768.0], [3200.0, 4288.0, 1280.0, 768.0], [3200.0, 4288.0, 1280.0, 768.0],
                      [3200.0, 4288.0, 1280.0, 768.0], [576.0, 3136.0, 2624.0, 3584.0], [576.0, 3136.0, 2624.0, 3584.0],
                      [576.0, 3136.0, 2624.0, 3584.0], [576.0, 3136.0, 2624.0, 3584.0], [3200.0, 5824.0, 704.0, 768.0],
                      [3200.0, 5824.0, 704.0, 768.0], [3200.0, 5824.0, 704.0, 768.0], [3200.0, 5824.0, 704.0, 768.0],
                      [3904.0, 5696.0, 3264.0, 1600.0], [3904.0, 5696.0, 3264.0, 1600.0],
                      [3904.0, 5696.0, 3264.0, 1600.0],
                      [3904.0, 5696.0, 3264.0, 1600.0], [3904.0, 7296.0, 3008.0, 64.0], [3904.0, 7296.0, 3008.0, 64.0],
                      [3904.0, 7296.0, 3008.0, 64.0], [3904.0, 7296.0, 3008.0, 64.0], [7040.0, 7296.0, 128.0, 64.0],
                      [7040.0, 7296.0, 128.0, 64.0], [7040.0, 7296.0, 128.0, 64.0], [7040.0, 7296.0, 128.0, 64.0]]
        self.paths_rects = [pygame.rect.Rect(384, 512, 2816, 2240), pygame.rect.Rect(384, 512, 2816, 2240),
                            pygame.rect.Rect(384, 512, 2816, 2240), pygame.rect.Rect(384, 512, 2816, 2240),
                            pygame.rect.Rect(3200, 1792, 1280, 768), pygame.rect.Rect(3200, 1792, 1280, 768),
                            pygame.rect.Rect(3200, 1792, 1280, 768), pygame.rect.Rect(3200, 1792, 1280, 768),
                            pygame.rect.Rect(4480, 1280, 2432, 3968), pygame.rect.Rect(4480, 1280, 2432, 3968),
                            pygame.rect.Rect(4480, 1280, 2432, 3968), pygame.rect.Rect(4480, 1280, 2432, 3968),
                            pygame.rect.Rect(3200, 4288, 1280, 768), pygame.rect.Rect(3200, 4288, 1280, 768),
                            pygame.rect.Rect(3200, 4288, 1280, 768), pygame.rect.Rect(3200, 4288, 1280, 768),
                            pygame.rect.Rect(576, 3136, 2624, 3584), pygame.rect.Rect(576, 3136, 2624, 3584),
                            pygame.rect.Rect(576, 3136, 2624, 3584), pygame.rect.Rect(576, 3136, 2624, 3584),
                            pygame.rect.Rect(3200, 5824, 704, 768), pygame.rect.Rect(3200, 5824, 704, 768),
                            pygame.rect.Rect(3200, 5824, 704, 768), pygame.rect.Rect(3200, 5824, 704, 768),
                            pygame.rect.Rect(3904, 5696, 3264, 1600), pygame.rect.Rect(3904, 5696, 3264, 1600),
                            pygame.rect.Rect(3904, 5696, 3264, 1600), pygame.rect.Rect(3904, 5696, 3264, 1600),
                            pygame.rect.Rect(3904, 7296, 3008, 64), pygame.rect.Rect(3904, 7296, 3008, 64),
                            pygame.rect.Rect(3904, 7296, 3008, 64), pygame.rect.Rect(3904, 7296, 3008, 64),
                            pygame.rect.Rect(7040, 7296, 128, 64), pygame.rect.Rect(7040, 7296, 128, 64),
                            pygame.rect.Rect(7040, 7296, 128, 64), pygame.rect.Rect(7040, 7296, 128, 64)]
        self.blockers = []
        self.puddles = []
        self.door = None

    def render(self):
        temp_surface = pygame.Surface(self.size)
        tw = self.tmx_data.tilewidth
        th = self.tmx_data.tileheight
        gt = self.tmx_data.get_tile_image_by_gid

        if self.tmx_data.background_color:
            temp_surface.fill(self.tmx_data.background_color)

        for layer in self.tmx_data.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = gt(gid)
                    if tile:
                        temp_surface.blit(tile, (x * tw, y * th))

            elif isinstance(layer, pytmx.TiledImageLayer):
                image = gt(layer.gid)
                if image:
                    temp_surface.blit(image, (0, 0))
        return temp_surface

    def define_zones(self):
        for tile_object in self.tmx_data:
            properties = tile_object.__dict__
            if properties['name'] == 'blocker':
                x = properties['x']
                y = properties['y']
                width = properties['width']
                height = properties['height']
                new_rect = pygame.Rect(x, y, width, height)
                self.blockers.append(new_rect)
            if properties['name'] == 'door':
                x = properties['x']
                y = properties['y']
                width = properties['width']
                height = properties['height']
                self.door = pygame.Rect(x, y, width, height)
        for path in range(len(self.paths)):
            for i in range(2):
                self.puddles.append(
                    Puddle(self.paths[path][0] + Tiles.SIZE + random.randint(0, int(
                        self.paths[path][2] // Tiles.SIZE) - 1) * Tiles.SIZE,
                           self.paths[path][1] + Tiles.SIZE + random.randint(0, int(
                               self.paths[path][3] // Tiles.SIZE) - 1) * Tiles.SIZE))
    def draw(self, camera):
        screen.blit(self.surface, (camera.offset.x, camera.offset.y))