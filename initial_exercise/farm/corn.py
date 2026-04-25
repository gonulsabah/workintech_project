from farm.crop import Crop


class Corn(Crop):
    def water(self):
        self.grains += 10