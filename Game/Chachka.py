

class Chachka:
    def __init__(self, age):
        self.age = age
        self.__size = [6, 6, 6]
    def Viy(self, scream: int = 2):
        scream = min(5, max(1, scream))
        print(f'Чачка викает: В{"И" * scream}')
    def Scream(self, scream: int = 10):
        scream = min(15, max(8, scream))
        print(f"Чачка орет: В{"И" * scream}")

