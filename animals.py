class Animal:
    def __init__(self, legs, name):
        self.legs = legs
        self.name = name

    def describe(self):
        return f"{self.name} has {self.legs} legs"

if __name__ == "__main__":
    test_animal = Animal(4, "Sparky")
    print(test_animal.describe())