class Person:
    def __init__(self):
        self.__name = "Student"
        self.__age = 10

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

# Example usage:
p = Person()
print(p.get_name())      # Output: Student
p.set_name("John")
p.set_age(15)
print(p.get_name())      # Output: John
print(p.get_age())       # Output: 15