class Animal:
    def __init__(self,name) -> None:
        self.name = name

    def make_sound(self):
        print('animal making sound')
class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

class Goat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

     def make_sound(self):
        print('beh beh')

        
    


class Dog (Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

        def make_sound(self):
            print('ghew ghwq')
don = Cat('Real Don')
don.make_sound()

shepard = Dog('Local Shepard')
shepard.make_sound()

mess = Goat('L M')
mess.make_sound()