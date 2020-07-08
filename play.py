import pyglet
from game import chrono, plantus, windo, depot

WIDTH = 1280
HEIGHT = 600
UPS = 60

chronometer = chrono.Chronometer()
the_plant = plantus.Plant()
res = depot.Resources()
game = windo.GameWindow(timer=chronometer, plant=the_plant, plant_image=res.plant_img, width=WIDTH, height=HEIGHT)


def update(dt):
    the_plant.set_growth_speed()
    the_plant.set_water_speed()

    game.set_atp()
    game.set_water()
    game.set_leaves()
    game.set_roots()
    game.set_time()

    the_plant.atp += the_plant.growth_speed / UPS
    the_plant.water += the_plant.water_speed / UPS

    chronometer.time += game.game_speed / UPS


if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1. / UPS)
    pyglet.app.run()
