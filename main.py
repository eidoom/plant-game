import pyglet

WIDTH = 1280
HEIGHT = 600
UPS = 60

pyglet.resource.path = ['.']
pyglet.resource.reindex()

plant_image = pyglet.resource.image("plant.png")
plant_image.anchor_x = plant_image.width / 2


class Chronometer:
    def __init__(self):
        self.time = 0  # total minutes

    def get_day(self):
        return self.time / (60 * 24)

    def get_hour(self):
        return (self.time % (60 * 24)) / 60

    def get_minute(self):
        return self.time % 60

    @staticmethod
    def format_time(time_quantity):
        the_time = int(time_quantity)
        return the_time if the_time > 9 else f"0{the_time}"


class Plant:
    def __init__(self):
        self.leaf_cost_atp = 3
        self.leaf_cost_water = 3
        self.root_cost_atp = 2

        self.growth_speed = 0
        self.water_speed = 0

        self.atp = 0
        self.water = 0

        self.leaves = 1
        self.roots = 1

    def set_growth_speed(self):
        self.growth_speed = self.leaves

    def set_water_speed(self):
        self.water_speed = self.roots


class GameWindow(pyglet.window.Window):
    def __init__(self, timer, plant, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.timer = timer
        self.plant = plant

        self.game_speed = 10

        self.game_batch = pyglet.graphics.Batch()
        self.background = pyglet.graphics.OrderedGroup(0)
        self.foreground = pyglet.graphics.OrderedGroup(1)

        self.row_1_height = self.height / 2
        self.row_1_length = 6
        self.atp_text = pyglet.text.Label(text="", batch=self.game_batch, x=self.width * 1 / self.row_1_length,
                                          y=self.row_1_height, group=self.foreground)
        self.leaves_text = pyglet.text.Label(text="", batch=self.game_batch, x=self.width * 2 / self.row_1_length,
                                             y=self.row_1_height, group=self.foreground)
        self.roots_text = pyglet.text.Label(text="", batch=self.game_batch, x=self.width * 3 / self.row_1_length,
                                            y=self.row_1_height, group=self.foreground)
        self.water_text = pyglet.text.Label(text="", batch=self.game_batch, x=self.width * 4 / self.row_1_length,
                                            y=self.row_1_height, group=self.foreground)
        self.time_text = pyglet.text.Label(text="", batch=self.game_batch, x=self.width * 5 / self.row_1_length,
                                           y=self.row_1_height, group=self.foreground)
        self.plant_sprite = pyglet.sprite.Sprite(img=plant_image, x=self.width / 2, y=0, batch=self.game_batch,
                                                 group=self.background)
        self.plant_sprite.scale = 0.1

    def set_atp(self):
        self.atp_text.text = f"ATP: {int(self.plant.atp)}"

    def set_water(self):
        self.water_text.text = f"Water: {int(self.plant.water)}"

    def set_leaves(self):
        self.leaves_text.text = f"Leaves: {self.plant.leaves}"

    def set_roots(self):
        self.roots_text.text = f"Roots: {self.plant.roots}"

    def set_time(self):
        self.time_text.text = f"Time: {int(self.timer.get_day())}.{self.timer.format_time(self.timer.get_hour())}:" \
            f"{self.timer.format_time(self.timer.get_minute())}"

    def on_draw(self):
        game.clear()
        self.game_batch.draw()

    def set_atp_white(self, dt):
        self.atp_text.color = (255, 255, 255, 255)

    def set_water_white(self, dt):
        self.water_text.color = (255, 255, 255, 255)

    def on_key_press(self, symbol, modifiers):
        if symbol is pyglet.window.key.L:
            if all([self.plant.atp >= self.plant.leaf_cost_atp, self.plant.water >= self.plant.leaf_cost_water]):
                self.plant.atp -= self.plant.leaf_cost_atp
                self.plant.water -= self.plant.leaf_cost_water
                self.plant.leaves += 1
                self.plant_sprite.scale += 0.1
            if self.plant.atp < self.plant.leaf_cost_atp:
                self.atp_text.color = (242, 38, 19, 255)
                pyglet.clock.schedule_once(self.set_atp_white, .5)
            if self.plant.water < self.plant.leaf_cost_water:
                self.water_text.color = (242, 38, 19, 255)
                pyglet.clock.schedule_once(self.set_water_white, .5)

        if symbol is pyglet.window.key.R:
            if self.plant.atp >= self.plant.root_cost_atp:
                self.plant.atp -= self.plant.root_cost_atp
                self.plant.roots += 1
            else:
                self.atp_text.color = (242, 38, 19, 255)
                pyglet.clock.schedule_once(self.set_atp_white, .5)


chronometer = Chronometer()
the_plant = Plant()
game = GameWindow(timer=chronometer, plant=the_plant, width=WIDTH, height=HEIGHT)


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
