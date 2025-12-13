from Module1.variables import result


def greet():
    print("Hello World")

greet()

def greet_person(name):
    print("Hello,", name)

greet_person("Emily")
greet_person("Alice")

'''
def add(x,y):
    z=x+y
     return z

add(3,7)
'''

def add(x,y):
    z=x+y
    return z

result = add(3,7)

print("the result of 3+7 =", result)