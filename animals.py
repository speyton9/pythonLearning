class Animal:
    def __init__(self, legs, name):
        self.legs = legs
        self.name = name

    def describe(self):
        return f"{self.name} has {self.legs} legs"
    
class Dog(Animal):
    def __init__(self, breed, legs, name):
        super().__init__(legs, name)
        self.breed = breed

    def bark(self):
        return f"{self.name} is a {self.breed} with {self.legs} who barks a lot"

if __name__ == "__main__":
    test_animal = Animal(4, "Sparky")
    print(test_animal.describe())

    test_dog = Dog(4, "Baxter", "Terrier")
    print(test_dog.bark())