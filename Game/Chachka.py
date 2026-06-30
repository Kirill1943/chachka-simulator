

class Chachka:
    def __init__(self, age, x, z):
        self.x, self.z = x, z
        self.age = age
        self.xp = 100
        self.eat = 100
        self.alive = True
        self.__size = [6, 6, 6]
    def Viy(self, scream: int = 2):
        if self.alive:
            scream = min(5, max(1, scream))
            print(f'Чачка викает: В{'И' * scream}')
        else:
            print('Чачка мертва... но кажется она хотела что-то викнуть')
    def Scream(self, scream: int = 10):
        if self.alive:
            scream = min(15, max(8, scream))
            print(f'Чачка орет: В{'И' * scream}')
        else:
            print('чачка мертва.. но она хотела что-то крикнуть')
    def eating(self):
        if self.alive:
            print('Чачка ест')
            self.eat += 3
            self.eat = max(0, min(self.eat, 100))
        else:
            print('чачка мертва.. но она хотела есть')