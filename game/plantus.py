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


if __name__ == "__main__":
    exit()
