class Animal:
    def __init__(self, name, food, habitat, reproduction):
        self.name = name
        self.food = food
        self.habitat = habitat
        self.reproduction = reproduction

class Rhinoceros(Animal):
    def __init__(self, name, food, habitat, reproduction, horn_size, skin_color):
        super().__init__(name, food, habitat, reproduction)
        self.horn_size = horn_size
        self.skin_color = skin_color

    def charge(self):
        print(f"{self.name} is charging.")

    def graze(self):
        print(f"{self.name} is grazing on grass.")

class Fish(Animal):
    def __init__(self, name, food, habitat, reproduction, fin_type, scale_color):
        super().__init__(name, food, habitat, reproduction)
        self.fin_type = fin_type
        self.scale_color = scale_color

    def swim(self):
        print(f"{self.name} is swimming.")

    def feed(self):
        print(f"{self.name} is feeding on {self.food}.")

class Snake(Animal):
    def __init__(self, name, food, habitat, reproduction, venomous, length):
        super().__init__(name, food, habitat, reproduction)
        self.venomous = venomous
        self.length = length

    def slither(self):
        print(f"{self.name} is slithering.")

    def hunt(self):
        print(f"{self.name} is hunting for prey.")

# Contoh penggunaan:
rhino = Rhinoceros("Rhino", "grass", "savannah", "live birth", "large", "gray")
rhino.charge()
rhino.graze()

fish = Fish("Nemo", "plankton", "ocean", "lay eggs", "pectoral", "orange")
fish.swim()
fish.feed()

snake = Snake("Python", "small mammals", "jungle", "lay eggs", "venomous", "long")
snake.slither()
snake.hunt()