class Animal:
    def __init__(self, alive=True, fed=False, name=''):
        self.alive = alive
        self.fed = fed
        self.name = name


class Plant:
    def __init__(self, edible=False, name=''):
        self.edible = edible
        self.name = name


class Predator(Animal):
    def __init__(self, name):
        super().__init__(True, False, name)

    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible:
                print(f'{self.name} съел {food.name}')
                self.fed = True
            else:
                print(f'{self.name} не стал есть {food.name}')
                self.fed = False
                self.alive = False
        else:
            print('Не еда')


class Mammal(Animal):
    def __init__(self, name):
        super().__init__(True, False, name)

    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible:
                print(f'{self.name} съел {food.name}')
                self.fed = True
            else:
                print(f'{self.name} не стал есть {food.name}')
                self.fed = False
                self.alive = False
        else:
            print('Не еда')


class Flower(Plant):
    def __init__(self, name):
        super().__init__(False, name)


class Fruit(Plant):
    def __init__(self, name):
        super().__init__(True, name)


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
