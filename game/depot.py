import pyglet


class Resources:
    def __init__(self):
        pyglet.resource.path = ['graphics']
        pyglet.resource.reindex()

        self.plant_img = pyglet.resource.image("plant.png")
        self.plant_img.anchor_x = self.plant_img.width / 2


if __name__ == "__main__":
    exit()
