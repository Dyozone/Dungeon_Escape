from character import *
from pygame.math import Vector2


class Player(Character):
    def __init__(self, pos):
        folder = 'player'
        self.max_hp = 30
        self.hp = self.max_hp
        self.oil_capacity = 1000
        self.oil = self.oil_capacity
        self.collecting_oil = False
        Character.__init__(self, pos, folder)
        self.light_frame = 0
        self.light_radius = 300
        self.light_circle = pygame.Surface((Display.WIDTH, Display.HEIGHT))
        self.light_circle.set_colorkey((255, 255, 255))

    def draw_lives(self):
        counter = 0
        for full_heart in range((self.hp // 10 + 1) if (self.hp % 10 > 5) else (self.hp // 10)):
            counter += 1
            screen.blit(Skins.LIBRARY['ui_heart_full'], (
                [Skins.LIBRARY['ui_heart_full'].get_width() + Skins.LIBRARY['ui_heart_full'].get_width() * full_heart,
                 Skins.LIBRARY['ui_heart_full'].get_height()]))
        if 0 < self.hp % 10 <= 5:
            screen.blit(Skins.LIBRARY['ui_heart_half'], (
                [Skins.LIBRARY['ui_heart_full'].get_width() + Skins.LIBRARY['ui_heart_full'].get_width() * counter,
                 Skins.LIBRARY['ui_heart_full'].get_height()]))
            counter += 1

    def draw_oil(self):
        counter = 0
        for full_oil in range((self.oil // 100 + 1) if (self.oil % 100 > 50) else (self.oil // 100)):
            counter += 1
            screen.blit(Skins.LIBRARY['ui_oil_full'], (
                [Skins.LIBRARY['ui_oil_full'].get_width() + Skins.LIBRARY['ui_oil_full'].get_width() * full_oil,
                 Skins.LIBRARY['ui_heart_full'].get_height() * 2.5]))
        if 0 < self.oil % 100 <= 50:
            screen.blit(Skins.LIBRARY['ui_oil_half'], (
                [Skins.LIBRARY['ui_oil_full'].get_width() + Skins.LIBRARY['ui_oil_full'].get_width() * counter,
                 Skins.LIBRARY['ui_oil_full'].get_height() * 2.5]))
            counter += 1

    def reset_stats(self):
        self.oil = self.oil_capacity
        self.hp = self.max_hp

    def update(self):
        self.get_event()
        self.rect.topleft = self.pos

    def get_event(self):
        keys = pygame.key.get_pressed()
        is_press = any(keys)
        if keys[pygame.K_w]:
            self.v = (0, -5)
            self.move(self.v)
        if keys[pygame.K_s]:
            self.v = (0, +5)
            self.move(self.v)
        if keys[pygame.K_a]:
            self.v = (-5, 0)
            self.move(self.v)
        if keys[pygame.K_d]:
            self.v = (+5, 0)
            self.move(self.v)
        if is_press is False:
            self.v = (0, 0)

    def escapes(self):
        if self.rect.colliderect(world.door):
            return True

    def dies(self):
        if self.hp <= 0:
            return True

    def use_light_source(self):
        if self.oil > 0:
            self.light_frame += 1
            self.light_frame %= 70
            screen.blit(pygame.transform.scale_by(Skins.LIBRARY['item_lamp_' + str(self.light_frame // 10)], 0.4),
                        (screen.get_rect().centerx - self.rect.width + 50,
                            screen.get_rect().centery - self.rect.height / 3))
            if not self.collecting_oil:
                self.oil -= 1
        self.light_circle.fill(0)
        pygame.draw.circle(self.light_circle, (255, 255, 255),
                           center=(screen.get_rect().centerx + 37, screen.get_rect().centery + 27),
                           radius=self.oil * 0.3)
        screen.blit(self.light_circle, screen.get_rect())

    def use_weapon(self):
        screen.blit(pygame.transform.scale_by(Skins.LIBRARY['item_weapon_bow_2'], 4),
                    (screen.get_rect().centerx - self.rect.width + 125,
                     screen.get_rect().centery - self.rect.height / 6))
    def search_oil(self, puddles):
        found_oil = self.collision_test(self.rect, puddles)
        if not found_oil:
            self.collecting_oil = False
            return
        for puddle in found_oil:
            if puddle.empty or self.oil >= self.oil_capacity:
                self.collecting_oil = False
                return
            else:
                if self.oil + 10 < self.oil_capacity:
                    self.collecting_oil = True
                    if puddle.time_left > 0:
                        puddle.time_left -= 10
                    else:
                        puddle.empty = True
                    self.oil += 10
                else:
                    self.oil = self.oil_capacity
