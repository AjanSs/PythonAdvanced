greeting = "Hello"
name = "Bob"

def greet():
    global greeting
    name = "Alice"

    message = f"{greeting}, {name}!"
    print(message)

greet()

print(greeting)

print(name)