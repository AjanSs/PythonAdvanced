from Module8.access_modifiers.public_modifiers import my_class


class MyClass:
    def __init__(self):
        self.__private_variable = "This is a private variable"

    def __private_method(self):
        print("This is a private method")

myclass = MyClass()
print(myclass.__private_variable)
print(myclass.__private_method())