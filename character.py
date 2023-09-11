from pygame.math import Vector2
from world import *
from enum import IntEnum
from settings import *

world = Map('maps/map.tmx')
world.define_zones()


class State(IntEnum):
    IDLE = 0
    RUNNING = 1


class Character:
    def __init__(self, pos, folder):

        self.folder = folder
        self.currently = State.IDLE
        self.direction_right = True
        self.sprite = [
            {
                'counter': 0,
                'speed': 0.2,
                'length': 4
            },
            {
                'counter': 0,
                'speed': 0.3,
                'length': 4
            },
        ]
        self.default_img = Skins.LIBRARY[self.folder + '_idle_0']
        self.rect = self.default_img.get_rect()
        self.rect.topleft = pos
        self.trajectory = [pos, pos]

        self.pos = Vector2(pos)

        self.dummy_rect = self.rect
        self.spawn = Vector2(pos)

    def resume_spawn(self):
        self.pos = self.spawn
        self.rect.topleft = self.pos

    def pin_start(self):
        self.trajectory[0] = self.rect.topleft

    def check_state(self):
        self.trajectory[1] = self.rect.topleft
        if self.trajectory[0] != self.trajectory[1]:
            self.currently = State.RUNNING
        else:
            self.currently = State.IDLE

    def animation(self):
        return Skins.LIBRARY[
            str(self.folder + '_' + State(self.currently).name.lower() + '_' +
                str(int(self.sprite[int(self.currently)]['counter'])))]

    def collision_test(self, rect, obstacles):
        collisions = []
        for obstacle in obstacles:
            if rect.colliderect(obstacle):
                collisions.append(obstacle)
        return collisions

    def move(self, v):
        self.dummy_rect.centerx += v[0]
        self.dummy_rect.centery += v[1]
        if not self.collision_test(self.dummy_rect, world.blockers):
            self.pos.x += v[0]
            self.pos.y += v[1]
            if v[0] < 0:
                self.direction_right = False
            else:
                self.direction_right = True

    def update_sprite(self):
        if self.sprite[int(self.currently)]['counter'] \
                >= self.sprite[int(self.currently)]['length'] - 1:
            self.sprite[int(self.currently)]['counter'] = 0
        self.sprite[int(self.currently)]['counter'] += self.sprite[int(self.currently)][
            'speed']

    def draw(self, camera):
        self.update_sprite()
        if self.direction_right:
            screen.blit(self.animation(), (self.rect.topleft + camera.offset))
        else:
            screen.blit(pygame.transform.flip(self.animation(), True, False),
                        (self.rect.topleft + camera.offset))