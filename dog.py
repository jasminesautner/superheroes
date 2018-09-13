dogs = list()
dogs.append("German Shepherd")
dogs.append("Poodle")
print(dogs)

class Dog:
    greeting = "Woof! \n"
    trick = 1

    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.greeting)

    def roll_over(self):
        print(self.trick)

if __name__ == "main":
    my_dog = Dog()
    my_dog.bark()

# my_dog = Dog("Spot")
# my_dog.bark()
# my_other_dog = Dog("Annie")

my_first_dog = Dog("Annie")
my_second_dog = Dog("Wyatt")

# print(my_dog.name)
# print(my_other_dog.name)
# my_other_dog.bark()

print(__name__)

print(my_first_dog.name)
print(my_second_dog.name)
my_first_dog.bark()
my_second_dog.bark()
my_first_dog.roll_over()



