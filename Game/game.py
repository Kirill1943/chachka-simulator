

class ClassGame:
    def __init__(self, time: int = 0.01):
        self.maps = []
        self.time = time # как быстро будет течь время
    def tick(self):
        for map in self.maps:
            for chack in map:
                chack.age += self.time
            

Game = ClassGame()
