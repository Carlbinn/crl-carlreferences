class Dog:
    """A simple attempt to mimic a dog"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        """An attempt to make the dog sit"""
        print(f"{self.name} is now sitting")

    def rollover(self):
        """An attempt to make the dog rollover"""
        print(f"{self.name} rolled over!")

my_dog = Dog('Yuki', 3)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog's age is {my_dog.age} years old.")
my_dog.sit()
my_dog.rollover()

your_dog = Dog('Aki', 5)
your_dog.sit()
your_dog.rollover()