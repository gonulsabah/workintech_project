class Crop:
    def __init__(self):
        self.grains = 0
    
    def water(self):
        self.grains += 10
    
    def ripe(self):
        return True if self.grains >= 15 else False