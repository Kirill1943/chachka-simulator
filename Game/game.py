from Map.maps import Map


class ClassGame:
    def __init__(self, time: int = 1):
        self.maps: list[Map] = []
        self.time = time # как быстро будет течь время
        self.ticks_passed = time
    def tick(self):
        for map in self.maps:
            for chack in map.chaks:
                chack.age += self.time / 100
        self.ticks_passed += self.time
    def add_map(self, map: Map):
        self.maps.append(map)