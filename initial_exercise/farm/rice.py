from farm.crop import Crop


class Rice(Crop):
    def water(self):
        self.grains += 5
    
    def ripe(self):
        return True if self.grains >= 15 else False

    def transplant(self):
        return