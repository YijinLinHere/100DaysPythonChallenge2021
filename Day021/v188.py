# 188. Class Inheritance

class Animal:
    def __init__(self):
        self.num_eye = 2

    def breathe(self):
        print("Inhale, exhale.")
    
    def makeSound(self):
        print("ohhhhhh")


class Fish(Animal):
    def __init__(self):
        super().__init__() # this is not necessary, but recommended
    
    def breathe(self):
        # inherit
        super().breathe()
        print("doing this under water")

    def swim(self):
        print("moving in the water.")


nemo = Fish()
nemo.swim()
nemo.makeSound() # method inherit from Animal
nemo.breathe()   # method extended
print(nemo.num_eye)