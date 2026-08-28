class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def speak(self):
        print("Hi my name is", self.name, "and I am", self.age, "years old")
    def change_age(self, new_age):
        self.age = new_age

pluto = Dog("Pluto", 55)
dufus = Dog("Dufus", 6)
pluto.speak()
dufus.speak()
pluto.change_age(5)
pluto.speak()
