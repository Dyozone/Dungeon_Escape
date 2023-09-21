from interface import *
from pygame.math import Vector2


pygame.init()


clock = pygame.time.Clock()

while 1:
    clock.tick(60)
    for event in pygame.event.get():
        Display.exit(event.type)
    if Game.STATE == GameNow.Starting:
        Game.start_menu()
        if Game.RESET:
            Game.reset()
            continue
    if Game.STATE == GameNow.Over:
        Game.over_menu()
        if Game.RESET:
            Game.reset()
            continue
    elif Game.STATE == GameNow.Playing:

        screen.fill((255, 255, 255))
        player.pin_start()
        player.update()

        player.search_oil(world.puddles)

        world.draw(camera)

        for puddle in world.puddles:
            puddle.draw(camera)

        camera.scroll()
        for monster in monsters:
            monster.pin_start()
            monster.chase(player)
            monster.draw(camera)
            monster.check_state()

        player.draw(camera)
        player.check_state()
        #player.use_weapon()
        player.use_light_source()

        player.draw_lives()
        player.draw_oil()

        pygame.display.update()
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            Game.STATE = GameNow.Pausing
            continue
        if player.dies():
            Game.STATE = GameNow.Over
            continue
        if player.escapes():
            Game.STATE = GameNow.Won
            continue
    elif Game.STATE == GameNow.Pausing:
        Game.pause_menu()
    elif Game.STATE == GameNow.Won:
        Game.victory_menu()
        if Game.RESET:
            Game.reset()
            continue
