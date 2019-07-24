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


if __name__ == "__main__":
    exit()
