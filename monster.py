from character import *
from pygame.math import Vector2

class Monster(Character):
    def __init__(self, pos, species='demon', variant='big', family=""):
        self.attack_rate = 30
        self.cooldown_timer = 0
        self.damage = 5
        self.speed = 1
        self.__family = family
        self.__species = species
        self.__variant = variant
        folder = str(
            'monster_' + ((self.__family + '_') if self.__family != '' else '') + self.__species + '_' + self.__variant)
        Character.__init__(self, pos, folder)

    def chase(self, who):
        distance_x = who.pos.x - self.pos.x
        distance_y = who.pos.x - self.pos.y
        distance = (distance_x ** 2 + distance_y ** 2) ** 0.5
        if 0 < abs(distance) < 2000:
            self.move((distance_x / distance * self.speed, distance_y / distance * self.speed))
        if self.rect.colliderect(who.rect):
            self.cooldown_timer += 1
            if self.cooldown_timer % self.attack_rate == 0:
                who.hp -= self.damage
        else:
            self.cooldown_timer = 0