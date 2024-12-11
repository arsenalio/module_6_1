
class Animal:
    alive = True
    fed = False
    def __init__(self, name):
        self.name = name

class Plant:
    edible = False  #
    def __init__(self, name):
        self.name = name

class Mammal(Animal):
    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False

class Predator(Animal):

    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False

class Fruit(Plant):
    edible = True

class Flower(Plant):
    pass




a1 = Predator('Lion')
a2 = Mammal('Sheep')
f1 = Plant('Grass')
f2 = Fruit('Orange')

print(a1.name)
print(f1.name)

print(a1.alive, f'- {a1.name} живой')
print(a2.fed, f'- {a2.name} голоден')

a1.eat(f1)
a2.eat(f2)
print(a1.alive, f'- {a1.name} умер')
print(a2.fed, f'- {a2.name} наелся')