import pyglet

WIDTH = 1280
HEIGHT = 600
UPS = 60

pyglet.resource.path = ['.']
pyglet.resource.reindex()

plant_image = pyglet.resource.image("plant.png")
plant_image.anchor_x = plant_image.width / 2


class GameWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.leaf_cost_atp = 3
        self.leaf_cost_water = 3
        self.root_cost_atp = 2

        self.growth_speed = 0
        self.water_speed = 0

        self.atp = 0
        self.water = 0

        self.leaves = 1
        self.roots = 1

        self.game_batch = pyglet.graphics.Batch()
        self.background = pyglet.graphics.OrderedGroup(0)
        self.foreground = pyglet.graphics.OrderedGroup(1)

        self.row_1_height = self.height / 2
        self.row_1_length = 5
        self.atp_text = pyglet.text.Label(text="", batch=self.game_batch, x=self.width * 1 / self.row_1_length,
                                          y=self.row_1_height, group=self.foreground)
        self.leaves_text = pyglet.text.Label(text="", batch=self.game_batch, x=self.width * 2 / self.row_1_length,
                                             y=self.row_1_height, group=self.foreground)
        self.roots_text = pyglet.text.Label(text="", batch=self.game_batch, x=self.width * 3 / self.row_1_length,
                                            y=self.row_1_height, group=self.foreground)
        self.water_text = pyglet.text.Label(text="", batch=self.game_batch, x=self.width * 4 / self.row_1_length,
                                            y=self.row_1_height, group=self.foreground)

        self.plant = pyglet.sprite.Sprite(img=plant_image, x=self.width / 2, y=0, batch=self.game_batch,
                                          group=self.background)
        self.plant.scale = 0.1

    def set_atp(self):
        self.atp_text.text = f"ATP: {int(self.atp)}"

    def set_water(self):
        self.water_text.text = f"Water: {int(self.water)}"

    def set_leaves(self):
        self.leaves_text.text = f"Leaves: {self.leaves}"

    def set_growth_speed(self):
        self.growth_speed = self.leaves

    def set_water_speed(self):
        self.water_speed = self.roots

    def set_roots(self):
        self.roots_text.text = f"Roots: {self.roots}"

    def on_draw(self):
        game.clear()
        self.game_batch.draw()

    def set_atp_white(self, time):
        self.atp_text.color = (255, 255, 255, 255)

    def set_water_white(self, time):
        self.water_text.color = (255, 255, 255, 255)

    def on_key_press(self, symbol, modifiers):
        if symbol is pyglet.window.key.L:
            if all([self.atp >= self.leaf_cost_atp, self.water >= self.leaf_cost_water]):
                self.atp -= self.leaf_cost_atp
                self.water -= self.leaf_cost_water
                self.leaves += 1
                self.plant.scale += 0.1
            if self.atp < self.leaf_cost_atp:
                self.atp_text.color = (242, 38, 19, 255)
                pyglet.clock.schedule_once(self.set_atp_white, .5)
            if self.water < self.leaf_cost_water:
                self.water_text.color = (242, 38, 19, 255)
                pyglet.clock.schedule_once(self.set_water_white, .5)

        if symbol is pyglet.window.key.R and self.atp > self.root_cost_atp:
            self.atp -= self.root_cost_atp
            self.roots += 1


game = GameWindow(width=WIDTH, height=HEIGHT)


def update(dt):
    game.set_growth_speed()
    game.set_water_speed()
    game.set_atp()
    game.set_water()
    game.set_leaves()
    game.set_roots()

    game.atp += game.growth_speed / UPS
    game.water += game.water_speed / UPS


if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1. / UPS)
    pyglet.app.run()
