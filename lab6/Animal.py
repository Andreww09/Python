# ex5

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Mammal(Animal):
    def __init__(self, name, age, biped):
        super().__init__(name, age)
        self.biped = biped

    def run(self):
        print(f"{self.name} is running")


class Bird(Animal):
    def __init__(self, name, age, flies):
        super().__init__(name, age)
        self.flies = flies

    def fly(self):
        if self.flies:
            print(f"{self.name} is flying")
        else:
            print(f"{self.name} cannot fly")


class Fish(Animal):
    def __init__(self, name, age, freshwater):
        super().__init__(name, age)
        self.freshwater = freshwater

    def swim(self):
        print(f"{self.name} is swimming")


mammal = Mammal("dog1", 10, False)
bird = Bird("bird1", 2, False)
fish = Fish("fish1", 1, True)

mammal.run()
bird.fly()
fish.swim()